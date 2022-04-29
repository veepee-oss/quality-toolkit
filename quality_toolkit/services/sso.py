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
        self._jwt_token = None
        self._jwt_token_expire_datetime = None

    def __init_access_token(self):
        logger.info('Init the access token')

        payload_access_token = self._open_id_connect.client_credentials()

        self._access_token = payload_access_token['access_token']
        self._refresh_token = payload_access_token['refresh_token']
        self._access_token_expire_datetime = datetime.now(
        ) + timedelta(seconds=payload_access_token['expires_in'])

    def __refresh_access_token(self):
        logger.info('Refresh the access token')

        payload_refresh_access_token = self._open_id_connect.refresh_token(
            refresh_token=self._refresh_token)

        self._access_token = payload_refresh_access_token['access_token']
        self._refresh_token = payload_refresh_access_token['refresh_token']
        self._access_token_expire_datetime = datetime.now(
        ) + timedelta(seconds=payload_refresh_access_token['expires_in'])

    def __refresh_jwt_token(self):
        logger.info('Refresh the jwt token')

        payload_jwt_token = None

        if self._username is not None:
            payload_jwt_token = self._open_id_connect.password_credentials(
                username=self._username,
                password=self._password,
            )

        if payload_jwt_token is None:
            payload_jwt_token = self._open_id_connect.token_exchange(
                subject_token=self._access_token,
                audience=self._audience,
            )

        self._jwt_token = payload_jwt_token['access_token']
        self._jwt_token_expire_datetime = datetime.now(
        ) + timedelta(seconds=payload_jwt_token['expires_in'])

    def jwt_token(self):
        """
        Refresh jwt token if necessary and return it
        """
        if self._access_token is None:
            self.__init_access_token()

        if self._access_token is not None and self._access_token_expire_datetime < datetime.now():
            self.__refresh_access_token()

        if self._jwt_token is None:
            self.__refresh_jwt_token()

        if self._jwt_token is not None and self._jwt_token_expire_datetime < datetime.now():
            self.__refresh_jwt_token()

        return self._jwt_token

    def logout(self):
        """
        Unvalid the jwt token and logout the user
        """
        if self._refresh_token:
            logger.info('Logout the authenticated user')
            self._open_id_connect.logout(self._refresh_token)
