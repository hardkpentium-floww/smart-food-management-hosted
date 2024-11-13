from rest_framework import serializers

from django_swagger_utils.drf_server.utils.decorator.deserialize import deserialize
from django_swagger_utils.drf_server.utils.server_gen.type_file_utils import get_type_object
from django_swagger_utils.drf_server.utils.server_gen.type_file_utils import get_type_list_object
from django_swagger_utils.drf_server.fields.collection_format_field import CollectionFormatField


class Status_201Type(object):
    def __init__(self, status_code, res_status, response,  **kwargs):
        self.status_code = status_code
        self.res_status = res_status
        self.response = response

    def __str__(self):
        from django_swagger_utils.drf_server.utils.server_gen.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class Status_201Serializer(serializers.Serializer):
    status_code = serializers.IntegerField()
    res_status = serializers.CharField()
    from meals.build.view_environments.logout_.logout.responses.Status_201.Status_201.response.responseSerializer import responseSerializer
    response = responseSerializer()

    def create(self, validated_data):
        from meals.build.view_environments.logout_.logout.responses.Status_201.Status_201.response.responseSerializer import responseSerializer
        response_val, _ = deserialize(responseSerializer, validated_data.pop("response", None), many=False, partial=True)
        
        return Status_201Type(response=response_val, **validated_data)
