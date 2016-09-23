#!/usr/bin/env python
try:
    import pika
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
channel = connection.channel()
