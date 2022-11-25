from django.urls import path, include
from . import views


urlpatterns = [
    # Include login/ & logout/ paths
    path('', include('rest_framework.urls')),
]
