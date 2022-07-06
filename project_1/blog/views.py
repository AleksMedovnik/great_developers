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

       post_new=Person.objects.create(
           title=request.data['title'],
           content=request.data['content'],
           cat_id=request.data['cat_id']
       )
       return Response({'post': PersonSerializer(post_new).data})