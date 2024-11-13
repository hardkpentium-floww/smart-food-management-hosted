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
    access_token_id: str

@dataclass
class ItemDTO:
    id: str
    name: str
    category: str
    base_size_unit: str
    serving_size_unit: str


@dataclass
class ScheduleMealDTO:
    item_ids: [str]
    full_meal_quantities: [int]
    half_meal_quantities: [int]
    date: datetime
    type: str
    meal_type: str


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
    def get_items(self,offset:int,limit:int):
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
    def schedule_meal(self, schedule_meal_dto: ScheduleMealDTO):
        pass

    @abstractmethod
    def create_refresh_token(self, refresh_token_dto: RefreshTokenDTO):
        pass

    @abstractmethod
    def validate_item_ids(self, item_ids: [int]):
        pass

    @abstractmethod
    def validate_quantities(self, full_meal_quantities:[int], half_meal_quantities:[int]):
        pass

    @abstractmethod
    def validate_date(self, date: datetime):
        pass