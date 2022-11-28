from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):

    password_confirmation = serializers.CharField(
        style={"input_type": "password"},
        write_only=True,
    )

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'password',
            'password_confirmation',
        )

    def validate(self, data):
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError(
                'The password confirmation does not match password.'
            )
        return {
            'username': data['username'],
            'password': make_password(data['password']),
        }
