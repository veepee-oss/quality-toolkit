"""
Unit tests for SFTP service with Paramiko
"""
import unittest
from unittest.mock import Mock, patch, MagicMock
import stat

from quality_toolkit.services.sftp import Sftp


class TestSftpService(unittest.TestCase):
    """Tests for Sftp class"""

    @patch('quality_toolkit.services.sftp.paramiko.Transport')
    @patch('quality_toolkit.services.sftp.paramiko.SFTPClient')
    def test_sftp_init(self, mock_sftp_client, mock_transport):
        """Test SFTP connection initialization"""
        mock_transport_instance = Mock()
        mock_transport.return_value = mock_transport_instance
        mock_sftp_instance = Mock()
        mock_sftp_client.from_transport.return_value = mock_sftp_instance

        sftp = Sftp('test.host.com', 'testuser', 'testpass')

        mock_transport.assert_called_once_with(('test.host.com', 22))
        mock_transport_instance.connect.assert_called_once_with(
            username='testuser',
            password='testpass'
        )
        mock_sftp_client.from_transport.assert_called_once_with(mock_transport_instance)
        self.assertEqual(sftp.transport, mock_transport_instance)
        self.assertEqual(sftp.sftp, mock_sftp_instance)
        print("✅ SFTP initialization test passed")

    @patch('quality_toolkit.services.sftp.paramiko.Transport')
    @patch('quality_toolkit.services.sftp.paramiko.SFTPClient')
    def test_sftp_upload_file(self, mock_sftp_client, mock_transport):
        """Test file upload"""
        mock_sftp_instance = Mock()
        mock_sftp_client.from_transport.return_value = mock_sftp_instance

        sftp = Sftp('test.host.com', 'testuser', 'testpass')
        sftp.upload_file('/local/path/file.txt', '/remote/path/file.txt')

        mock_sftp_instance.put.assert_called_once_with(
            '/local/path/file.txt',
            '/remote/path/file.txt'
        )
        print("✅ SFTP file upload test passed")

    @patch('quality_toolkit.services.sftp.paramiko.Transport')
    @patch('quality_toolkit.services.sftp.paramiko.SFTPClient')
    def test_sftp_list_files(self, mock_sftp_client, mock_transport):
        """Test file listing"""
        mock_sftp_instance = Mock()
        mock_sftp_client.from_transport.return_value = mock_sftp_instance

        # Mock files in directory
        mock_sftp_instance.listdir.return_value = ['file1.txt', 'file2.txt', 'file3.csv']

        # Mock stat for each file
        def mock_stat(path):
            mock_stat_result = Mock()
            mock_stat_result.st_mode = stat.S_IFREG  # Regular file
            return mock_stat_result

        mock_sftp_instance.stat.side_effect = mock_stat

        sftp = Sftp('test.host.com', 'testuser', 'testpass')
        files = sftp.list_files('/remote/path/', 'nonexistent')

        mock_sftp_instance.chdir.assert_called_once_with('/remote/path/')
        # Files that don't match the filter are returned
        self.assertEqual(len(files), 3)
        print("✅ SFTP file listing test passed")

    @patch('quality_toolkit.services.sftp.paramiko.Transport')
    @patch('quality_toolkit.services.sftp.paramiko.SFTPClient')
    def test_sftp_close(self, mock_sftp_client, mock_transport):
        """Test SFTP connection closure"""
        mock_transport_instance = Mock()
        mock_transport.return_value = mock_transport_instance
        mock_sftp_instance = Mock()
        mock_sftp_client.from_transport.return_value = mock_sftp_instance

        sftp = Sftp('test.host.com', 'testuser', 'testpass')
        sftp.close()

        mock_sftp_instance.close.assert_called_once()
        mock_transport_instance.close.assert_called_once()
        print("✅ SFTP connection closure test passed")


if __name__ == '__main__':
    unittest.main(verbosity=2)

