from .models import Person
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PersonSerializer


class PersonAPIViews(APIView):
   def get(self, request):
       p=Person.objects.all()
       return Response({'posts': PersonSerializer(p, many=True).data})

   def post(self, request):
       serializer = PersonSerializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       return Response({'post': serializer.data})

   def put(self, request, *args, **kwargs):
       pk = kwargs.get('pk', None)
       if not pk:
           return Response({'error': 'Metod PUT not allowed'})

       try:
           instance = Person.objects.get(pk=pk)
       except:
           return Response({'error': 'Object does not exists'})

       serializer = PersonSerializer(data=request.data, instance=instance)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       return Response({'post': serializer.data})
