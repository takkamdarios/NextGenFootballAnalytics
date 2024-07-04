import unittest
from unittest.mock import patch
from kafka_producer import send_to_kafka

class TestKafkaProducer(unittest.TestCase):

    @patch('kafka_producer.KafkaProducer')
    def test_send_to_kafka(self, mock_kafka_producer):
        # Mock the Kafka producer and its send and flush methods.
        mock_send = mock_kafka_producer.return_value.send
        mock_flush = mock_kafka_producer.return_value.flush

        send_to_kafka('football_data', {'test': 'data'})

        # Assert send was called once
        mock_send.assert_called_once_with('football_data', value={'test': 'data'})
        # Assert flush was called once to ensure the data is sent
        mock_flush.assert_called_once()

if __name__ == '__main__':
    unittest.main()
