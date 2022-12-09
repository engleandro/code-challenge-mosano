from django.test import TestCase

from apps.got.models import House, Member


class HouseModelTest(TestCase):

    def setUp(self):
        House.objects.create(
            region='Vale of Arryn',
            name='Arryn of the Eyrie',
            blazon='A sky-blue falcon soaring against a white moon, on sky-blue	Eyrie',
            seat='Eyrie',
            words="As High as Honor",
        )
    
    def test_post_house(self):
        house = House.objects.get(id=1)
        self.assertEqual(house.name, 'Arryn of the Eyrie')

class MemberModelTest(TestCase):
    
    def setUp(self):
        Member.objects.create(
            name="Jon Arryn",
            description="Patriarch, former Hand of the King, deceased",
            house=House.objects.create(
                region='Stormlands',
                name="Baratheon of Storm's End",
                blazon='A crowned stag black on a golden field',
                seat="Storm's Enn",
                words="Ours is the Fury",
            )
        )
    
    def test_post_member(self):
        member = Member.objects.get(pk=1)
        self.assertEqual(member.name, "Jon Arryn")
        self.assertEqual(member.house.pk, 2)
