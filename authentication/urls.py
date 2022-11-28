from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

from . import views


urlpatterns = [
    path('signup/', views.UserViewset.as_view({
        'post': 'create'
    }), name='signup'),
    path(
        'login/',
        jwt_views.TokenObtainPairView.as_view(),
        name='token_obtain_pair',
    ),
    path(
        'api/token/refresh/',
        jwt_views.TokenRefreshView.as_view(),
        name='token_refresh',
    ),
]
