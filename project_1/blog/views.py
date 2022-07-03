from django.shortcuts import render
from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


# class PersonAPIViews(generics.ListAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer


class PersonAPIViews(APIView):
   def get(self, request):
       return Response({'title', 'Linus'})