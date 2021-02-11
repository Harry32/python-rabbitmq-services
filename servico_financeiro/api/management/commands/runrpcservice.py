import pika
import time
import importlib

from contextlib import contextmanager
from django.core.management.base import BaseCommand, CommandError
from concurrent import futures
from django.utils import autoreload
from django.conf import settings

from api.services import ChargeAppointment

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


@contextmanager
def serve_forever():
    try:
        time.sleep(5)
        params = pika.ConnectionParameters('rabbit-mq')
        connection = pika.BlockingConnection(params)

        channel = connection.channel()

        channel.queue_declare(queue='charge')

        channel.basic_consume(queue='charge',
                              auto_ack=True,
                              on_message_callback=ChargeAppointment)

        channel.start_consuming()
    except Exception as e:
        print(e)


class Command(BaseCommand):
    help = 'Comando para inicializar o serviço GRPC'

    def add_arguments(self, parser):
        parser.add_argument('-a', '--autoreload', action='store_true', help='Habilita autoreload')

    def inner_handle(self, **kwargs):
        with serve_forever():
            self.stdout.write(self.style.SUCCESS(f'RPC server inicializado com sucesso'))

    def handle(self, *args, **options):
        if options['autoreload']:
            autoreload.run_with_reloader(self.inner_handle, **options)
        else:
            self.inner_handle(**options)
