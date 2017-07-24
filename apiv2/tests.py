from django.test import TestCase
from .models import Bucketlist, Item


# tests for bucketlist and item models


class BucketlistTest(TestCase):
    def setUp(self):
        Bucketlist.objects.create(name='Travel')
        Bucketlist.objects.create(name='Ministry')

    def test_result(self):
        first = Bucketlist.objects.get(name='Travel')
        second = Bucketlist.objects.get(name='Ministry')
        self.assertEqual(first.get_name(), "Travel")
        self.assertEqual(second.get_name(), "Ministry")


class ItemTest(TestCase):
    def setUp(self):
        Item.objects.create(name='Europe')
        Item.objects.create(name='Souls')

    def test_output(self):
        firstitem = Bucketlist.objects.get(name='Europe')
        seconditem = Bucketlist.objects.get(name='Souls')
        self.assertEqual(firstitem.get_name(), "Europe")
        self.assertEqual(seconditem.get_name(), "Souls")
