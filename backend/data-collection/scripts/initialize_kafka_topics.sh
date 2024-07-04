#!/bin/bash
# scripts/initialize_kafka_topics.sh

# List of topics to create
topics=("football_data" "player_performance" "match_events")

# Kafka server address
kafka_server="localhost:9092"

# Create each topic
for topic in ${topics[@]}; do
  echo "Creating Kafka topic: $topic"
  kafka-topics --create --if-not-exists --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic $topic
done

echo "All topics created successfully."
