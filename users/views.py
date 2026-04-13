from django.shortcuts import render

# Create your views here.

from drf_yasg.utils import swagger_auto_schema

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from users.models import RateMovie
from users.serializer import RateMovieSerializer

class RateView(ViewSet):
    serializer_class=RateMovieSerializer

    def list(self, request):
        user_rates = RateMovie.objects.filter(user__id=request.user.id)
        serializer = RateMovieSerializer(user_rates,many=True)
        return Response(serializer.data,status=200) 

    @swagger_auto_schema(request_body=RateMovieSerializer)
    def create(self, request):

        if request.data['user'] != request.user.id:
            return Response("User doesn't match", status=403)

        serializer= RateMovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors,status=400)

   