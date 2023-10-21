from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from cn_p2_simple_ws.models import Directory


class StatusApiView(APIView):

    def get(self, request, *args, **kwargs):
        return Response({'response': 'pong'})


class DirectorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Directory
        fields = '__all__'


class DirectoryListCreateAPIView(ListCreateAPIView):

    queryset = Directory.objects.all()
    serializer_class = DirectorySerializer


class DirectoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Directory.objects.all()
    serializer_class = DirectorySerializer
