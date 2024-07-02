from api_client import fetch_all_data
from kafka_producer import send_to_kafka

def main():
    # Fetch data from all configured APIs
    all_data = fetch_all_data()

    # Send each data set to Kafka, categorized by source
    for source, data in all_data.items():
        if data:
            print(f"Sending data from {source} to Kafka.")
            send_to_kafka(source, data)
        else:
            print(f"No data fetched from {source}, nothing to send.")

if __name__ == "__main__":
    main()
