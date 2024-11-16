from datetime import datetime, timedelta
from unittest.mock import patch

import pytest

from meals.storages.storage_implementation import StorageImplementation
from meals.tests.factories.models import ApplicationFactory, UserFactory, UserAccountFactory, AccessTokenFactory, \
    RefreshTokenFactory
from meals.tests.factories.storage_dtos import AccessTokenDTOFactory, RefreshTokenDTOFactory



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
        application = ApplicationFactory(id=access_token_dto.application_id, user_id=access_token_dto.user_id)

        access_token = storage.create_access_token(access_token_dto=access_token_dto)

        assert access_token.user_id == access_token_dto.user_id
        assert access_token.token == access_token_dto.token
        assert access_token.application_id == access_token_dto.application_id
        assert access_token.expires == access_token_dto.expires
        assert access_token.scope == access_token_dto.scope

    def test_create_refresh_token(self, storage):
        refresh_token_dto = RefreshTokenDTOFactory()
        user = UserAccountFactory(user_id = refresh_token_dto.user_id)
        application = ApplicationFactory(id=refresh_token_dto.application_id, user_id=refresh_token_dto.user_id)
        access_token = AccessTokenFactory(id=refresh_token_dto.access_token_id, user_id=refresh_token_dto.user_id, application_id=refresh_token_dto.application_id)

        refresh_token = storage.create_refresh_token(refresh_token_dto=refresh_token_dto)

        assert refresh_token.user_id == refresh_token_dto.user_id
        assert refresh_token.token == refresh_token_dto.refresh_token
        assert refresh_token.application_id == refresh_token_dto.application_id
        assert refresh_token.access_token_id == refresh_token_dto.access_token_id



    def test_get_application_id(self, storage):
        application = ApplicationFactory()
        user = UserAccountFactory(user_id = application.user_id)
        app_id = storage.get_application_id(application_name = application.name)

        assert app_id == application.id

    def test_expire_access_token(self, storage):
        user = UserAccountFactory()
        application = ApplicationFactory(user_id=user.user_id)
        access_token = AccessTokenFactory(user_id=user.user_id, application_id=application.id)

        access_token = storage.expire_access_token(access_token_id=access_token.id)
        assert access_token.expires.date() == datetime.now().date()

    def test_revoke_refresh_token(self, storage):
        user = UserAccountFactory()
        application = ApplicationFactory()
        access_token = AccessTokenFactory(user_id=user.user_id, application_id=application.id)
        refresh_token = RefreshTokenFactory(access_token_id=access_token.id, application_id=application.id, user_id=user.user_id)

        refresh_token  = storage.revoke_refresh_token(refresh_token_id=refresh_token.id)

        assert refresh_token.revoked.date() == datetime.now().date()

    # def get_items(self, offset: int, limit: int):
    #     pass
    #
    # def get_user_acc(self, user_id: str):
    #     pass
    #
    # def get_user(self, username: str):
    #     pass
    #
    # def create_access_token(self, access_token_dto: AccessTokenDTO):
    #     pass
    #
    # def schedule_meal(self, schedule_meal_dto: ScheduleMealDTO):
    #     pass
    #
    # def create_refresh_token(self, refresh_token_dto: RefreshTokenDTO):
    #     pass
    #
    # def validate_item_ids(self, item_ids: [int]):
    #     pass
    #
    # def validate_quantities(self, quantities: [int]):
    #     pass
    #
    # def validate_date(self, date: datetime):
    #     pass
    #
    # def get_scheduled_meal_by_admin(self, date: datetime, meal_type: str):
    #     pass
    #
    # def get_meal_status(self, meal_id: str):
    #     pass
    #
    # def save_meal_status(self, meal_id: str, meal_status: str):
    #     pass
    #
    # def get_meal_preference(self, meal_id: str, user_id: str, meal_type: str):
    #     pass
    #
    # def check_meal_type(self, meal_type: str):
    #     pass
    #
    # def check_meal_status(self, meal_status: str):
    #     pass
    #
    # def check_meal_preference(self, meal_preference: str):
    #     pass
    #
    # def add_meal_for_user(self, add_meal_dto: AddMealDTO):
    #     pass
    #
    # def update_incampus_status(self, user_id: str, incampus_status: bool):
    #     pass
    #
    # def get_scheduled_meal_for_user(self, user_id: str, date: datetime):
    #     pass
    #
    #
    #
    #
    #









