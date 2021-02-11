import uuid
from rest_framework import serializers
from api.models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        validated_data.pop('price')
        return Appointment.objects.create(**validated_data)

    def validate(self, data):
        if 'end_date' in data and data['start_date'] > data['end_date']:
            raise serializers.ValidationError("end_date must be after start_date")

        return data

    class Meta:
        model = Appointment
        fields = ['id', 'start_date', 'end_date', 'price', 'patient', 'physician']


class FinishAppointmentSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    end_date = serializers.DateTimeField(input_formats=["%Y-%m-%d %H:%M:%S"])

    class Meta:
        model = Appointment
        fields = ['id', 'end_date']
