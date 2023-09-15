from django.urls import path
from applications.films.views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', FilmAPIView)


urlpatterns = [
    # path('', FilmsListAPIView.as_view()),
    # path('create/', CreateFilmAPIView.as_view()),
    # path('<int:pk>/', RetrieveFilmAPIView.as_view()),
    # path('update/<int:pk>/', UpdateFilmAPIView.as_view()),
    # path('delete/<int:pk>/', DeleteFilmAPIView.as_view())
]

urlpatterns += router.urls
