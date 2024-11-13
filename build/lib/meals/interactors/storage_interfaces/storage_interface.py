from abc import abstractmethod
from datetime import datetime
from attr import dataclass


@dataclass
class AccessTokenDTO:
    user_id: str
    token: str
    application_id: int
    expires: datetime
    scope: str

@dataclass
class RefreshTokenDTO:
    user_id: str
    refresh_token: str
    application_id: int
    access_token_id: int



class StorageInterface:
    @abstractmethod
    def login(self, username: str, user_id: str, password:str):
        pass

    @abstractmethod
    def logout(self, user_id:str, access_token:str):
        pass

    @abstractmethod
    def get_application_id(self, application_name: str):
        pass

    @abstractmethod
    def expire_access_token(self, access_token_id:str):
        pass

    @abstractmethod
    def revoke_refresh_token(self, refresh_token_id: str):
        pass

    @abstractmethod
    def get_user_acc(self, user_id: str):
        pass

    @abstractmethod
    def get_user(self, username:str):
        pass

    @abstractmethod
    def create_access_token(self, access_token_dto:AccessTokenDTO):
        pass


    @abstractmethod
    def create_refresh_token(self, refresh_token_dto: RefreshTokenDTO):
        pass