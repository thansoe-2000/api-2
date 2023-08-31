from rest_framework.response import Response
from rest_framework.decorators import api_view
from mainapp.models import *
from .serializers import *


@api_view(['GET'])
def getData(requset):
     person = Person.objects.all()
     serializer = PersonSerializer(person, many=True)
     return Response(serializer.data)

@api_view(['POST'])
def addPerson(request):
     serializer = PersonSerializer(data=request.data)
     if serializer.is_valid():
          serializer.save()
     return Response(serializer.data)