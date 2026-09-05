#!/usr/bin/env python3
"""Install a verified public workforce without overwriting recipient changes."""
import argparse, hashlib, json, os, shutil
from pathlib import Path

def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def checked_path(root, rel):
    relative = Path(rel)
    if relative.is_absolute() or not relative.parts or any(p in {".", ".."} for p in relative.parts):
        raise ValueError("Unsafe install path: " + rel)
    dest = root / relative
    for path in (dest, *dest.parents):
        if path == root.parent: break
        if path.is_symlink(): raise ValueError("Symlink destination refused: " + rel)
        if path != dest and path.exists() and not path.is_dir():
            raise ValueError("Parent is not a directory: " + rel)
    if dest.exists() and not dest.is_file(): raise ValueError("File destination required: " + rel)
    return dest

def serialized(value): return json.dumps(value, indent=2)

def install(source, target, agents_dir=None):
    source = source.resolve()
    target = target.expanduser()
    if target.is_symlink(): raise ValueError("Install root symlink refused")
    target = target.resolve()
    source_marker = checked_path(source, "PUBLIC_BUILD.json")
    receipt = json.loads(source_marker.read_text())
    paths = {row["path"]: row["sha256"] for row in receipt["files"]}
    if len(paths) != len(receipt["files"]) or set(paths) & {"PUBLIC_BUILD.json", "bindings.json", ".workforce-install.json"}:
        raise ValueError("Duplicate or reserved manifest destination")
    for rel, expected in paths.items():
        p = checked_path(source, rel)
        if digest(p) != expected:
            raise ValueError("Source integrity failure: " + rel)
    paths["PUBLIC_BUILD.json"] = digest(source_marker)
    marker = checked_path(target, "PUBLIC_BUILD.json")
    stamp = checked_path(target, ".workforce-install.json")
    config = checked_path(target, "bindings.json")
    previous = {}
    if stamp.exists():
        recorded = json.loads(stamp.read_text())
        if not marker.exists(): raise ValueError("Managed installation receipt missing")
        old_receipt = json.loads(marker.read_text())
        expected_stamp = {"schema_version": 1, "version": old_receipt["version"],
            "files": {**{r["path"]: r["sha256"] for r in old_receipt["files"]}, "PUBLIC_BUILD.json": digest(marker)}}
        if recorded != expected_stamp or stamp.read_text() != serialized(expected_stamp):
            raise ValueError("Recipient installation metadata conflict; preserve and install to a fresh directory")
        previous = recorded["files"]
    for rel, expected in paths.items():
        dest = checked_path(target, rel)
        if dest.exists() and digest(dest) not in {expected, previous.get(rel)}:
            raise ValueError("Recipient edit preserved; update conflict: " + rel)
    agent_sources = []
    if agents_dir:
        agents_dir = agents_dir.expanduser()
        if agents_dir.is_symlink(): raise ValueError("Custom profile root symlink refused")
        agents_dir = agents_dir.resolve()
        for rel in sorted(paths):
            if not rel.startswith("plugins/institutional-skills/agents/") or not rel.endswith(".toml"): continue
            p = source / rel
            dest = checked_path(agents_dir, p.name)
            if dest.exists() and digest(dest) != digest(p):
                raise ValueError("Existing custom profile preserved: " + p.name)
            agent_sources.append((p, dest))
    # All payload, metadata, bindings and optional profile destinations passed preflight.
    for rel in paths:
        dest = target / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.exists() or digest(dest) != paths[rel]: shutil.copy2(source / rel, dest)
    if not config.exists():
        shutil.copy2(target / "bindings.example.json", config)
        os.chmod(config, 0o600)
    stamp.write_text(serialized({"schema_version": 1, "version": receipt["version"], "files": paths}))
    for p, dest in agent_sources:
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.exists(): shutil.copy2(p, dest)
    return {"installed": True, "version": receipt["version"], "files": len(paths), "external_actions": 0}

if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--target", type=Path, required=True)
    p.add_argument("--agents-dir", type=Path)
    args = p.parse_args()
    print(json.dumps(install(Path(__file__).parent, args.target, args.agents_dir)))
