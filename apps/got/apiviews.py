from rest_framework import viewsets

from apps.got.models import House, Member
from apps.got.serializers import HouseSerializer, MemberSerializer


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
