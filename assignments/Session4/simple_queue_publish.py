# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 14:08:57 2017

@author: cavasinf
"""

# publish.py
import pika, os, argparse

parser = argparse.ArgumentParser(description='Option pour persist les messages')
parser.add_argument('-concurrency', action='store_true', help='persist the messages')
parser.add_argument('-n', type=int, default=1, help='number of messages to be pusblished')

arg = parser.parse_args().concurrency

property = None

if arg:
	property = pika.BasicProperties(delivery_mode = 2)

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
amqp_url='amqp://vqpdfink:e0NW4iPm3cS67fVS9rpxIUCA7C-GUIvL@lark.rmq.cloudamqp.com/vqpdfink'
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
#set timeout
params.socket_timeout = 5

connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='presentation')


message = "BANANA Florian"

for i in range(parser.parse_args().n):
	channel.basic_publish(exchange='',
		routing_key='presentation',
		body=message,
		properties=property)

print(" [X] Username sent! " + str(parser.parse_args().n) + " messages sent.")

connection.close()