from rest_framework import serializers
from .models import SystemLogModel


class SystemLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemLogModel
        fields = ['time', 'date', 'device', 'log']