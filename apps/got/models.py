from django.db import models

from main.models import Registry


class House(Registry):
    class Meta:
        db_table = 'house'
    
    region = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    blazon = models.CharField(max_length=200, null=True)
    seat = models.CharField(max_length=200, null=True)
    words = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name

class Member(Registry):
    class Meta:
        db_table = 'member'
    
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    house = models.ForeignKey(
        House,
        on_delete=models.CASCADE,
        related_name='members',
        related_query_name='member'
    )
    
    def __str__(self):
        return self.name
