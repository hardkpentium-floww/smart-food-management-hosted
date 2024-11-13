class UserParamParameter(object):
    @staticmethod
    def get_param_name():
        param_names = {
            "parameter_name": "userParam",
            "parameter_field_name": "user_param"
        }
        return param_names

    @staticmethod
    def get_serializer_class():
        serializer_options = {
            "param_serializer": "user_paramSerializer",
            "param_serializer_import_str": "from meals.build.parameters.userParam.user_param.user_paramSerializer import user_paramSerializer",
            "param_serializer_required": False,
            "param_serializer_array": False
        }
        return serializer_options
        

    @staticmethod
    def get_serializer_field():
        pass

    @staticmethod
    def get_url_regex():
        pass