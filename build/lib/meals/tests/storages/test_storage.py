from datetime import datetime, timedelta
from unittest.mock import patch

import pytest
from ib_users.models import UserAccount

from meals.storages.storage_implementation import StorageImplementation
from meals.tests.factories.models import ApplicationFactory, UserFactory, UserAccountFactory
from meals.tests.factories.storage_dtos import AccessTokenDTOFactory
from smart_food_management.wsgi import application


@pytest.mark.django_db
class TestStorageImplementation:

    @pytest.fixture
    def storage(self):
        storage = StorageImplementation()
        return storage

    def test_login(self, storage):
        pass

    def test_create_access_token(self, storage):
        access_token_dto = AccessTokenDTOFactory()
        user = UserAccountFactory(user_id=access_token_dto.user_id)
        application = ApplicationFactory(id=access_token_dto.application_id)

        access_token = storage.create_access_token(access_token_dto=access_token_dto)

        assert access_token.user_id == access_token_dto.user_id
        assert access_token.token == access_token_dto.token
        assert access_token.application_id == access_token_dto.application_id
        assert access_token.expires == access_token_dto.expires
        assert access_token.scope == access_token_dto.scope

    def test_create_refresh_token(self, storage):
        pass

    def test_get_application_id(self, storage):
        application = ApplicationFactory()
        user = UserAccountFactory(user_id = application.user_id)
        app_id = storage.get_application_id(application_name = application.name)

        assert app_id == application.id

    def test_expire_access_token(self, storage):
        pass

    def test_revoke_refresh_token(self, storage):
        pass