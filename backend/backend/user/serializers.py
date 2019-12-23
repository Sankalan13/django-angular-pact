from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .helpers import is_email_verified


class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    username = serializers.SerializerMethodField()
    email = serializers.ReadOnlyField()
    first_name = serializers.SerializerMethodField()
    last_name = serializers.ReadOnlyField()
    is_admin = serializers.SerializerMethodField()
    email_verified = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'url',
            'username',
            'email',
            'first_name',
            'last_name',
            'is_admin',
            'groups',
            'id',
            'email_verified'
        ]

    def get_first_name(self, user):
        return user.first_name

    def get_username(self, user):
        return user.username

    def get_last_name(self, user):
        return user.last_name

    def get_code(self, user):
        if user.is_authenticated():
            return 200
        return 500

    def get_is_admin(self, user):
        return user.is_superuser or user.is_staff

    def get_email_verified(self, user):
        return is_email_verified(user)

    # def create(self, validated_data):
    #     return User.objects._create_user(**validated_data)
    #
    # def create_superuser(self, validated_data):
    #     return User.objects.create_superuser(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.url = validated_data.get('url', instance.url)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.firstname = validated_data.get('first_name', instance.firstname)
    #     instance.lastname = validated_data.get('last_name', instance.lastname)
    #     instance.is_admin = validated_data.get('is_admin', instance.is_admin)
    #     instance.groups = validated_data.get('groups', instance.groups)
    #     instance.id = validated_data.get('id', instance.id)
    #     instance.email_verified = validated_data.get('email_verified', instance.email_verified)
    #     instance.save()
    #     return instance


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
