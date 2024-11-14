environment_variables = {
    'Variables': {

        "APIGATEWAY_ENDPOINT": "https://smart-food-management-alpha.apigateway.in",
        "AWS_ACCOUNT_ID": "607092105028",
        "AWS_CLOUDFRONT_DOMAIN": "xxxxx.cloudfront.net",
        "AWS_STORAGE_BUCKET_NAME": "smart-food-management-media-static",
        "CUSTOM_AWS_ACCESS_KEY_ID": "",
        "CUSTOM_AWS_SECRET_ACCESS_KEY": "",
        "DJANGO_SETTINGS_MODULE": "smart_food_management.settings.alpha",
        "function": "smart-food-management-alpha",

        'LE_200_TOKEN': u'',
        'LE_DB_TOKEN': u'',
        'LE_NON_200_TOKEN': u'',
        'LE_NON_API_TOKEN': u'',
        'LE_PYNAMODB_TOKEN': u'',
        'LE_TOKEN': u'',

        'RAVEN_DSN': u'',

        "RDS_PORT": "3306",
        "RDS_DB_ENGINE": "django.db.backends.mysql",
        "RDS_DB_NAME": "",
        "RDS_USERNAME": "",
        "RDS_PASSWORD": "",
        "RDS_HOSTNAME": "",

        "SECRET_KEY": "YzM3YTNlODctZjNmMy00ZjAzLTlhYzctYTQzMzk4M2Y5YTRk",
        "SENTRY_DSN": "",
        "STAGE": "alpha",

        "EMAIL_HOST": "",
        "EMAIL_HOST_PASSWORD": "",
        "EMAIL_HOST_USER": "",
        "EMAIL_PORT": "465",
        "EMAIL_USE_TLS": "True",
        "DEFAULT_SENDER_EMAIL": "",
        "DEFAULT_SENDER_NAME": "",

        "DEFAULT_SMS_SENDER_ID": "",
        "MSG91_AUTH_KEY": "",  # need to change
        "MSG91_OTP_TEMPLATE_ID": "",
        "OTP_MAX_RETRIES_COUNT": "20",

        'S3_COGNITO_DEVELOPER_IDENTITY_NAME': 'smart-food-management-alpha.apigateway.in',
        'S3_COGNITO_IDENTITY_POOL_ID': u'',
        'S3_COGNITO_POOL_REGION_NAME': 'ap-south-1',

    }
}

import boto3

lambda_client = boto3.client('lambda', region_name='ap-south-1')
print(lambda_client.update_function_configuration(
    FunctionName=environment_variables['Variables']['function'],
    Environment=environment_variables))
