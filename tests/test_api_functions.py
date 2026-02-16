"""
Unit tests for API functions
"""
import unittest
from unittest.mock import patch, Mock

from quality_toolkit.helpers.api_functions import send_api_request


class TestApiFunctions(unittest.TestCase):
    """Tests for API functions"""

    @patch('quality_toolkit.helpers.api_functions.requests.request')
    def test_send_api_request_success(self, mock_request):
        """Test successful API request"""
        # Mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = b'{"success": true}'
        mock_request.return_value = mock_response

        response = send_api_request('GET', 'https://api.example.com/data')

        self.assertEqual(response.status_code, 200)
        mock_request.assert_called_once()
        print("✅ Successful API request test passed")

    @patch('quality_toolkit.helpers.api_functions.requests.request')
    def test_send_api_request_with_params(self, mock_request):
        """Test API request with parameters"""
        mock_response = Mock()
        mock_response.status_code = 201
        mock_request.return_value = mock_response

        response = send_api_request(
            'POST',
            'https://api.example.com/data',
            status_code=[201],
            json={'key': 'value'},
            headers={'Authorization': 'Bearer token'}
        )

        self.assertEqual(response.status_code, 201)
        call_kwargs = mock_request.call_args[1]
        self.assertEqual(call_kwargs['json'], {'key': 'value'})
        self.assertIn('Authorization', call_kwargs['headers'])
        print("✅ API request with parameters test passed")

    @patch('quality_toolkit.helpers.api_functions.requests.request')
    @patch('quality_toolkit.helpers.api_functions.time.sleep')
    def test_send_api_request_retry(self, mock_sleep, mock_request):
        """Test retry mechanism"""
        # First call fails, second succeeds
        mock_response_fail = Mock()
        mock_response_fail.status_code = 500
        mock_response_fail.content = b'error'

        mock_response_success = Mock()
        mock_response_success.status_code = 200

        mock_request.side_effect = [mock_response_fail, mock_response_success]

        response = send_api_request(
            'GET',
            'https://api.example.com/data',
            nb_retry=5,
            wait_time=1
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(mock_request.call_count, 2)
        mock_sleep.assert_called_once_with(1)
        print("✅ Retry mechanism test passed")

    @patch('quality_toolkit.helpers.api_functions.requests.request')
    def test_send_api_request_custom_status_codes(self, mock_request):
        """Test with custom status codes"""
        mock_response = Mock()
        mock_response.status_code = 404
        mock_request.return_value = mock_response

        response = send_api_request(
            'GET',
            'https://api.example.com/data',
            status_code=[404],
            nb_retry=0
        )

        self.assertEqual(response.status_code, 404)
        print("✅ Custom status codes test passed")


if __name__ == '__main__':
    unittest.main(verbosity=2)

