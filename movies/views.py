
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
from rest_framework.views import APIView

from movies.models import Movie
from movies.serializers import MovieSerializers, MovieModeSerializer

class MoviesView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieModeSerializer(movies,many=True)
        return Response(serializer.data,status=200) 

    @swagger_auto_schema(request_body=MovieModeSerializer)
    def post(self, request):
        serializer= MovieModeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors,status=400)

    @swagger_auto_schema(request_body=MovieModeSerializer)
    def put (self, request, pk=None):
        try:
            movie=Movie.objects.get(id=pk)
            serializer= MovieSerializers(movie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors,status=400)
        except:
            return Response('NOT FOUND', status=404)

#@swagger_auto_schema(method="POST", request_body=MovieSerializers)
@swagger_auto_schema(method="POST", request_body=MovieModeSerializer)
@api_view(["GET", "POST"])

def get_movie(request):

    if request.method == "GET":
        movies = Movie.objects.all()
        #data = []

        #for element in movies:
        #    data.append({'id':element.id,'title':element.title})

        ##return JsonResponse(data, safe=False)
        #return Response(data,status=200)

        #serializer = MovieSerializers(movies,many=True)
        serializer = MovieModeSerializer(movies,many=True)
        return Response(serializer.data,status=200)    

    if request.method=="POST":

        #serializer= MovieSerializers(data=request.data)
        serializer= MovieModeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors,status=400)
    
    #return Response({}, status=405)


@swagger_auto_schema(method="PUT", request_body=MovieSerializers)
@api_view(["PUT"])

def update_movie(request,pk):
    try:
        movie=Movie.objects.get(id=pk)
        serializer= MovieSerializers(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors,status=400)
    except:
        return Response('NOT FOUND', status=404)