class Status201Response(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '{"status_code": 1, "res_status": "string", "response": {"message": "string"}}',
            "response_serializer": "Status_201Serializer",
            "response_serializer_import_str": "from meals.build.view_environments.logout_.logout.responses.Status_201.Status_201.Status_201Serializer import Status_201Serializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass