from rest_framework import serializers
from api.models import Charge


class ChargeSerializer(serializers.ModelSerializer):

    appointment_id = serializers.UUIDField(source="appointment")

    def create(self, validated_data):
        return Charge.objects.create(**validated_data)

    class Meta:
        model = Charge
        fields = ['id', 'value', 'appointment_id']
