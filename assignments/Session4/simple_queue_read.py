# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 14:11:37 2017

@author: cavasinf
"""

# consume.py
import pika, os, argparse


parser = argparse.ArgumentParser(description='Adding an option to persist the messages')
parser.add_argument('-concurrency', action='store_true', help='persist the messages')

arg = parser.parse_args().concurrency

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
amqp_url='amqp://vqpdfink:e0NW4iPm3cS67fVS9rpxIUCA7C-GUIvL@lark.rmq.cloudamqp.com/vqpdfink'
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5

counter = 0

#initiate the connexion
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='presentation')

def callback(ch, method, properties, body):
	global counter
	counter += 1
	print(" [X] Received " + str(body))
	print("You received " + str(counter) + " message(s)")
	if arg:
		ch.basic_ack(delivery_tag = method.delivery_tag)

if arg:
	channel.basic_qos(prefetch_count=1)

channel.basic_consume(callback,
	queue='presentation',
	no_ack=not arg)

print(" [*] Waiting or messages.")

channel.start_consuming()