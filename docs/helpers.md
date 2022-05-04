# Helpers

List of helpers that you can use in your project

## send_api_request(method, url, status_code=None, nb_retry=5, wait_time=10, **kwargs)

Helper that send an http request to an API. This helper test the result of the response automaticaly.
If the response http code is not in [200, 201, 202, 204], the helper retry the call N times.

```python
from quality_toolkit.helpers.api_functions import send_api_request
from resources.environment import urls

...
context.response = send_api_request("GET", urls.MY_API_URL)
...
```

## find_resource(name: str, filepath='resources/')

Helper to find a resource in a project.

```python
from quality_toolkit.helpers.local_functions import find_resource

...
with open(str(find_resource(file, f"{context.config.userdata['dataset']}/{resource}")), 'r', encoding="UTF-8") as dataset_file:
        dataset = json.load(dataset_file)
...
```

## response_message(message, response, password=False, truncate_content=0, truncate_body=0)

Helper to transform an HTTP response into a string in order to display or log the information

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
