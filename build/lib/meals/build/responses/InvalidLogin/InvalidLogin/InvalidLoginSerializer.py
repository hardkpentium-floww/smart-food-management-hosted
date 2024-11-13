from rest_framework import serializers

from django_swagger_utils.drf_server.utils.decorator.deserialize import deserialize
from django_swagger_utils.drf_server.utils.server_gen.type_file_utils import get_type_object
from django_swagger_utils.drf_server.utils.server_gen.type_file_utils import get_type_list_object
from django_swagger_utils.drf_server.fields.collection_format_field import CollectionFormatField


class InvalidLoginType(object):
    def __init__(self, status_code, res_status, response,  **kwargs):
        self.status_code = status_code
        self.res_status = res_status
        self.response = response

    def __str__(self):
        from django_swagger_utils.drf_server.utils.server_gen.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class InvalidLoginSerializer(serializers.Serializer):
    status_code = serializers.IntegerField()
    res_status = serializers.ChoiceField(choices=(('INVALID_USERNAME', 'INVALID_USERNAME'), ('INVALID_PASSWORD', 'INVALID_PASSWORD'), ('INVALID_USER', 'INVALID_USER')))
    from meals.build.responses.InvalidLogin.InvalidLogin.response.responseSerializer import responseSerializer
    response = responseSerializer()

    def create(self, validated_data):
        from meals.build.responses.InvalidLogin.InvalidLogin.response.responseSerializer import responseSerializer
        response_val, _ = deserialize(responseSerializer, validated_data.pop("response", None), many=False, partial=True)
        
        return InvalidLoginType(response=response_val, **validated_data)
