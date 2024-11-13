class InvalidLoginResponse(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '{"status_code": 1, "res_status": "INVALID_USERNAME", "response": {"message": "string"}}',
            "response_serializer": "InvalidLoginSerializer",
            "response_serializer_import_str": "from meals.build.responses.InvalidLogin.InvalidLogin.InvalidLoginSerializer import InvalidLoginSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass