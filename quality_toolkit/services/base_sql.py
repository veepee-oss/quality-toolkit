"""
Generic BaseSql Extension
"""
import logging
import time
from abc import ABC

class BaseSql(ABC):
    """docstring for BaseSql"""

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

    def close(self):
        self.connection.close()
        self.cursor.close()
