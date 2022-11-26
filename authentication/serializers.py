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
    #     user = super(UserSerializer, self).create(validated_data)
    #     if 'password' in validated_data:
    #           user.set_password(validated_data['password'])
    #           user.save()
    #     return user
