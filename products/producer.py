import pika, json

params = pika.URLParameters('amqps://rivzikvh:h0y_hrsQfHsxJ9zXk3k5egVuCDGqv4eI@clam.rmq.cloudamqp.com/rivzikvh')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)