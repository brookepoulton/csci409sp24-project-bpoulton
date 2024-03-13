from rest_framework import serializers
from .models import Vessel, VesselSchedule, BillOfLading, Container

class VesselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vessel
        fields = '__all__'
        read_only_fields = ['id']

class VesselScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VesselSchedule
        fields = '__all__'
        read_only_fields = ['id']

class BillOfLadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillOfLading
        fields = '__all__'
        read_only_fields = ['id']

class ContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Container
        fields = '__all__'
        read_only_fields = ['id']
