"""Unit tests for SysKit."""

import unittest
from syskit.cli import check_doctor


class TestSysKit(unittest.TestCase):

    def test_doctor_runs_without_exception(self):
        try:
            check_doctor()
            success = True
        except Exception:
            success = False
        self.assertTrue(success)


if __name__ == "__main__":
    unittest.main()
