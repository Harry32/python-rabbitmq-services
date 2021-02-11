import pika
import json
from servico_consulta.settings import SERVICO_FINANCEIRO


class Financeiro:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit-mq'))
        self.channel = self.connection.channel()

        self.channel.queue_declare(queue='charge')

    def ChargeAppointment(self, appointment_id, value):

        objeto = {
            "appointment_id": appointment_id,
            "value": value
        }

        self.channel.basic_publish(exchange='', routing_key='charge', body=json.dumps(objeto))

        self.connection.close()
