#!/usr/bin/env python3
"""Render branded HTML to PDF with Chrome and run the document release audit."""

from __future__ import annotations

import argparse
import os
import signal
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path


DEFAULT_CHROME = Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")


def stop_process_group(process: subprocess.Popen[bytes]) -> None:
    if process.poll() is not None:
        return
    try:
        os.killpg(process.pid, signal.SIGTERM)
        process.wait(timeout=3)
    except (ProcessLookupError, subprocess.TimeoutExpired):
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        process.wait(timeout=3)


def chrome_path(explicit: str | None) -> Path:
    candidates = [
        Path(explicit).expanduser() if explicit else None,
        Path(os.environ["CHROME_PATH"]).expanduser() if os.environ.get("CHROME_PATH") else None,
        DEFAULT_CHROME,
        Path(shutil.which("google-chrome") or ""),
        Path(shutil.which("chromium") or ""),
    ]
    for candidate in candidates:
        if candidate and str(candidate) and candidate.is_file():
            return candidate.resolve()
    raise FileNotFoundError("Google Chrome or Chromium was not found")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_html", type=Path)
    parser.add_argument("output_pdf", type=Path)
    parser.add_argument("--brand", choices=("research-platform", "dfh", "academic", "neutral"), default="neutral")
    parser.add_argument("--final", action="store_true", help="Run strict final-output checks")
    parser.add_argument("--chrome", help="Explicit Chrome or Chromium executable")
    parser.add_argument("--virtual-time-budget", type=int, default=8000, help="Milliseconds allowed for fonts and scripts")
    parser.add_argument("--skip-audit", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source = args.input_html.expanduser().resolve()
    output = args.output_pdf.expanduser().resolve()

    if not source.is_file():
        print(f"FAIL: HTML source not found: {source}", file=sys.stderr)
        return 2
    if source.suffix.lower() not in {".html", ".htm"}:
        print(f"FAIL: input must be HTML: {source}", file=sys.stderr)
        return 2

    output.parent.mkdir(parents=True, exist_ok=True)
    output.unlink(missing_ok=True)

    try:
        chrome = chrome_path(args.chrome)
    except FileNotFoundError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 2

    with tempfile.TemporaryDirectory(prefix="research-platform-pdf-") as profile:
        command = [
            str(chrome),
            "--headless=new",
            "--disable-gpu",
            "--hide-scrollbars",
            "--allow-file-access-from-files",
            "--no-pdf-header-footer",
            "--run-all-compositor-stages-before-draw",
            f"--virtual-time-budget={args.virtual_time_budget}",
            f"--user-data-dir={profile}",
            f"--print-to-pdf={output}",
            source.as_uri(),
        ]
        process = subprocess.Popen(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True,
        )
        deadline = time.monotonic() + 90
        last_size = -1
        stable_since: float | None = None
        rendered = False

        while time.monotonic() < deadline:
            returncode = process.poll()
            if output.is_file() and output.stat().st_size > 0:
                size = output.stat().st_size
                if size == last_size:
                    stable_since = stable_since or time.monotonic()
                    if time.monotonic() - stable_since >= 3:
                        rendered = True
                        stop_process_group(process)
                        break
                else:
                    last_size = size
                    stable_since = None
            if returncode is not None:
                rendered = returncode == 0 and output.is_file() and output.stat().st_size > 0
                break
            time.sleep(0.25)
        else:
            stop_process_group(process)

    if not rendered:
        detail = "Chrome did not produce a stable PDF within 90 seconds"
        print(f"FAIL: {detail}", file=sys.stderr)
        return 3

    if not args.skip_audit:
        audit = Path(__file__).with_name("audit_document_output.py")
        command = [sys.executable, str(audit), str(output), "--brand", args.brand]
        if args.final:
            command.append("--final")
        result = subprocess.run(command, check=False)
        if result.returncode != 0:
            return result.returncode

    print(f"WROTE: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
