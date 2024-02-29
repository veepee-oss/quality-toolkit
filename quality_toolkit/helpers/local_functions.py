"""
All methods link to the local environment
"""
from datetime import datetime
from pathlib import Path

import pkgutil
import pytz
import requests


def compare_values(symbol, arg1, arg2) -> bool:
    """ Compare two values for equality. Return a Syntax Error if the symbol is not found.

    Args:
        symbol (str): Symbol to use for comparison ('==', '<', '<=', '>=', '>').
        arg1 (Any): First value to compare.
        arg2 (Any): Second value to compare.

    Returns:
        bool: True if the comparison is successful, False otherwise.

    Raises:
        SyntaxError: If the symbol variable in the argument is not found.
    """
    arg1 = int(arg1)
    arg2 = int(arg2)
    if symbol == "==":
        return arg1 == arg2
    elif symbol == "<":
        return arg1 < arg2
    elif symbol == "<=":
        return arg1 <= arg2
    elif symbol == ">=":
        return arg1 >= arg2
    elif symbol == ">":
        return arg1 > arg2
    raise SyntaxError('Symbol variable in argument not found')


def find_resource(name: str, filepath: str = 'resources/') -> Path:
    """ Help to find a resource in a project.

    Args:
        name (str): Name of the resource.
        filepath (str, optional): Default file path of the resource.

    Returns:
        Path: The path of the resource.

    Raises:
        FileNotFoundError: If the resource is not found.
    """
    for path in Path(filepath).rglob('*.*'):
        if name in path.name:
            return path
    raise FileNotFoundError("File not found")


def import_recurcively_modules(path_file: str) -> None:
    """ Import all modules in a package.

    Args:
        path_file (str): Path of the file/module.

    Returns:
        None
    """
    __all__ = []
    path = [path_file]
    for loader, module_name, _ in pkgutil.walk_packages(path):
        __all__.append(module_name)
        _module = loader.find_module(module_name).load_module(module_name)
        globals()[module_name] = _module


def get_timezone_paris(timezone: str = 'Europe/Paris') -> datetime:
    """ Get the current datetime in the Paris timezone.

    Args:
        timezone (str, optional): Timezone to use.

    Returns:
        datetime: Current datetime in the specified timezone.
    """
    tz = pytz.timezone(timezone)
    return datetime.now(tz)


def response_message(message: str, response: requests.Response, password: bool = False, truncate_content: int = 0, truncate_body: int = 0) -> str:
    """ Show the response with all information to have a better debug.

    Args:
        message (str): A message to explain the request or the error.
        response (requests.Response): The request response.
        password (bool, optional): If the header contains secure data, it will not be shown. Defaults to False.
        truncate_content (int, optional): Truncate content to the defined size, -1 to deactivate, 0 to show all content. Defaults to 0.
        truncate_body (int, optional): Truncate body to the defined size, -1 to deactivate, 0 to deactivate. Defaults to 0.

    Returns:
        str: The formatted response message.
"""
    header = "the header contain a secure data, it can't to be showed"
    body = "No body"
    if not password:
        header = f"{response.request.headers}"
    if response.request.body is not None:
        body = response.request.body.decode(
            'utf-8') if isinstance(response.request.body, (bytes, bytearray)) else response.request.body
        if truncate_body != -1:
            if truncate_body != 0:
                body = body[0:truncate_body]
        else:
            body = "Don't want to show the body."
    content = response.content.decode(
        'utf-8') if isinstance(response.content, (bytes, bytearray)) else response.content
    if truncate_content != -1:
        if truncate_content != 0:
            content = content[0:truncate_content]
    else:
        content = "Don't want to show the content."
    return f"{message},\n\t" \
           f"- code: {response.status_code}\n\t" \
           f"- content: {content}\n\t" \
           f"- method: {response.request.method}\n\t" \
           f"- url: {response.request.url}\n\t" \
           f"- header: {header}\n\t" \
           f"- body: {body}"
