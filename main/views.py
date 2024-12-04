from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from main.serializers import LectureSerializer
from main.models import Lecture
from rest_framework import generics


# Create your views here.
class LectureListView(generics.ListCreateAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer

    def post(self, request):
        serializer = LectureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class LectureDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
