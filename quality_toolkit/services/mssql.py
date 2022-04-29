"""
Service MSSQL
"""
import logging

import pytds

from quality_toolkit.helpers.local_functions import find_resource
from quality_toolkit.services.base_sql import BaseSql


class ConnectionMssql(BaseSql):
    """docstring for ConnectionMssql"""

    def __init__(self, db_config):
        logging.debug("db_config: %s", db_config)
        self.connection = pytds.connect(**db_config, as_dict=True, autocommit=True)
        self.cursor = self.connection.cursor()

    def execute_script(self, script_name, script_path='resources/scripts/', params=None):
        logging.debug("execute_script, script: %s%s, params: %s", script_path, script_name, params)
        with open(find_resource(script_name, script_path), 'r') as script:
            query = script.read() if params is None else script.read() % params
            self.cursor.execute(query)
            self.connection.commit()
            return 0

    def execute_ps(self, ps_name, params=None):
        logging.debug("execute_ps, ps_name: %s, params: %s", ps_name, params)
        if params is None:
            self.cursor.callproc(ps_name)
        else:
            self.cursor.callproc(ps_name, params)
        self.connection.commit()
        return self.cursor.fetchone()

    def execute_query(self, query, params=None):
        logging.debug("execute_query, query: %s, params: %s", query, params)
        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)
        self.connection.commit()
        return 0
