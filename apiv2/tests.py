from django.test import TestCase
import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import Bucketlist, Item
from .serializers import BucketlistSerializer, ItemSerializer


# initialize the APIClient app
client = Client()

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


class GetAllPuppiesTest(TestCase):
    """ Test module for GET all bucketlist API """

    def setUp(self):
        Bucketlist.objects.create(name='Travel')
        Bucketlist.objects.create(name='Ministry')
        Bucketlist.objects.create(name='Travel')
        Bucketlist.objects.create(name='Ministry')

    def test_get_all_bucketlists(self):
        # get API response
        response = client.get(reverse('get_post_bucketlists'))
        # get data from db
        blists = Bucketlist.objects.all()
        serializer = BucketlistSerializer(blists, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
