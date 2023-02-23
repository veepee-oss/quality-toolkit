"""
All methods link to the local environment
"""
from datetime import datetime
from pathlib import Path

import pkgutil
import pytz


def compare_values(symbol, arg1, arg2):
    """Compare two values for equality. Return a Syntax Error if the symbol is not found"""
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


def find_resource(name: str, filepath='resources/'):
    """
    Help to find a resource in a project
    :param str name: Name of the resource
    :param str filepath: Default file path of the resource
    :return: The path of the resource
    :raises FileNotFoundError: if the resource is not found
    """
    for path in Path(filepath).rglob('*.*'):
        if name in path.name:
            return path
    raise FileNotFoundError("File not found")


def import_recurcively_modules(path_file):
    """
    Import all modules in a package
    >>> import_recurcively_modules(os.path.dirname(__file__))
    """
    __all__ = []
    path = [path_file]
    for loader, module_name, _ in pkgutil.walk_packages(path):
        __all__.append(module_name)
        _module = loader.find_module(module_name).load_module(module_name)
        globals()[module_name] = _module


def get_timezone_paris(timezone='Europe/Paris'):
    """
    In docker the time zone is in UTC-0, but in some database the dates are in UTC+2
    So for request by date you need to get datetime.now() + 2
    """
    tz = pytz.timezone(timezone)
    return datetime.now(tz)


def response_message(message, response, password=False, truncate_content=0, truncate_body=0):
    """
    Show the response with all information to have a better debug
    :param str message: A message to explain the request or the error
    :param requests.Response response: the request response
    :param bool password: if the header contain a secure data it will not show, by default it's false
    :param integer truncate_content: truncate content to the defined size, -1 to deactivate, 0 to show all content, by default 0
    :param integer truncate_body: truncate body to the defined size, -1 to deactivate, 0 to deactivate, by default 0
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
