"""
All methods link to APIs
"""
import logging
import time

import requests


def send_api_request(method, url, status_code=None, nb_retry=5, wait_time=10, timeout=60, **kwargs):
    """
    Constructs and sends a Request object.

    Args:
        method (str): Method for the new Request object: 'GET', 'OPTIONS', 'HEAD', 'POST', 'PUT', 'PATCH', or 'DELETE'.
        url (str): URL for the new Request object.
        status_code (List[int]): List to get the expected status code.
        nb_retry (int): Integer to set the number of possible retries.
        wait_time (int, optional): Integer to set the waiting time between each try.
        params (dict, optional): Dictionary, list of tuples or bytes to send in the query string for the Request.
        data (dict, optional): Dictionary, list of tuples, bytes, or file-like object to send in the body of the Request.
        json (optional): A JSON serializable Python object to send in the body of the Request.
        headers (dict, optional): Dictionary of HTTP Headers to send with the Request.
        cookies (optional): Dict or CookieJar object to send with the Request.
        files (dict, optional): Dictionary of 'name': file-like-objects (or {'name': file-tuple'}) for multipart encoding upload.
            'file-tuple' can be a 2-tuple ('filename', fileobj'), 3-tuple ('filename', fileobj', 'content_type')'
            or a 4-tuple ('filename', fileobj', 'content_type', custom_headers'), where 'content-type' is a string
            defining the content type of the given file and 'custom_headers' a dict-like object containing additional headers
            to add for the file.
        auth (optional): Auth tuple to enable Basic/Digest/Custom HTTP Auth.
        timeout (float or tuple, optional): How many seconds to wait for the server to send data before giving up, as a float, or a (connect timeout,
            read timeout) tuple.
        allow_redirects (bool, optional): Boolean. Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection. Defaults to True.
        proxies (optional): Dictionary mapping protocol to the URL of the proxy.
        verify (optional): Either a boolean, in which case it controls whether we verify the server's TLS certificate, or a string, in which
            case it must be a path to a CA bundle to use. Defaults to True.
        stream (optional): If False, the response content will be immediately downloaded.
        cert (optional): If String, path to SSL client cert file (.pem). If Tuple, ('cert', 'key') pair.

    Returns:
        Response: Response object.
    """
    if status_code is None:
        status_code = [200, 201, 202, 204]
    retry = 0
    while True:
        response = requests.request(method, url, timeout=timeout, **kwargs)
        if response.status_code in status_code:
            return response
        if retry < nb_retry != 0:
            logging.info(f"Request Retry {retry + 1}/{nb_retry} - {response.status_code} - {response.content.decode('UTF-8')}")
            time.sleep(wait_time)
            retry += 1
        else:
            return response
