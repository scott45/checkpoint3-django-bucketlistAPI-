from rest_framework import serializers
from .models import Bucketlist, Item


class BucketlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bucketlist
        fields = ('name', 'date_created', 'date_modified', 'created_by')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'date_created', 'date_modified', 'bucketlist')
