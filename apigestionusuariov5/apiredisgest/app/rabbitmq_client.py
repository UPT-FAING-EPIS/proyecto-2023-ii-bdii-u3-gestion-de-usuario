
import pika
import json
from datetime import datetime
import time

class RabbitMQClient:
    def __init__(self, config):
        self.config = config
        self.connect()

    def connect(self):
        credentials = pika.PlainCredentials(self.config['username'], self.config['password'])
        connection_params = pika.ConnectionParameters(
            host=self.config['host'],
            port=self.config['port'],
            credentials=credentials,
            heartbeat=self.config['heartbeat'],
            blocked_connection_timeout=300
        )
        self.connection = pika.BlockingConnection(connection_params)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.config['queue_name'], durable=True)

    def publish_event(self, event_type, event_details):
        if self.connection is None or self.channel is None or not self.channel.is_open:
            self.connect()
        message = {
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'event': event_type,
            'text': event_details
        }
        try:
            self.channel.basic_publish(
                exchange='',
                routing_key=self.config['queue_name'],
                body=json.dumps(message),
                properties=pika.BasicProperties(delivery_mode=2)
            )
        except pika.exceptions.AMQPConnectionError as e:
            print("Connection to RabbitMQ lost. Trying to reconnect...")
            self.connect()
            self.publish_event(event_type, event_details)  
        except pika.exceptions.ChannelClosedByBroker as e:
            print("Channel closed by broker, trying to reopen...")
            self.connect()
            self.publish_event(event_type, event_details)  
        except pika.exceptions.StreamLostError as e:
            print("Stream lost, trying to reconnect...")
            self.connect()
            self.publish_event(event_type, event_details)  
        except Exception as e:
            print(f"Unhandled exception: {e}")
            raise

    def close_connection(self):
        if self.connection:
            self.connection.close()
            self.connection = None
            self.channel = None
