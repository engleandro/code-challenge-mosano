from rest_framework import serializers

from apps.got.models import House, Member


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    house = HouseSerializer()
    
    class Meta:
        model = House
        fields = '__all__'
