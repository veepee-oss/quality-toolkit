import logging
from pathlib import Path

import pysftp


class Sftp:

    def __init__(self, host, username, password):
        logging.getLogger('paramiko').setLevel(logging.WARNING)
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None
        self.sftp = pysftp.Connection(host=host, username=username, password=password, cnopts=cnopts)

    def upload_file(self, local_file, remote_path):
        """
        Upload a local file into the sftp path
        """
        self.sftp.put(local_file, remote_path)

    def list_files(self, remote_path, file):
        """
        List files into the remote path
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
        Close the sftp connection
        """
        self.sftp.close()
