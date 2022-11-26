from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from . import views


router = routers.SimpleRouter()

router.register('signup', views.UserViewset, basename='signup')

urlpatterns = [
    # Include login/ & logout/ paths
    path('', include('rest_framework.urls')),
    path('', include(router.urls)),
    path(
        'api/token/',
        jwt_views.TokenObtainPairView.as_view(),
        name='token_obtain_pair',
    ),
    path(
        'api/token/refresh/',
        jwt_views.TokenRefreshView.as_view(),
        name='token_refresh',
    ),
]
