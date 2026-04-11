
"""
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

class ExampleView(APIView):

    def get(self, request, format=None):
        content = {
            'message':'request was permitted'
        }

        return Response(content)
"""
#from django.http import JsonResponse

from drf_yasg.utils import swagger_auto_schema

from rest_framework.decorators import api_view
from rest_framework.response import Response
from movies.models import Movie
from movies.serializers import MovieSerializers

@swagger_auto_schema(method="POST", request_body=MovieSerializers)
@api_view(["GET", "POST"])

def get_movie(request):

    if request.method == "GET":
        movies = Movie.objects.all()
        data = []

        #for element in movies:
        #    data.append({'id':element.id,'title':element.title})

        ##return JsonResponse(data, safe=False)
        #return Response(data,status=200)

        serializer = MovieSerializers(movies,many=True)

        return Response(serializer.data,status=200)    

    if request.method=="POST":

        serializer= MovieSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors,status=400)
    
    return Response({}, status=405)