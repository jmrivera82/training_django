from django.urls import path
from movies.views import get_movie, update_movie, MoviesView


app_name='movies'

urlpatterns = [
    #path('',get_movie,name='movie'),
    #path('<int:pk>',update_movie,name='movie'),
    path('',MoviesView.as_view(),name='movie')
]


