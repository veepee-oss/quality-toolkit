"""
Python compatibility tests
Verifies that the code works correctly with the installed Python version
"""
import unittest
import sys


class TestPythonCompatibility(unittest.TestCase):
    """Python compatibility tests"""

    def test_python_version_minimum(self):
        """Test that Python >= 3.10"""
        version = sys.version_info
        self.assertGreaterEqual(version.major, 3, "Python 3.x required")
        self.assertGreaterEqual(version.minor, 10, "Python 3.10+ required")
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")

    def test_python_version_supported(self):
        """Test that Python <= 3.13"""
        version = sys.version_info
        if version.major == 3:
            self.assertLessEqual(version.minor, 13, "Python 3.13 is the maximum tested version")
        print(f"✅ Python {version.major}.{version.minor} in supported range (3.10-3.13)")

    def test_required_modules_available(self):
        """Test that all required modules are available"""
        required_modules = [
            'psycopg2',
            'requests',
            'pytz',
            'pytds',
            'selenium',
            'keycloak',
            'paramiko',
            'playwright'
        ]

        missing_modules = []
        for module_name in required_modules:
            try:
                __import__(module_name)
            except ImportError:
                missing_modules.append(module_name)

        if missing_modules:
            self.fail(f"❌ Missing modules: {', '.join(missing_modules)}")

        print(f"✅ All {len(required_modules)} required modules are available")


if __name__ == '__main__':
    unittest.main(verbosity=2)

