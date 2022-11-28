from rest_framework import viewsets
from .serializers import UserSerializer


class UserViewset(viewsets.ModelViewSet):

    serializer_class = UserSerializer
