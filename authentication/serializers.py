from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'password',
        )

    def validate_password(self, value):
        return make_password(value)

    # def create(self, validated_data):
    #     return get_user_model().objects.create_user(validated_data)
