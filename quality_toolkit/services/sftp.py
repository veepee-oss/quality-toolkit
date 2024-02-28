import logging
from pathlib import Path

import pysftp


class Sftp:
    """
    Sftp class for performing SFTP operations.

    Args:
        host (str): The hostname or IP address of the remote server.
        username (str): The username to authenticate with on the remote server.
        password (str): The password to authenticate with on the remote server.

    Methods:
        __init__:
            Initializes the Sftp object.

        upload_file:
            Uploads a local file to the specified remote path on the server.

        list_files:
            Lists files in the specified remote path on the server.

        close:
            Closes the SFTP connection.
    """

    def __init__(self, host, username, password):
        """
        Initializes the Sftp object.

        Args:
            host (str): The hostname or IP address of the remote server.
            username (str): The username to authenticate with on the remote server.
            password (str): The password to authenticate with on the remote server.
        """
        logging.getLogger('paramiko').setLevel(logging.WARNING)
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None
        self.sftp = pysftp.Connection(host=host, username=username, password=password, cnopts=cnopts)

    def upload_file(self, local_file, remote_path):
        """
        Uploads a local file to the specified remote path on the server.

        Args:
            local_file (str): The path to the local file to be uploaded.
            remote_path (str): The path on the server where the file should be uploaded.
        """
        self.sftp.put(local_file, remote_path)

    def list_files(self, remote_path, file):
        """
        Lists files in the specified remote path on the server.

        Args:
            remote_path (str): The path on the server to list files from.
            file (str): The name of the file to filter the list by.

        Returns:
            list_files (list): A list of file names in the remote path that match the provided file name.
        """
        list_files = []
        self.sftp.cwd(remote_path)
        list_elt = self.sftp.listdir()
        for elt in list_elt:
            p = Path(elt)
            if self.sftp.isfile(elt) and elt.replace("".join(p.suffixes), "") == file:
                self.sftp.remove(elt)
            elif self.sftp.isfile(elt):
                list_files.append(elt)
        return list_files

    def close(self):
        """
        Closes the SFTP connection.
        """
        self.sftp.close()
