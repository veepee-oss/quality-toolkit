"""
Service MSSQL
"""
import logging

import pytds

from helpers import local_functions as helpers

class ConnectionMssql():
    """docstring for ConnectionMssql"""

    def __init__(self, db_config):
        logging.debug("db_config: %s", db_config)
        self.connection = pytds.connect(**db_config, as_dict=True)
        self.cursor = self.connection.cursor()

    def fetch_all(self, query, params=None):
        logging.debug("fetch_all, query: %s, params: %s", query, params)
        self.cursor.execute(query, params)
        result = self.cursor.fetchall()
        return result

    def fetch_one(self, query, params=None):
        logging.debug("fetch_one, query: %s, params: %s", query, params)
        self.cursor.execute(query, params)
        result = self.cursor.fetchone()
        return result

    def execute_script(self, script_name, params=None):
        logging.debug("execute_script, script_name: %s, params: %s", script_name, params)
        with open(helpers.get_project_file_path(script_name), 'r') as script:
            query = script.read() if params is None else script.read() % params
            self.cursor.execute(query)
            self.connection.commit()
            return 0

    def execute_ps(self, ps_name, params=None):
        logging.debug("execute_ps, ps_name: %s, params: %s", ps_name, params)
        result = (self.cursor.callproc(ps_name) if params is None else self.cursor.callproc(ps_name, params))
        self.connection.commit()
        return result if result else 0

    def execute_query(self, query, params=None):
        logging.debug("execute_query, query: %s, params: %s", query, params)
        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)
        self.connection.commit()
        return 0

    def close(self):
        self.connection.close()
        self.cursor.close()
