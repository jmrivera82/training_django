from django.urls import path
from movies.views import get_movie



app_name='movies'

urlpatterns = [
    path('',get_movie,name='movie')
]


