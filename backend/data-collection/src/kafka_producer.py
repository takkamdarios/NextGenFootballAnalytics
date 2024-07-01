from kafka import KafkaProducer
import json

# Kafka configuration
KAFKA_TOPIC = 'football_data'
KAFKA_SERVER = 'localhost:9092'

producer = KafkaProducer(bootstrap_servers=[KAFKA_SERVER],
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

def send_to_kafka(data):
    try:
        producer.send(KAFKA_TOPIC, value=data)
        producer.flush()
        print(f"Data sent to Kafka topic {KAFKA_TOPIC}")
    except Exception as e:
        print(f"Failed to send data to Kafka: {e}")
