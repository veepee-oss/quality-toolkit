"""
Service PSQL
"""
import logging
import time

import psycopg2
from psycopg2.extras import RealDictCursor


class ConnectionPsql():
    """docstring for ConnectionPsql"""

    def __init__(self, db_config):
        logging.debug("db_config: %s", db_config)
        self.connection = psycopg2.connect(**db_config, cursor_factory=RealDictCursor)
        self.cursor = self.connection.cursor()

    def fetch_all(self, query, params=None):
        logging.debug("fetch_all, query: %s, params: %s", query, params)
        self.cursor.execute(query, params)
        result = self.cursor.fetchall()
        return result

    def fetch_one(self, query, params=None):
        logging.debug("fetch_one, query: %s, params: %s", query, params)
        retry = 0
        while True:
            self.cursor.execute(query, params)
            result = self.cursor.fetchone()
            if result is not None and result:
                return result
            elif retry < 5:
                retry += 1
                time.sleep(5)
            else:
                log = 'error executing query "{}"'.format(query)
                logging.error(log)
                break

    def execute_query(self, query, params=None):
        logging.debug("execute_query, query: %s, params: %s", query, params)
        self.cursor.execute(query, params)
        self.cursor.commit()

    def close(self):
        self.connection.close()
        self.cursor.close()
