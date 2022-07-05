from .models import Person
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict


class PersonAPIViews(APIView):
   def get(self, request):
       lst=Person.objects.all().values()
       return Response({'posts': list(lst)})

   def post(self, request):
       post_new=Person.objects.create(
           title=request.data['title'],
           content=request.data['content'],
           cat_id=request.data['cat_id']
       )
       return Response({'post': model_to_dict(post_new)})