import io

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Person


class PersonModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content


class PersonSerializer(serializers.Serializer):
   title=serializers.CharField(max_length=150)
   content=serializers.CharField()


def encode():
    model=PersonModel('Vasya Pupkin', 'His message to the world!')
    model_sr=PersonSerializer(model)
    print(model_sr.data, type(model_sr.data), sep='\n')
    json = JSONRenderer().render(model_sr.data)
    print(json)


def decode():
    stream=io.BytesIO(b'{"title": "Vasya Pupkin", "content": "His message to the world!"}')
    data=JSONParser().parse(stream)
    serializer=PersonSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)