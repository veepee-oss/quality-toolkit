"""
Service SSO
"""
import datetime
import logging
from datetime import datetime, timedelta

from keycloak.realm import KeycloakRealm

logger = logging.getLogger('sso')


class Sso:
    """
    Sso class for handling authentication and authorization using Single Sign-On (SSO).

    Args:
        server_url (str): The URL of the SSO server.
        realm_name (str): The name of the realm.
        client_id (str): The client ID for authentication.
        client_secret (str): The client secret for authentication.
        **kwargs: Additional optional arguments.

    Optional Args:
        - username (str): The username for password grant.
        - password (str): The password for password grant.
        - audience (str): The audience for token exchange.

    Methods:
        __init__:
            Initializes the Sso object.

        __initialize_access_token:
            Initializes the access token.

        __refresh_access_token:
            Refreshes the JWT token if necessary and returns it.

        jwt_token:
            Refreshes the JWT token if necessary and returns it.

        logout:
            Invalidates the JWT token and logs out the user.
    """

    def __init__(self, server_url, realm_name, client_id, client_secret, **kwargs):
        """
        Initializes the Sso object.

        Args:
            server_url (str): The URL of the SSO server.
            realm_name (str): The name of the realm.
            client_id (str): The client ID for authentication.
            client_secret (str): The client secret for authentication.
            **kwargs: Additional optional arguments.

        Returns:
            None
        """
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
        """
        Initializes the access token.

        Returns:
            None
        """
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
        """
        Refreshes the JWT token if necessary and returns it.

        Returns:
            str: The JWT token.
        """
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
        Refreshes the JWT token if necessary and returns it.

        Returns:
            str: The JWT token.
        """
        if self._access_token is None:
            self.__initialize_access_token()

        if self._access_token is not None and self._access_token_expire_datetime < datetime.now():
            self.__refresh_access_token()

        return self._access_token

    def logout(self):
        """
        Invalidates the JWT token and logs out the user.

        Returns:
            None
        """
        if self._refresh_token:
            logger.info('Logout the authenticated user')
            self._open_id_connect.logout(self._refresh_token)
