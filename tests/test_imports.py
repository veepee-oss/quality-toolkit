"""
Quality-toolkit module import tests
Verifies that all modules can be imported without error
"""
import unittest


class TestImports(unittest.TestCase):
    """Test that all modules import correctly"""

    def test_import_services_sftp(self):
        """Test SFTP service import"""
        try:
            from quality_toolkit.services.sftp import Sftp
            self.assertIsNotNone(Sftp)
            print("✅ SFTP service imported successfully")
        except ImportError as e:
            self.fail(f"❌ SFTP import failed: {e}")

    def test_import_services_psql(self):
        """Test PostgreSQL service import"""
        try:
            from quality_toolkit.services.psql import ConnectionPsql
            self.assertIsNotNone(ConnectionPsql)
            print("✅ PostgreSQL service imported successfully")
        except ImportError as e:
            self.fail(f"❌ PostgreSQL import failed: {e}")

    def test_import_services_mssql(self):
        """Test MSSQL service import"""
        try:
            from quality_toolkit.services.mssql import ConnectionMssql
            self.assertIsNotNone(ConnectionMssql)
            print("✅ MSSQL service imported successfully")
        except ImportError as e:
            self.fail(f"❌ MSSQL import failed: {e}")

    def test_import_services_sso(self):
        """Test SSO service import"""
        try:
            from quality_toolkit.services.sso import Sso
            self.assertIsNotNone(Sso)
            print("✅ SSO service imported successfully")
        except ImportError as e:
            self.fail(f"❌ SSO import failed: {e}")

    def test_import_helpers_api_functions(self):
        """Test API functions import"""
        try:
            from quality_toolkit.helpers.api_functions import send_api_request
            self.assertIsNotNone(send_api_request)
            print("✅ API functions imported successfully")
        except ImportError as e:
            self.fail(f"❌ API functions import failed: {e}")

    def test_import_helpers_local_functions(self):
        """Test local functions import"""
        try:
            from quality_toolkit.helpers.local_functions import find_resource
            self.assertIsNotNone(find_resource)
            print("✅ Local functions imported successfully")
        except ImportError as e:
            self.fail(f"❌ Local functions import failed: {e}")

    def test_import_helpers_ui_functions(self):
        """Test UI functions import"""
        try:
            from quality_toolkit.helpers.ui_functions import install_selenium_webdriver
            self.assertIsNotNone(install_selenium_webdriver)
            print("✅ UI functions imported successfully")
        except ImportError as e:
            self.fail(f"❌ UI functions import failed: {e}")


if __name__ == '__main__':
    unittest.main(verbosity=2)

