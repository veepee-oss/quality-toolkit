"""
All methods link to the local environment
"""
from datetime import datetime
from pathlib import Path

import pytz


def find_resource(name: str, filepath='resources/'):
    """
    Help to find a resource in a project
    :param str name: Name of the resource
    :param str filepath: Default file path of the resource
    :return: The path of the resource
    :raises Exception: if the resource is not found
    """
    for path in Path(filepath).rglob('*.*'):
        if path.name.__contains__(name):
            return path
    raise Exception("File not found")


def get_timezone_paris(timezone='Europe/Paris'):
    """
    In docker the time zone is in UTC-0, but in some database the dates are in UTC+2
    So for request by date you need to get datetime.now() + 2
    """
    tz = pytz.timezone(timezone)
    return datetime.now(tz)


def expected_value_test(context, value: str):
    """
    Check if the context contain the expected value
    :param str context: The context
    :param str value: The expected value to find
    """
    if str(value).__contains__('context'):
        split_value = value.split('.')
        expected_value = context.__getattr__(split_value[1])
        if len(split_value) > 2:
            for i in range(2, len(split_value)):
                expected_value = expected_value[split_value[i] if not split_value[i].isnumeric() else int(split_value[i])]
        return expected_value
    if str(value) == '0<' or str(value).__contains__('>'):
        return ""
    else:
        return value


def response_message(message, response, password=False, truncate_content=0, truncate_body=0):
    """
    Show the response with all information to have a better debug
    :param str message: A message to explain the request or the error
    :param requests.Response response: the request response
    :param bool password: if the header contain a secure data it will not show, by default it's false
    :param integer truncate_content: truncate content to the defined size, 0 to deactivate, by default 0
    :param integer truncate_body: truncate body to the defined size, 0 to deactivate, by default 0
    """
    header = "the header contain a secure data, it can't to be showed"
    body = "No body"
    if not password:
        header = f"{response.request.headers}"
    if response.request.body is not None:
        body = response.request.body.decode('utf-8')
        if truncate_body != 0:
            body = response.request.body.decode('utf-8')[0:truncate_body]
    content = response.content.decode('utf-8')
    if truncate_content != 0:
        content = response.content.decode('utf-8')[0:truncate_content]
    return f"{message},\n\t" \
           f"- code: {response.status_code}\n\t" \
           f"- content: {content}\n\t" \
           f"- method: {response.request.method}\n\t" \
           f"- url: {response.request.url}\n\t" \
           f"- header: {header}\n\t" \
           f"- body: {body}"
