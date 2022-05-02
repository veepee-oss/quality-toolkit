"""
All methods link to APIs
"""
import logging
import time

import requests


def send_api_request(method, url, status_code=None, nb_retry=5, wait_time=10, **kwargs):
    """Constructs and sends a :class:`Request <Request>`.
        :param method: method for the new :class:`Request` object: ``GET``, ``OPTIONS``, ``HEAD``, ``POST``, ``PUT``, ``PATCH``, or ``DELETE``.
        :param url: URL for the new :class:`Request` object.
        :param status_code: List, list to get the expected status code
        :param nb_retry: Integer, set the number of possible retry
        :param wait_time: (optional) Integer, set the waiting time between each try
        :param params: (optional) Dictionary, list of tuples or bytes to send in the query string for the :class:`Request`.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like object to send in the body of the :class:`Request`.
        :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
        :param headers: (optional) Dictionary of HTTP Headers to send with the :class:`Request`.
        :param cookies: (optional) Dict or CookieJar object to send with the :class:`Request`.
        :param files: (optional) Dictionary of ``'name': file-like-objects`` (or ``{'name': file-tuple}``) for multipart encoding upload.
            ``file-tuple`` can be a 2-tuple ``('filename', fileobj)``, 3-tuple ``('filename', fileobj, 'content_type')``
            or a 4-tuple ``('filename', fileobj, 'content_type', custom_headers)``, where ``'content-type'`` is a string
            defining the content type of the given file and ``custom_headers`` a dict-like object containing additional headers
            to add for the file.
        :param auth: (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.
        :param timeout: (optional) How many seconds to wait for the server to send data before giving up, as a float, or a :ref:`(connect timeout,
            read timeout) <timeouts>` tuple.
        :type timeout: float or tuple :param allow_redirects: (optional) Boolean. Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection.
            Defaults to ``True``.
        :type allow_redirects: bool
        :param proxies: (optional) Dictionary mapping protocol to the URL of the proxy.
        :param verify: (optional) Either a boolean, in which case it controls whether we verify the server's TLS certificate, or a string, in which
            case it must be a path to a CA bundle to use. Defaults to ``True``.
        :param stream: (optional) if ``False``, the response content will be immediately downloaded.
        :param cert: (optional) if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
    """
    if status_code is None:
        status_code = [200, 201, 202, 204]
    retry = 0
    while True:
        response = requests.request(method, url, **kwargs)
        if response.status_code in status_code:
            return response
        if retry < nb_retry != 0:
            logging.info(f"Request Retry {retry + 1}/{nb_retry} - {response.status_code} - {response.content.decode('UTF-8')}")
            time.sleep(wait_time)
            retry += 1
        else:
            return response
