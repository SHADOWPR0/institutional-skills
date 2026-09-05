import importlib.util, json, subprocess, sys, tempfile, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

class ConsumerTests(unittest.TestCase):
    def test_metadata_conflict_preserved_before_install(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "recipient"
            target.mkdir()
            marker = target / "PUBLIC_BUILD.json"
            marker.write_text('{"recipient_note": "preserve"}')
            result = subprocess.run([sys.executable, "-B", str(ROOT / "install.py"), "--target", str(target)], capture_output=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(marker.read_text(), '{"recipient_note": "preserve"}')
            self.assertFalse((target / "README.md").exists())
    def test_bindings_symlink_rejected_before_install(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "recipient"
            target.mkdir()
            external = Path(tmp) / "protected"
            external.write_text("preserve")
            (target / "bindings.json").symlink_to(external)
            result = subprocess.run([sys.executable, "-B", str(ROOT / "install.py"), "--target", str(target)], capture_output=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(external.read_text(), "preserve")
            self.assertFalse((target / "README.md").exists())
    def test_install_execute_recover_and_preserve_config(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "recipient"
            subprocess.run([sys.executable, str(ROOT / "install.py"), "--target", str(target)], check=True, capture_output=True)
            config = target / "bindings.json"
            config.write_text('{"recipient_setting": true}')
            subprocess.run([sys.executable, str(ROOT / "install.py"), "--target", str(target)], check=True, capture_output=True)
            self.assertTrue(json.loads(config.read_text())["recipient_setting"])
            result = subprocess.run([sys.executable, "-B", str(target / "examples/run_demo.py"), "--output", str(Path(tmp) / "artifacts")], check=True, capture_output=True, text=True)
            receipt = json.loads(result.stdout)
            self.assertTrue(receipt["demo_passed"])
            self.assertTrue(receipt["recovery_verified"])
            self.assertEqual(receipt["ratios"]["dscr"], 2)
            self.assertEqual(receipt["external_actions"], 0)
            self.assertFalse(receipt["native_agent_invoked"])
            self.assertIn("credit_committee", receipt["roles_executed"])
            self.assertIn("communications", receipt["roles_executed"])
    def test_profiles_and_capability_coverage(self):
        root = ROOT / "plugins/institutional-skills"
        registry = json.loads((root / "skills/financial-house-operating-system/references/capability-registry.json").read_text())
        self.assertEqual(len(registry["execution_roles"]), 14)
        self.assertGreaterEqual(len(registry["capabilities"]), 169)
        self.assertEqual(len(list((root / "agents").glob("*.toml"))), 14)
        self.assertEqual(set(registry["master_financial_owners"]), {"investment-management", "universal-banker"})

if __name__ == "__main__": unittest.main()
