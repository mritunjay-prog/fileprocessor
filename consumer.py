from kafka import KafkaConsumer
from pymongo import MongoClient
import json

# Setup MongoDB
mongo_client = MongoClient("mongodb://root:example@localhost:27017/")
db = mongo_client["pitchstat"]
collection = db["pitchsta"]  # Changed collection to 'pitchstat'

# Kafka consumer
consumer = KafkaConsumer(
    'json-topic',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

print("Listening to Kafka...")

for message in consumer:
    data = message.value
    print(f"Received: {data}")
    
    # Check if the data is a dictionary
    if isinstance(data, dict):
        try:
            # Insert the dictionary as a new document into the collection
            collection.insert_one(data)
            print("Stored JSON document in MongoDB.")
        except Exception as e:
            print(f"Error storing data in MongoDB: {e}")
    else:
        print("Invalid data format. Expected a dictionary.")