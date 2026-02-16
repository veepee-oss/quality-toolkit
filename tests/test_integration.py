"""
Basic integration tests
Verifies that classes can be instantiated and used in a basic way
"""
import unittest
from unittest.mock import patch, Mock


class TestBasicIntegration(unittest.TestCase):
    """Basic integration tests"""

    def test_package_version(self):
        """Test that the package has a version"""
        try:
            import quality_toolkit
            # Package should be importable
            self.assertIsNotNone(quality_toolkit)
            print("✅ quality_toolkit package imported successfully")
        except ImportError as e:
            self.fail(f"❌ Unable to import quality_toolkit: {e}")

    @patch('quality_toolkit.services.sftp.paramiko.Transport')
    @patch('quality_toolkit.services.sftp.paramiko.SFTPClient')
    def test_sftp_workflow(self, mock_sftp_client, mock_transport):
        """Test complete SFTP workflow"""
        from quality_toolkit.services.sftp import Sftp

        # Setup mocks
        mock_transport_instance = Mock()
        mock_transport.return_value = mock_transport_instance
        mock_sftp_instance = Mock()
        mock_sftp_client.from_transport.return_value = mock_sftp_instance
        mock_sftp_instance.listdir.return_value = []

        # Create a connection
        sftp = Sftp('test.example.com', 'user', 'pass')
        self.assertIsNotNone(sftp)

        # Use methods
        sftp.upload_file('/local/file.txt', '/remote/file.txt')
        files = sftp.list_files('/remote/path/', 'test')
        sftp.close()

        # Verify calls
        mock_sftp_instance.put.assert_called_once()
        mock_sftp_instance.close.assert_called_once()
        mock_transport_instance.close.assert_called_once()

        print("✅ Complete SFTP workflow tested successfully")

    @patch('quality_toolkit.helpers.api_functions.requests.request')
    def test_api_workflow(self, mock_request):
        """Test complete API workflow"""
        from quality_toolkit.helpers.api_functions import send_api_request

        # Mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'data': 'test'}
        mock_request.return_value = mock_response

        # Make a request
        response = send_api_request('GET', 'https://api.test.com/endpoint')

        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
        mock_request.assert_called_once()

        print("✅ Complete API workflow tested successfully")

    def test_all_services_importable(self):
        """Test that all services can be imported together"""
        try:
            from quality_toolkit.services.sftp import Sftp
            from quality_toolkit.services.psql import ConnectionPsql
            from quality_toolkit.services.mssql import ConnectionMssql
            from quality_toolkit.services.sso import Sso
            from quality_toolkit.helpers.api_functions import send_api_request
            from quality_toolkit.helpers.local_functions import find_resource
            from quality_toolkit.helpers.ui_functions import install_selenium_webdriver

            # All should be importable
            self.assertIsNotNone(Sftp)
            self.assertIsNotNone(ConnectionPsql)
            self.assertIsNotNone(ConnectionMssql)
            self.assertIsNotNone(Sso)
            self.assertIsNotNone(send_api_request)
            self.assertIsNotNone(find_resource)
            self.assertIsNotNone(install_selenium_webdriver)

            print("✅ All services can be imported together")
        except ImportError as e:
            self.fail(f"❌ Import error: {e}")


if __name__ == '__main__':
    unittest.main(verbosity=2)

