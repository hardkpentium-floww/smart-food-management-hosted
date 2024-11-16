import json
from unittest.mock import create_autospec, patch, Mock
import pytest

from meals.interactors.login_interactor import LoginInteractor
from meals.interactors.logout_interactor import LogoutInteractor
from meals.interactors.storage_interfaces.storage_interface import StorageInterface
from meals.tests.factories.models import UserAccountFactory, UserFactory


class TestInteractor:
    @pytest.fixture
    def storage(self):
        storage = create_autospec(StorageInterface)
        return storage


    def test_login(self,storage):
        interactor = LoginInteractor(storage=storage)
        user = Mock()
        user.id = "1"
        user.name = "user"

        user_acc = Mock()
        user_acc.user_id = "1"
        user_acc.user_name = "user"

        storage.get_user.return_value = user
        storage.get_user_acc.return_value = user_acc
        user_acc.check_password.return_value = True

        storage.login.return_value = {
            "status_code": 200,
            "res_status": "LOGIN_SUCCESS",
            "response": {
                    "access_token": "access_token_str",
                    "expires_in": "expires",
                    "token_type": "Bearer",
                    "scope": "read write",
                    "refresh_token": "refresh_token_str"
                }
        }

        response = interactor.login(username=user.name, password="user_password")
        response_data = json.loads(response.content.decode('utf-8'))
        login_response = response_data["response"]["response"]
        expected_login_response =  {
            "status_code": 200,
            "res_status": "LOGIN_SUCCESS",
            "response": {
                    "access_token": "access_token_str",
                    "expires_in": "expires",
                    "token_type": "Bearer",
                    "scope": "read write",
                    "refresh_token": "refresh_token_str"
                }
        }

        storage.get_user.assert_called_once_with(username=user.name)
        storage.get_user_acc.assert_called_once_with(user_id=user.id)
        user_acc.check_password.assert_called_once_with("user_password")

        assert login_response["access_token"] == expected_login_response["response"]["access_token"]

    def test_login_with_invalid_username(self,storage):
        interactor = LoginInteractor(storage=storage)
        user = Mock()
        user.id = 1
        user.name = "invalid_user"

        user_acc = Mock()
        user_acc.user_id = 2
        user_acc.user_name = "user"

        storage.get_user.return_value = None
        storage.get_user_acc.return_value = user_acc
        user_acc.check_password.return_value = True


        response = interactor.login(username="user.name", password="user_password")
        response_data = json.loads(response.content.decode('utf-8'))
        login_response = response_data
        expected_login_response = {
                "status_code": 401,
                "res_status": "INVALID_USERNAME",
                "response": {
                    "message": "Invalid Username"
                }
            }

        storage.get_user.assert_called_once_with(username="user.name")

        assert login_response["status_code"] == expected_login_response["status_code"]
        assert login_response["res_status"] == expected_login_response["res_status"]
        assert login_response["response"]["message"] == expected_login_response["response"]["message"]





    def test_login_invalid_password(self,storage):
        interactor = LoginInteractor(storage=storage)
        user = Mock()
        user.id = "1"
        user.name = "user"

        user_acc = Mock()
        user_acc.user_id = "1"
        user_acc.user_name = "user"

        storage.get_user.return_value = user
        storage.get_user_acc.return_value = user_acc
        user_acc.check_password.return_value = False


        response = interactor.login(username="user.name", password="user_password")
        response_data = json.loads(response.content.decode('utf-8'))
        login_response = response_data
        expected_login_response = {
                    "status_code": 401,
                    "res_status": "INVALID_PASSWORD",
                    "response": {
                        "message": "Invalid Password"
                    }
                }

        storage.get_user.assert_called_once_with(username="user.name")
        storage.get_user_acc.assert_called_once_with(user_id=user.id)
        user_acc.check_password.assert_called_once_with("user_password")

        assert login_response["status_code"] == expected_login_response["status_code"]
        assert login_response["res_status"] == expected_login_response["res_status"]
        assert login_response["response"]["message"] == expected_login_response["response"]["message"]


    def test_logout(self, storage):
        interactor = LogoutInteractor(storage=storage)

        storage.logout.return_value = None

        response = interactor.logout(user_id="user_id", access_token="access_token")
        response_data = json.loads(response.content.decode('utf-8'))
        logout_response = response_data


        expected_logout_response = {
            "status_code": 200,
            "res_status": "LOGOUT SUCCESS",
            "response": {
                "message": "logged out successfully"
            }
        }

        assert logout_response["status_code"] == expected_logout_response["status_code"]
        assert logout_response["res_status"] == expected_logout_response["res_status"]
        assert logout_response["response"]["message"] == expected_logout_response["response"]["message"]


    def test_get_items(self, storage):
        pass

    def test_get_items_with_no_items(self, storage):
        pass

    def test_add_meal_for_user(self, storage):
        pass

    def test_save_meal_for_user(self,storage):
        pass

    def test_schedule_meal(self, storage):
        pass

    def test_update_scheduled_meal(self, storage):
        pass

    def test_get_meal_preference(self, storage):
        pass

    def test_get_meal_status(self, storage):
        pass

    def test_get_scheduled_meal_by_admin(self, storage):
        pass

    def test_get_scheduled_meal_by_admin_with_no_meals(self, storage):
        pass


    def test_get_scheduled_meal_for_user(self, storage):
        pass

    def test_get_scheduled_meal_for_user_with_no_user_meals(self, storage):
        pass

    def test_update_incampus_status(self, storage):
        pass

