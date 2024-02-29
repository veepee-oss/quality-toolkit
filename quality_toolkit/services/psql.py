"""
Service PSQL
"""
import logging

import psycopg2
from psycopg2.extras import RealDictCursor

from quality_toolkit.services.base_sql import BaseSql


class ConnectionPsql(BaseSql):
    """
    ConnectionPsql class for establishing a connection and executing queries on a PostgreSQL database.

    Args:
        db_config (dict): A dictionary containing the database configuration parameters.

    Methods:
        __init__:
            Initializes the ConnectionPsql object.

        execute_query:
            Executes a query on the PostgreSQL database.

    """

    def __init__(self, db_config):
        """
        Initializes the ConnectionPsql object.

        Args:
            db_config (dict): A dictionary containing the database configuration parameters.

        Returns:
            None
        """
        logging.debug("db_config: %s", db_config)
        self.connection = psycopg2.connect(**db_config, cursor_factory=RealDictCursor)
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        """
        Executes a query on the PostgreSQL database.

        Args:
            query (str): The SQL query to be executed.
            params (tuple): Optional parameters to be used in the query.

        Returns:
            None
        """
        logging.debug("execute_query, query: %s, params: %s", query, params)
        self.cursor.execute(query, params)
        self.connection.commit()
