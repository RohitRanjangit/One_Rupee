from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import NgoSerializer
from .models import Ngo
from django.contrib.auth.models import AnonymousUser


@api_view(['POST', ])
def register(request):
    if request.method == 'POST':
        serializer = NgoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # we will implement json response later
            return Response({'data': serializer.data, 'message': "success"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
