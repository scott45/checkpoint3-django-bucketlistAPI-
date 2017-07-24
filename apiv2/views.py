from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Bucketlist, Item
from .serializers import ItemSerializer, BucketlistSerializer


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_bucketlist(request, pk):
    try:
        bklist = Bucketlist.objects.get(pk=pk)
    except Bucketlist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single bucketlist
    if request.method == 'GET':
        return Response({})
    # delete a single bucketlist
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single bucketlist
    elif request.method == 'PUT':
        return Response({})


@api_view(['GET', 'POST'])
def get_post_bucketlist(request):
    # get all bucketlists
    if request.method == 'GET':
        puppies = Bucketlist.objects.all()
        serializer = BucketlistSerializer(puppies, many=True)
        return Response(serializer.data)
    # insert a new record for a bucketlist
    elif request.method == 'POST':
        return Response({})
