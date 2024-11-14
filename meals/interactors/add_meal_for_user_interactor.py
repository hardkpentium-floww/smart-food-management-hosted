from meals.exceptions.custom_exceptions import NoItemsFound
from meals.interactors.storage_interfaces.storage_interface import StorageInterface, AddMealDTO


class AddMealForUserInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def add_meal_for_user(self, add_meal_dto: AddMealDTO):

        user_meal_id = self.storage.add_meal_for_user(add_meal_dto=add_meal_dto)

        return user_meal_id