from rest_framework import serializers

from django_swagger_utils.drf_server.utils.decorator.deserialize import deserialize
from django_swagger_utils.drf_server.utils.server_gen.type_file_utils import get_type_object
from django_swagger_utils.drf_server.utils.server_gen.type_file_utils import get_type_list_object
from django_swagger_utils.drf_server.fields.collection_format_field import CollectionFormatField


class UserType(object):
    def __init__(self, username, password, in_campus, created_at=None, updated_at=None,  **kwargs):
        self.username = username
        self.password = password
        self.in_campus = in_campus
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        from django_swagger_utils.drf_server.utils.server_gen.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    in_campus = serializers.CharField()
    created_at = serializers.DateTimeField(required=False, allow_null=True, format='%Y-%m-%d %H:%M:%S')
    updated_at = serializers.DateTimeField(required=False, allow_null=True, format='%Y-%m-%d %H:%M:%S')

    def create(self, validated_data):
        return UserType(**validated_data)
