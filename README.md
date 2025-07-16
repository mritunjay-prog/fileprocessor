# Kafka Consumer to MongoDB

## Description
This application consumes JSON messages from a Kafka topic (`json-topic`) and stores each message as a new document in a MongoDB collection (`pitchsta`) within the `pitchstat` database.

## Features
- Listens to Kafka messages in real-time.
- Automatically deserializes JSON messages.
- Inserts each JSON message as a new document into MongoDB.

## Prerequisites
- **Kafka**: A running Kafka broker on `localhost:9092`.
- **MongoDB**: A running MongoDB instance on `localhost:27017`.
- **Python**: Python 3.10 or higher.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd fileprocessor