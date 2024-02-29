"""
Service MSSQL
"""
import logging

import pytds

from quality_toolkit.helpers.local_functions import find_resource
from quality_toolkit.services.base_sql import BaseSql


class ConnectionMssql(BaseSql):
    """
    A class representing a connection to a Microsoft SQL Server.

    Args:
        db_config (dict): A dictionary containing the configuration details for the database connection.

    Attributes:
        connection: A pytds.Connection object representing the connection to the database.
        cursor: A pytds.Cursor object representing the cursor used to execute SQL queries.

    Methods:
        execute_script:
            Executes a SQL script from a file.

            Args:
                script_name (str): The name of the script.
                script_path (str, optional): The path where the script is located. Defaults to 'resources/scripts/'.
                params (Union[dict, None], optional): The parameters to be substituted into the script. Defaults to None.

            Returns:
                int: A return value indicating the status of the execution. (0 indicates success)

        execute_ps:
            Executes a stored procedure.

            Args:
                ps_name (str): The name of the stored procedure.
                params (Union[list, None], optional): The parameters to be passed to the stored procedure. Defaults to None.

            Returns:
                any: The result of the execution, typically the first row returned by the stored procedure.

        execute_query:
            Executes a SQL query.

            Args:
                query (str): The SQL query to be executed.
                params (Union[tuple, None], optional): The parameters to be passed to the query. Defaults to None.

            Returns:
                int: A return value indicating the status of the execution. (0 indicates success)

    Note:
        - The `db_config` dictionary should contain the necessary connection details, such as host, port, database name, username, and password.
        - The `as_dict` and `autocommit` parameters are set to True by default.
        - The `execute_script`, `execute_ps`, and `execute_query` methods execute the provided SQL script, stored procedure, and SQL query, respectively.
        - The `execute_script` method can optionally accept parameters to be substituted in the script using string formatting.
        - The `execute_ps` and `execute_query` methods can optionally accept parameters to be passed to the stored procedure or query, respectively.

    Usage Example:
        db_config = {
            "host": "localhost",
            "port": 1433,
            "database": "mydatabase",
            "user": "myusername",
            "password": "mypassword"
        }

        connection = ConnectionMssql(db_config)
        connection.execute_script("myscript.sql")
        result = connection.execute_ps("mystoredprocedure", [param1, param2])
        connection.execute_query("SELECT * FROM mytable")
    """

    def __init__(self, db_config):
        """
        Initializes a new instance of the ConnectionMssql class.

        Args:
            db_config (dict): A dictionary containing the configuration details for the database connection.
        """
        logging.debug("db_config: %s", db_config)
        self.connection = pytds.connect(**db_config, as_dict=True, autocommit=True)
        self.cursor = self.connection.cursor()

    def execute_script(self, script_name, script_path='resources/scripts/', params=None):
        """
        Executes a SQL script from a file.

        Args:
            script_name (str): The name of the script.
            script_path (str, optional): The path where the script is located. Defaults to 'resources/scripts/'.
            params (Union[dict, None], optional): The parameters to be substituted into the script. Defaults to None.

        Returns:
            int: A return value indicating the status of the execution. (0 indicates success)
        """
        logging.debug("execute_script, script: %s%s, params: %s", script_path, script_name, params)
        with open(find_resource(script_name, script_path), 'r', encoding='UTF-8') as script:
            query = script.read() if params is None else script.read() % params
            self.cursor.execute(query)
            self.connection.commit()
            return 0

    def execute_ps(self, ps_name, params=None):
        """
        Executes a stored procedure.

        Args:
            ps_name (str): The name of the stored procedure.
            params (Union[list, None], optional): The parameters to be passed to the stored procedure. Defaults to None.

        Returns:
            any: The result of the execution, typically the first row returned by the stored procedure.
        """
        logging.debug("execute_ps, ps_name: %s, params: %s", ps_name, params)
        if params is None:
            self.cursor.callproc(ps_name)
        else:
            self.cursor.callproc(ps_name, params)
        self.connection.commit()
        return self.cursor.fetchone()

    def execute_query(self, query, params=None):
        """
        Executes a SQL query.

        Args:
            query (str): The SQL query to be executed.
            params (Union[tuple, None], optional): The parameters to be passed to the query. Defaults to None.

        Returns:
            int: A return value indicating the status of the execution. (0 indicates success)
        """
        logging.debug("execute_query, query: %s, params: %s", query, params)
        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)
        self.connection.commit()
        return 0
