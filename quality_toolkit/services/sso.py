"""
Service SSO
"""
import datetime
import logging
from datetime import datetime, timedelta

from keycloak.realm import KeycloakRealm

logger = logging.getLogger('sso')


class Sso:
    def __init__(self, server_url, realm_name, client_id, client_secret, **kwargs):
        self._realm = KeycloakRealm(
            server_url,
            realm_name,
        )
        self._open_id_connect = self._realm.open_id_connect(
            client_id,
            client_secret,
        )

        self._username = kwargs.get('username', None)
        self._password = kwargs.get('password', None)
        self._audience = kwargs.get('audience', None)

        self._access_token = None
        self._access_token_expire_datetime = None
        self._refresh_token = None

    def __initialize_access_token(self):
        if self._username is not None:
            logger.info('Get access token: grant by password')
            access_token_payload = self._open_id_connect.password_credentials(
                username=self._username,
                password=self._password,
            )
            self._access_token = access_token_payload['access_token']
            self._refresh_token = access_token_payload['refresh_token']
            self._access_token_expire_datetime = datetime.now(
            ) + timedelta(seconds=access_token_payload['expires_in'])
        else:
            logger.info('Get access token: grant by client_credentials')
            client_credentials_payload = self._open_id_connect.client_credentials()
            self._access_token = client_credentials_payload['access_token']
            self._access_token_expire_datetime = datetime.now(
            ) + timedelta(seconds=client_credentials_payload['expires_in'])

            if self._audience is not None:
                logger.info('Get access token: grant by token-exchange')
                token_exchange_payload = self._open_id_connect.token_exchange(
                    subject_token=self._access_token,
                    audience=self._audience,
                )
                self._access_token = token_exchange_payload['access_token']
                self._access_token_expire_datetime = datetime.now(
                ) + timedelta(seconds=token_exchange_payload['expires_in'])

    def __refresh_access_token(self):
        if self._username is not None:
            logger.info('Refresh the access token: grant by refresh_token')
            refresh_access_token_payload = self._open_id_connect.refresh_token(
                refresh_token=self._refresh_token)
            self._access_token = refresh_access_token_payload['access_token']
            self._refresh_token = refresh_access_token_payload['refresh_token']
            self._access_token_expire_datetime = datetime.now(
            ) + timedelta(seconds=refresh_access_token_payload['expires_in'])
        else:
            self.__initialize_access_token()

    def jwt_token(self):
        """
        Refresh jwt token if necessary and return it
        """
        if self._access_token is None:
            self.__initialize_access_token()

        if self._access_token is not None and self._access_token_expire_datetime < datetime.now():
            self.__refresh_access_token()

        return self._access_token

    def logout(self):
        """
        Unvalid the jwt token and logout the user
        """
        if self._refresh_token:
            logger.info('Logout the authenticated user')
            self._open_id_connect.logout(self._refresh_token)
