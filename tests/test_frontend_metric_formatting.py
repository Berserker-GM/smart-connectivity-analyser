import subprocess
import shutil
import unittest
from pathlib import Path

class TestFrontendNetworkMetricFormatting(unittest.TestCase):
    """
    Test suite verifying that frontend network metric formatting tests
    execute and pass.
    """

    def test_node_metric_formatting_tests_pass(self):
        """Execute the Node.js test runner for frontend network metric formatting."""
        node_bin = shutil.which("node")
        self.assertIsNotNone(node_bin, "Node.js executable is required to run frontend tests")

        repo_root = Path(__file__).resolve().parent.parent
        test_file = repo_root / "tests" / "metric_formatting.test.js"
        self.assertTrue(test_file.exists(), f"Test file {test_file} must exist")

        result = subprocess.run(
            [node_bin, "--test", str(test_file)],
            cwd=str(repo_root),
            capture_output=True,
            text=True
        )

        self.assertEqual(
            result.returncode,
            0,
            f"Node test runner failed with exit code {result.returncode}.\nOutput:\n{result.stdout}\nError:\n{result.stderr}"
        )
        self.assertIn("fail 0", result.stdout)
        self.assertIn("pass 57", result.stdout)

if __name__ == "__main__":
    unittest.main()
