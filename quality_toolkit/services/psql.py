"""
Service PSQL
"""
import logging

import psycopg2
from psycopg2.extras import RealDictCursor

from quality_toolkit.services.base_sql import BaseSql


class ConnectionPsql(BaseSql):
    """docstring for ConnectionPsql"""

    def __init__(self, db_config):
        logging.debug("db_config: %s", db_config)
        self.connection = psycopg2.connect(**db_config, cursor_factory=RealDictCursor)
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        logging.debug("execute_query, query: %s, params: %s", query, params)
        self.cursor.execute(query, params)
        self.connection.commit()
