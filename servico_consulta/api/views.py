import datetime
import pytz
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Appointment
from api.serializers import AppointmentSerializer, FinishAppointmentSerializer
from api.rpc_client import Financeiro


class AppointmentView(APIView):

    def get(self, request):
        appointment_list = Appointment.objects.all()

        serializer = AppointmentSerializer(appointment_list, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        serializer = FinishAppointmentSerializer(data=request.data)

        if serializer.is_valid():
            appoitment = Appointment.objects.get(pk=serializer.data['id'])

            end_date = pytz.UTC.localize(datetime.datetime.strptime(serializer.data['end_date'], "%Y-%m-%dT%H:%M:%SZ"))

            if appoitment.end_date:
                return Response("Appointment already finished.", status=status.HTTP_400_BAD_REQUEST)
            elif appoitment.start_date > end_date:
                return Response("end_date must be after start_date", status=status.HTTP_400_BAD_REQUEST)

            appoitment.end_date = end_date

            minutos = (appoitment.end_date - appoitment.start_date).total_seconds() / 60

            valor = 200 * int(minutos/60)

            if minutos%60 > 0:
                valor += 200

            appoitment.save()

            financeiro = Financeiro()

            financeiro.ChargeAppointment(serializer.data['id'], valor)

            return Response(None, status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
