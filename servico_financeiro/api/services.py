import json

from api.serializers import ChargeSerializer


def ChargeAppointment(ch, method, properties, body):
    dados = json.loads(body.decode("utf-8"))

    serializer = ChargeSerializer(data=dados)

    if serializer.is_valid():
        serializer.save()
