"""
Generic BaseSql Extension
"""
import logging
import time
from abc import ABC


class BaseSql(ABC):
    """docstring for BaseSql"""

    def fetch_all(self, query, params=None, nb_retry=5, wait_time=5):
        """
        Get a list of dictionary
        """
        retry = 1 if nb_retry > 0 else 0
        while retry <= nb_retry:
            logging.debug("%s/%s - fetch_all, query: %s, params: %s", retry, nb_retry, query, params)
            self.cursor.execute(query, params)
            result = self.cursor.fetchall()
            if result is not None and result:
                return result
            if retry > nb_retry:
                log = 'error executing query "{}"'.format(query)
                logging.error(log)
                break
            retry += 1
            time.sleep(wait_time)

    def fetch_one(self, query, params=None, nb_retry=5, wait_time=5):
        """
        Get only one dictionary
        """
        retry = 1 if nb_retry > 0 else 0
        while retry <= nb_retry:
            logging.debug("%s/%s - fetch_one, query: %s, params: %s", retry, nb_retry, query, params)
            self.cursor.execute(query, params)
            result = self.cursor.fetchone()
            if result is not None and result:
                return result
            if retry > nb_retry:
                log = 'error executing query "{}"'.format(query)
                logging.error(log)
                break
            retry += 1
            time.sleep(wait_time)

    def close(self):
        self.connection.close()
        self.cursor.close()
