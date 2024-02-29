"""
Generic BaseSql Extension
"""
import logging
import time
from abc import ABC


class BaseSql(ABC):
    """Base class for SQL operations."""

    def fetch_all(self, query, params=None, nb_retry=5, wait_time=5):
        """
        Get a list of dictionaries.

        Args:
            query (str): The SQL query to execute.
            params (tuple, optional): The parameters to substitute in the query. Defaults to None.
            nb_retry (int, optional): The number of retries in case of query failure.
                Defaults to 5.
            wait_time (int, optional): The waiting time between retries in seconds. Defaults to 5.

        Returns:
            list: A list of dictionaries representing the query result.

        """
        retry = 1 if nb_retry > 0 else 0
        while retry <= nb_retry:
            logging.debug(f"{retry}/{nb_retry} - fetch_all, query: {query}, params: {params}")
            self.cursor.execute(query, params)
            result = self.cursor.fetchall()
            if result is not None and result:
                return result
            if retry > nb_retry:
                log = f'error executing query "{query}"'
                logging.error(log)
                break
            retry += 1
            time.sleep(wait_time)
        return None

    def fetch_one(self, query, params=None, nb_retry=5, wait_time=5):
        """
        Get only one dictionary.

        Args:
            query (str): The SQL query to execute.
            params (tuple, optional): The parameters to substitute in the query. Defaults to None.
            nb_retry (int, optional): The number of retries in case of query failure.
                Defaults to 5.
            wait_time (int, optional): The waiting time between retries in seconds. Defaults to 5.

        Returns:
            dict: A dictionary representing the first row of the query result.

        """
        retry = 1 if nb_retry > 0 else 0
        while retry <= nb_retry:
            logging.debug(f"{retry}/{nb_retry} - fetch_all, query: {query}, params: {params}")
            self.cursor.execute(query, params)
            result = self.cursor.fetchone()
            if result is not None and result:
                return result
            if retry > nb_retry:
                log = f'error executing query "{query}"'
                logging.error(log)
                break
            retry += 1
            time.sleep(wait_time)
        return None

    def close(self):
        """
        Close the database connection and cursor.
        """
        self.connection.close()
        self.cursor.close()
