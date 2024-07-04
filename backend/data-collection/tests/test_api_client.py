import unittest
from unittest.mock import patch
from api_client import fetch_data_from_source, fetch_all_data

class TestAPIClient(unittest.TestCase):

    @patch('api_client.requests.get')
    def test_fetch_data_from_source_success(self, mock_get):
        # Configure the mock to return a response with an OK status code.
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'data': 'success'}

        data = fetch_data_from_source('FIFA22Dataset')
        self.assertIsNotNone(data)
        self.assertEqual(data, {'data': 'success'})

    @patch('api_client.requests.get')
    def test_fetch_data_from_source_failure(self, mock_get):
        # Configure the mock to simulate a failed API call.
        mock_get.return_value.status_code = 404

        data = fetch_data_from_source('NonexistentSource')
        self.assertIsNone(data)

    @patch('api_client.fetch_data_from_source')
    def test_fetch_all_data(self, mock_fetch_data):
        # Setup the mock to return different data for each source.
        mock_fetch_data.side_effect = [
            {'data': 'data1'},  # Return value for the first call
            {'data': 'data2'}   # Return value for the second call
        ]

        all_data = fetch_all_data()
        self.assertEqual(len(all_data), 2)
        self.assertDictEqual(all_data, {
            'FIFA22Dataset': {'data': 'data1'},
            'FootballMatchEvents': {'data': 'data2'}
        })

if __name__ == '__main__':
    unittest.main()
