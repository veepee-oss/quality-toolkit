# Services

List of services that you can use in your project

## Sso

Service to help you to get a Java Web Token and use it in your http client

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
