from rest_framework import serializers
from webKomber.models import UserData
# from geojson_serializer.serializers import geojson_serializer

# @geojson_serializer('locations', id='id')
class UserdataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserData
        fields = [
            'id',
            'nama_user',
            'label_aktivitas',
            'locations',
            'created_at'
        ]
