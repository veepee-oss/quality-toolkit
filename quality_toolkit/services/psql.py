"""
Service PSQL
"""
import logging
from base_sql import BaseSql
import psycopg2
from psycopg2.extras import RealDictCursor

class ConnectionPsql(BaseSql):
    """docstring for ConnectionPsql"""

    def __init__(self, db_config):
        logging.debug("db_config: %s", db_config)
        self.connection = psycopg2.connect(**db_config, cursor_factory=RealDictCursor)
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        logging.debug("execute_query, query: %s, params: %s", query, params)
        self.cursor.execute(query, params)
        self.cursor.commit()
