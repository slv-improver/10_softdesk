from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.SimpleRouter()

router.register('signup', views.UserViewset, basename='signup')

urlpatterns = [
    # Include login/ & logout/ paths
    path('', include('rest_framework.urls')),
    path('', include(router.urls)),
]
