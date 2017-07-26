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
        serializer = BucketlistSerializer(bklist)
        return Response(serializer.data)
    # delete a single bucketlist
    elif request.method == 'DELETE':
        bklist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # update details of a single bucketlist
    elif request.method == 'PUT':
        serializer = BucketlistSerializer(bklist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_bucketlist(request):
    # get all bucketlists
    if request.method == 'GET':
        puppies = Bucketlist.objects.all()
        serializer = BucketlistSerializer(puppies, many=True)
        return Response(serializer.data)
    # insert a new record for a bucketlist
    elif request.method == 'POST':
        data = {
            'name': request.data.get('name'),
        }
        serializer = BucketlistSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
