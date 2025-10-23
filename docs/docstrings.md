<a id="helpers"></a>

# helpers

<a id="helpers.api_functions"></a>

# helpers.api\_functions

All methods link to APIs

<a id="helpers.api_functions.send_api_request"></a>

### send\_api\_request

```python
def send_api_request(method,
                     url,
                     status_code=None,
                     nb_retry=5,
                     wait_time=10,
                     timeout=60,
                     **kwargs)
```

Constructs and sends a Request object.

**Arguments**:

- `method` _str_ - Method for the new Request object: 'GET', 'OPTIONS', 'HEAD', 'POST', 'PUT', 'PATCH', or 'DELETE'.
- `url` _str_ - URL for the new Request object.
- `status_code` _List[int]_ - List to get the expected status code.
- `nb_retry` _int_ - Integer to set the number of possible retries.
- `wait_time` _int, optional_ - Integer to set the waiting time between each try.
- `params` _dict, optional_ - Dictionary, list of tuples or bytes to send in the query string for the Request.
- `data` _dict, optional_ - Dictionary, list of tuples, bytes, or file-like object to send in the body of the Request.
- `json` _optional_ - A JSON serializable Python object to send in the body of the Request.
- `headers` _dict, optional_ - Dictionary of HTTP Headers to send with the Request.
- `cookies` _optional_ - Dict or CookieJar object to send with the Request.
- `files` _dict, optional_ - Dictionary of 'name': file-like-objects (or {'name': file-tuple'}) for multipart encoding upload.
  'file-tuple' can be a 2-tuple ('filename', fileobj'), 3-tuple ('filename', fileobj', 'content_type')'
  or a 4-tuple ('filename', fileobj', 'content_type', custom_headers'), where 'content-type' is a string
  defining the content type of the given file and 'custom_headers' a dict-like object containing additional headers
  to add for the file.
- `auth` _optional_ - Auth tuple to enable Basic/Digest/Custom HTTP Auth.
- `timeout` _float or tuple, optional_ - How many seconds to wait for the server to send data before giving up, as a float, or a (connect timeout,
  read timeout) tuple.
- `allow_redirects` _bool, optional_ - Boolean. Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection. Defaults to True.
- `proxies` _optional_ - Dictionary mapping protocol to the URL of the proxy.
- `verify` _optional_ - Either a boolean, in which case it controls whether we verify the server's TLS certificate, or a string, in which
  case it must be a path to a CA bundle to use. Defaults to True.
- `stream` _optional_ - If False, the response content will be immediately downloaded.
- `cert` _optional_ - If String, path to SSL client cert file (.pem). If Tuple, ('cert', 'key') pair.
  

**Returns**:

- `Response` - Response object.

<a id="helpers.local_functions"></a>

# helpers.local\_functions

All methods link to the local environment

<a id="helpers.local_functions.compare_values"></a>

### compare\_values

```python
def compare_values(symbol, arg1, arg2) -> bool
```

Compare two values for equality. Return a Syntax Error if the symbol is not found.

**Arguments**:

- `symbol` _str_ - Symbol to use for comparison ('==', '<', '<=', '>=', '>').
- `arg1` _Any_ - First value to compare.
- `arg2` _Any_ - Second value to compare.
  

**Returns**:

- `bool` - True if the comparison is successful, False otherwise.
  

**Raises**:

- `SyntaxError` - If the symbol variable in the argument is not found.

<a id="helpers.local_functions.find_resource"></a>

### find\_resource

```python
def find_resource(name: str, filepath: str = 'resources/') -> Path
```

Help to find a resource in a project.

**Arguments**:

- `name` _str_ - Name of the resource.
- `filepath` _str, optional_ - Default file path of the resource.
  

**Returns**:

- `Path` - The path of the resource.
  

**Raises**:

- `FileNotFoundError` - If the resource is not found.

<a id="helpers.local_functions.import_recurcively_modules"></a>

### import\_recurcively\_modules

```python
def import_recurcively_modules(path_file: str) -> None
```

Import all modules in a package.

**Arguments**:

- `path_file` _str_ - Path of the file/module.
  

**Returns**:

  None

<a id="helpers.local_functions.get_timezone_paris"></a>

### get\_timezone\_paris

```python
def get_timezone_paris(timezone: str = 'Europe/Paris') -> datetime
```

Get the current datetime in the Paris timezone.

**Arguments**:

- `timezone` _str, optional_ - Timezone to use.
  

**Returns**:

- `datetime` - Current datetime in the specified timezone.

<a id="helpers.local_functions.response_message"></a>

### response\_message

```python
def response_message(message: str,
                     response: requests.Response,
                     password: bool = False,
                     truncate_content: int = 0,
                     truncate_body: int = 0) -> str
```

Show the response with all information to have a better debug.

**Arguments**:

- `message` _str_ - A message to explain the request or the error.
- `response` _requests.Response_ - The request response.
- `password` _bool, optional_ - If the header contains secure data, it will not be shown. Defaults to False.
- `truncate_content` _int, optional_ - Truncate content to the defined size, -1 to deactivate, 0 to show all content. Defaults to 0.
- `truncate_body` _int, optional_ - Truncate body to the defined size, -1 to deactivate, 0 to deactivate. Defaults to 0.
  

**Returns**:

- `str` - The formatted response message.


#### Examples:

```python
from quality_toolkit.helpers.local_functions import response_message

...
assert response.status_code == 204, response_message('Failed to get information', response, truncate_content=20, is_header_secure=False)
...
```

Result :

```text
Assertion Failed: Failed to get information from SAP,
    - code: 200
    - content: {"d":{"results":[{"_
    - method: GET
    - url: http://localhost?test=1
    - header: the header contain a secure data, it can't to be showed
    - body: No body
```
<a id="helpers.ui_functions"></a>

# helpers.ui\_functions

All methods link to the ui

<a id="helpers.ui_functions.install_selenium_webdriver"></a>

### install\_selenium\_webdriver

```python
def install_selenium_webdriver(remote_url='http://127.0.0.1:4444/wd/hub',
                               browser='chrome',
                               headless=True)
```

Method to install the Selenium WebDriver.

**Arguments**:

- `remote_url` _str, optional_ - Either a string representing the URL of the remote server or a custom RemoteConnection object.
  Defaults to 'http://127.0.0.1:4444/wd/hub'.
- `browser` _str, optional_ - Define which type of browser to instantiate. Possible values are 'chrome', 'firefox', or 'edge'.
  Opera is not supported by Selenium: https://github.com/robotframework/SeleniumLibrary/pull/1782.
  Defaults to 'chrome'.
- `headless` _bool, optional_ - Set the headless option, which is only available for Chrome and Firefox.
  Defaults to True.

<a id="helpers.ui_functions.install_sync_playwright"></a>

### install\_sync\_playwright

```python
def install_sync_playwright(browser='chromium', **kwargs)
```

Method to install the Sync Playwright browser.

**Arguments**:

- `browser` _str, optional_ - The browser name, possible values are 'chrome', 'firefox', or 'webkit'. Defaults to 'chrome'.
- `executable_path` _Union[pathlib.Path, str, None], optional_ - Path to a browser executable to run instead of the bundled one,
  if `executable_path` is a relative path, then it is resolved relative to the current working directory.
  Note that Playwright only works with the bundled Chromium, Firefox, or WebKit, use at your own risk.
  Defaults to None.
- `channel` _Union[str, None], optional_ - Browser distribution channel, supported values are 'chrome', 'chrome-beta',
  'chrome-dev', 'chrome-canary', 'msedge', 'msedge-beta', 'msedge-dev', 'msedge-canary'.
  Read more about using [Google Chrome and Microsoft Edge](../browsers.md#google-chrome--microsoft-edge).
  Defaults to None.
- `args` _Union[List[str], None], optional_ - Additional arguments to pass to the browser instance,
  the list of Chromium flags can be found [here](http://peter.sh/experiments/chromium-command-line-switches/).
  Defaults to None.
- `ignore_default_args` _Union[List[str], bool, None], optional_ - If True, Playwright does not pass its own configuration args
  and only uses the ones from `args`. If a list is given, it filters out the given default arguments.
  Dangerous option; use with care. Defaults to False.
- `handle_sigint` _Union[bool, None], optional_ - Close the browser process on Ctrl-C. Defaults to True.
- `handle_sigterm` _Union[bool, None], optional_ - Close the browser process on SIGTERM. Defaults to True.
- `handle_sighup` _Union[bool, None], optional_ - Close the browser process on SIGHUP. Defaults to True.
- `timeout` _Union[float, None], optional_ - Maximum time in milliseconds to wait for the browser instance to start.
  Defaults to 30000 (30 seconds). Pass 0 to disable timeout.
- `env` _Union[Dict[str, Union[bool, float, str]], None], optional_ - Specify environment variables that will be visible to the browser.
  Defaults to `process.env`.
- `headless` _Union[bool, None], optional_ - Whether to run the browser in headless mode.
  Defaults to True unless the `devtools` option is True.
- `devtools` _Union[bool, None], optional_ - **Chromium-only** Whether to auto-open a Developer Tools panel for each tab.
  If True, the `headless` option will be set to False.
  proxy (Union[
- `{'server'` - str, 'bypass': Union[str, None], 'username': Union[str, None], 'password': Union[str, None]}, None
  ], optional): Network proxy settings.
- `downloads_path` _Union[pathlib.Path, str, None], optional_ - If specified, accepted downloads are downloaded into this directory.
  Otherwise, a temporary directory is created and is deleted when the browser is closed.
  In either case, the downloads are deleted when the browser context they were created in is closed.
- `slow_mo` _Union[float, None], optional_ - Slows down Playwright operations by the specified amount of milliseconds.
  Useful for debugging. Defaults to None.
- `traces_dir` _Union[pathlib.Path, str, None], optional_ - If specified, traces are saved into this directory.
- `chromium_sandbox` _Union[bool, None], optional_ - Enable Chromium sandboxing. Defaults to None.
- `firefox_user_prefs` _Union[Dict[str, Union[bool, float, str]], None], optional_ - Firefox user preferences.
  Learn more about the Firefox user preferences at `about:config`.

<a id="helpers.ui_functions.install_async_playwright"></a>

### install\_async\_playwright\_browser

```python
async def install_async_playwright(browser: str = 'chrome', **kwargs)
```

Method to install the Async Playwright browser.

**Arguments**:

- `browser` _str, optional_ - The browser name, possible values are 'chrome', 'firefox', or 'webkit'. Defaults to 'chrome'.
- `executable_path` _Union[pathlib.Path, str, None], optional_ - Path to a browser executable to run instead of the bundled one,
  if `executable_path` is a relative path, then it is resolved relative to the current working directory.
  Note that Playwright only works with the bundled Chromium, Firefox, or WebKit, use at your own risk.
  Defaults to None.
- `channel` _Union[str, None], optional_ - Browser distribution channel, supported values are 'chrome', 'chrome-beta',
  'chrome-dev', 'chrome-canary', 'msedge', 'msedge-beta', 'msedge-dev', 'msedge-canary'.
  Read more about using [Google Chrome and Microsoft Edge](../browsers.md#google-chrome--microsoft-edge).
  Defaults to None.
- `args` _Union[List[str], None], optional_ - Additional arguments to pass to the browser instance,
  the list of Chromium flags can be found [here](http://peter.sh/experiments/chromium-command-line-switches/).
  Defaults to None.
- `ignore_default_args` _Union[List[str], bool, None], optional_ - If True, Playwright does not pass its own configuration args
  and only uses the ones from `args`. If a list is given, it filters out the given default arguments.
  Dangerous option; use with care. Defaults to False.
- `handle_sigint` _Union[bool, None], optional_ - Close the browser process on Ctrl-C. Defaults to True.
- `handle_sigterm` _Union[bool, None], optional_ - Close the browser process on SIGTERM. Defaults to True.
- `handle_sighup` _Union[bool, None], optional_ - Close the browser process on SIGHUP. Defaults to True.
- `timeout` _Union[float, None], optional_ - Maximum time in milliseconds to wait for the browser instance to start.
  Defaults to 30000 (30 seconds). Pass 0 to disable timeout.
- `env` _Union[Dict[str, Union[bool, float, str]], None], optional_ - Specify environment variables that will be visible to the browser.
  Defaults to `process.env`.
- `headless` _Union[bool, None], optional_ - Whether to run the browser in headless mode.
  Defaults to True unless the `devtools` option is True.
- `devtools` _Union[bool, None], optional_ - **Chromium-only** Whether to auto-open a Developer Tools panel for each tab.
  If True, the `headless` option will be set to False.
  proxy (Union[
- `{'server'` - str, 'bypass': Union[str, None], 'username': Union[str, None], 'password': Union[str, None]}, None
  ], optional): Network proxy settings.
- `downloads_path` _Union[pathlib.Path, str, None], optional_ - If specified, accepted downloads are downloaded into this directory.
  Otherwise, a temporary directory is created and is deleted when the browser is closed.
  In either case, the downloads are deleted when the browser context they were created in is closed.
- `slow_mo` _Union[float, None], optional_ - Slows down Playwright operations by the specified amount of milliseconds.
  Useful for debugging. Defaults to None.
- `traces_dir` _Union[pathlib.Path, str, None], optional_ - If specified, traces are saved into this directory.
- `chromium_sandbox` _Union[bool, None], optional_ - Enable Chromium sandboxing. Defaults to None.
- `firefox_user_prefs` _Union[Dict[str, Union[bool, float, str]], None], optional_ - Firefox user preferences.
  Learn more about the Firefox user preferences at `about:config`.

<a id="services"></a>

# services

<a id="services.base_sql"></a>

# services.base\_sql

Generic BaseSql Extension

<a id="services.base_sql.BaseSql"></a>

## BaseSql Objects

```python
class BaseSql(ABC)
```

Base class for SQL operations.

<a id="services.base_sql.BaseSql.fetch_all"></a>

### fetch\_all

```python
def fetch_all(query, params=None, nb_retry=5, wait_time=5)
```

Get a list of dictionaries.

**Arguments**:

- `query` _str_ - The SQL query to execute.
- `params` _tuple, optional_ - The parameters to substitute in the query. Defaults to None.
- `nb_retry` _int, optional_ - The number of retries in case of query failure.
  Defaults to 5.
- `wait_time` _int, optional_ - The waiting time between retries in seconds. Defaults to 5.
  

**Returns**:

- `list` - A list of dictionaries representing the query result.

<a id="services.base_sql.BaseSql.fetch_one"></a>

### fetch\_one

```python
def fetch_one(query, params=None, nb_retry=5, wait_time=5)
```

Get only one dictionary.

**Arguments**:

- `query` _str_ - The SQL query to execute.
- `params` _tuple, optional_ - The parameters to substitute in the query. Defaults to None.
- `nb_retry` _int, optional_ - The number of retries in case of query failure.
  Defaults to 5.
- `wait_time` _int, optional_ - The waiting time between retries in seconds. Defaults to 5.
  

**Returns**:

- `dict` - A dictionary representing the first row of the query result.

<a id="services.base_sql.BaseSql.close"></a>

### close

```python
def close()
```

Close the database connection and cursor.

<a id="services.mssql"></a>

# services.mssql

Service MSSQL

<a id="services.mssql.ConnectionMssql"></a>

## ConnectionMssql Objects

```python
class ConnectionMssql(BaseSql)
```

A class representing a connection to a Microsoft SQL Server.

**Arguments**:

- `db_config` _dict_ - A dictionary containing the configuration details for the database connection.
  

**Attributes**:

- `connection` - A pytds.Connection object representing the connection to the database.
- `cursor` - A pytds.Cursor object representing the cursor used to execute SQL queries.
  

**Methods**:

  execute_script:
  Executes a SQL script from a file.
  

**Arguments**:

- `script_name` _str_ - The name of the script.
- `script_path` _str, optional_ - The path where the script is located. Defaults to 'resources/scripts/'.
- `params` _Union[dict, None], optional_ - The parameters to be substituted into the script. Defaults to None.
  

**Returns**:

- `int` - A return value indicating the status of the execution. (0 indicates success)
  
  execute_ps:
  Executes a stored procedure.
  

**Arguments**:

- `ps_name` _str_ - The name of the stored procedure.
- `params` _Union[list, None], optional_ - The parameters to be passed to the stored procedure. Defaults to None.
  

**Returns**:

- `any` - The result of the execution, typically the first row returned by the stored procedure.
  
  execute_query:
  Executes a SQL query.
  

**Arguments**:

- `query` _str_ - The SQL query to be executed.
- `params` _Union[tuple, None], optional_ - The parameters to be passed to the query. Defaults to None.
  

**Returns**:

- `int` - A return value indicating the status of the execution. (0 indicates success)
  

**Notes**:

  - The `db_config` dictionary should contain the necessary connection details, such as host, port, database name, username, and password.
  - The `as_dict` and `autocommit` parameters are set to True by default.
  - The `execute_script`, `execute_ps`, and `execute_query` methods execute the provided SQL script, stored procedure, and SQL query, respectively.
  - The `execute_script` method can optionally accept parameters to be substituted in the script using string formatting.
  - The `execute_ps` and `execute_query` methods can optionally accept parameters to be passed to the stored procedure or query, respectively.
  
  Usage Example:
  db_config = {
- `"host"` - "localhost",
- `"port"` - 1433,
- `"database"` - "mydatabase",
- `"user"` - "myusername",
- `"password"` - "mypassword"
  }
  
  connection = ConnectionMssql(db_config)
  connection.execute_script("myscript.sql")
  result = connection.execute_ps("mystoredprocedure", [param1, param2])
  connection.execute_query("SELECT * FROM mytable")

<a id="services.mssql.ConnectionMssql.__init__"></a>

### \_\_init\_\_

```python
def __init__(db_config)
```

Initializes a new instance of the ConnectionMssql class.

**Arguments**:

- `db_config` _dict_ - A dictionary containing the configuration details for the database connection.

<a id="services.mssql.ConnectionMssql.execute_script"></a>

### execute\_script

```python
def execute_script(script_name, script_path='resources/scripts/', params=None)
```

Executes a SQL script from a file.

**Arguments**:

- `script_name` _str_ - The name of the script.
- `script_path` _str, optional_ - The path where the script is located. Defaults to 'resources/scripts/'.
- `params` _Union[dict, None], optional_ - The parameters to be substituted into the script. Defaults to None.
  

**Returns**:

- `int` - A return value indicating the status of the execution. (0 indicates success)

<a id="services.mssql.ConnectionMssql.execute_ps"></a>

### execute\_ps

```python
def execute_ps(ps_name, params=None)
```

Executes a stored procedure.

**Arguments**:

- `ps_name` _str_ - The name of the stored procedure.
- `params` _Union[list, None], optional_ - The parameters to be passed to the stored procedure. Defaults to None.
  

**Returns**:

- `any` - The result of the execution, typically the first row returned by the stored procedure.

<a id="services.mssql.ConnectionMssql.execute_query"></a>

### execute\_query

```python
def execute_query(query, params=None)
```

Executes a SQL query.

**Arguments**:

- `query` _str_ - The SQL query to be executed.
- `params` _Union[tuple, None], optional_ - The parameters to be passed to the query. Defaults to None.
  

**Returns**:

- `int` - A return value indicating the status of the execution. (0 indicates success)

<a id="services.psql"></a>

# services.psql

Service PSQL

<a id="services.psql.ConnectionPsql"></a>

## ConnectionPsql Objects

```python
class ConnectionPsql(BaseSql)
```

ConnectionPsql class for establishing a connection and executing queries on a PostgreSQL database.

**Arguments**:

- `db_config` _dict_ - A dictionary containing the database configuration parameters.
  

**Methods**:

  __init__:
  Initializes the ConnectionPsql object.
  
  execute_query:
  Executes a query on the PostgreSQL database.

<a id="services.psql.ConnectionPsql.__init__"></a>

### \_\_init\_\_

```python
def __init__(db_config)
```

Initializes the ConnectionPsql object.

**Arguments**:

- `db_config` _dict_ - A dictionary containing the database configuration parameters.
  

**Returns**:

  None

<a id="services.psql.ConnectionPsql.execute_query"></a>

### execute\_query

```python
def execute_query(query, params=None)
```

Executes a query on the PostgreSQL database.

**Arguments**:

- `query` _str_ - The SQL query to be executed.
- `params` _tuple_ - Optional parameters to be used in the query.
  

**Returns**:

  None

<a id="services.sftp"></a>

# services.sftp

<a id="services.sftp.Sftp"></a>

## Sftp Objects

```python
class Sftp()
```

Sftp class for performing SFTP operations.

**Arguments**:

- `host` _str_ - The hostname or IP address of the remote server.
- `username` _str_ - The username to authenticate with on the remote server.
- `password` _str_ - The password to authenticate with on the remote server.
  

**Methods**:

  __init__:
  Initializes the Sftp object.
  
  upload_file:
  Uploads a local file to the specified remote path on the server.
  
  list_files:
  Lists files in the specified remote path on the server.
  
  close:
  Closes the SFTP connection.

<a id="services.sftp.Sftp.__init__"></a>

### \_\_init\_\_

```python
def __init__(host, username, password)
```

Initializes the Sftp object.

**Arguments**:

- `host` _str_ - The hostname or IP address of the remote server.
- `username` _str_ - The username to authenticate with on the remote server.
- `password` _str_ - The password to authenticate with on the remote server.

<a id="services.sftp.Sftp.upload_file"></a>

### upload\_file

```python
def upload_file(local_file, remote_path)
```

Uploads a local file to the specified remote path on the server.

**Arguments**:

- `local_file` _str_ - The path to the local file to be uploaded.
- `remote_path` _str_ - The path on the server where the file should be uploaded.

<a id="services.sftp.Sftp.list_files"></a>

### list\_files

```python
def list_files(remote_path, file)
```

Lists files in the specified remote path on the server.

**Arguments**:

- `remote_path` _str_ - The path on the server to list files from.
- `file` _str_ - The name of the file to filter the list by.
  

**Returns**:

- `list_files` _list_ - A list of file names in the remote path that match the provided file name.

<a id="services.sftp.Sftp.close"></a>

### close

```python
def close()
```

Closes the SFTP connection.

<a id="services.sso"></a>

# services.sso

Service SSO

<a id="services.sso.Sso"></a>

## Sso Objects

```python
class Sso()
```

Sso class for handling authentication and authorization using Single Sign-On (SSO).

**Arguments**:

- `server_url` _str_ - The URL of the SSO server.
- `realm_name` _str_ - The name of the realm.
- `client_id` _str_ - The client ID for authentication.
- `client_secret` _str_ - The client secret for authentication.
- `**kwargs` - Additional optional arguments.
  
  Optional Args:
  - username (str): The username for password grant.
  - password (str): The password for password grant.
  - audience (str): The audience for token exchange.
  

**Methods**:

  __init__:
  Initializes the Sso object.
  
  __initialize_access_token:
  Initializes the access token.
  
  __refresh_access_token:
  Refreshes the JWT token if necessary and returns it.
  
  jwt_token:
  Refreshes the JWT token if necessary and returns it.
  
  logout:
  Invalidates the JWT token and logs out the user.

<a id="services.sso.Sso.__init__"></a>

### \_\_init\_\_

```python
def __init__(server_url, realm_name, client_id, client_secret, **kwargs)
```

Initializes the Sso object.

**Arguments**:

- `server_url` _str_ - The URL of the SSO server.
- `realm_name` _str_ - The name of the realm.
- `client_id` _str_ - The client ID for authentication.
- `client_secret` _str_ - The client secret for authentication.
- `**kwargs` - Additional optional arguments.
  

**Returns**:

  None

**Example**:

```python
from quality_toolkit.services.sso import Sso
# Create your own resources for your application
from resources.environment.sso import sso_env

...
context.sso1 = Sso(
    sso_env.SERVER_URL,
    sso_env.REALM_NAME,
    sso_env.CLIENT_ID,
    sso_env.CLIENT_SECRET,
    audience = sso_env.AUDIENCE)
context.sso2 = Sso(
    sso_env.SERVER_URL,
    sso_env.REALM_NAME,
    sso_env.CLIENT_ID,
    sso_env.CLIENT_SECRET,
    username = sso_env.USERNAME,
    password = sso_env.USERNAME)
...
token1 = context.sso1.jwt_token()
token2 = context.sso2.jwt_token()
...
```
<a id="services.sso.Sso.jwt_token"></a>

### jwt\_token

```python
def jwt_token()
```

Refreshes the JWT token if necessary and returns it.

**Returns**:

- `str` - The JWT token.

<a id="services.sso.Sso.logout"></a>

### logout

```python
def logout()
```

Invalidates the JWT token and logs out the user.

**Returns**:

  None

