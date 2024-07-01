from api_client import fetch_match_data
from kafka_producer import send_to_kafka

def main():
    # Fetch data from the API
    data = fetch_match_data()

    # Send data to Kafka
    if data:
        send_to_kafka(data)
    else:
        print("No data fetched")

if __name__ == "__main__":
    main()
