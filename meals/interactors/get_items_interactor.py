from build.lib.meals.storages.storage_implementation import StorageImplementation
from meals.exceptions.custom_exceptions import NoItemsFound


class GetItemsInteractor:
    def __init__(self, storage: StorageImplementation):
        self.storage = storage

    def get_items(self,offset:int,limit:int):

        item_dtos = self.storage.get_items(offset=offset,limit=limit)

        if len(item_dtos) == 0:
            raise NoItemsFound

        return item_dtos