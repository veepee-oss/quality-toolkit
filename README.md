# Quality-Toolkit

Toolkit for the quality in order to help writing tests

## Contribution

Clone the project

```bash
git clone git@git.vptech.eu:veepee/vptech/qa/quality-toolkit.git quality-toolkit
cd quality-toolkit
```

## Installation in local

make install

## Installation in a project

Edit the project's requirements.txt and add the line :

```txt
quality-toolkit
```

and finish by install the project dependencies :

```bash
pip3 install
```

## How to use the classes ?

### Helpers

This library share functions that help to build a steps

example :

```python
from quality_toolkit.helpers.api_functions import send_api_request
from resources.environment import urls

...
context.response = send_api_request("GET", urls.MY_API_URL, [200])
...
```

### Services

This library share services that give customize clients

```python
from quality_toolkit.services.sso import Sso
# Create your own resources for your application
from resources.environment.sso import sso_constant

...
context.sso1 = Sso(sso_constant.SERVER_URL, sso_constant.REALM_NAME, sso_constant.CLIENT_ID, sso_constant.CLIENT_SECRET, sso_constant.AUDIENCE)
context.sso2 = Sso(sso_constant.SERVER_URL, sso_constant.REALM_NAME, sso_constant.CLIENT_ID, sso_constant.CLIENT_SECRET, sso_constant.AUDIENCE)
...
token1 = context.sso1.jwt_token()
token2 = context.sso2.jwt_token()
...
```
