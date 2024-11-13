import graphene

from build.lib.meals.storages.storage_implementation import StorageImplementation
from meals.exceptions.custom_exceptions import ItemNotFound, InvalidQuantity, InvalidDate
from meals.interactors.schedule_meal_interactor import ScheduleMealInteractor
from meals.interactors.storage_interfaces.storage_interface import ScheduleMealDTO
from meals_gql.meal.types.types import ScheduleMealParams, ScheduleMealResponse, ScheduleMealFailure,ScheduleMealSuccess


class ScheduleMeal(graphene.Mutation):
    class Arguments:
        params = ScheduleMealParams(required=True)

    Output = ScheduleMealResponse

    @staticmethod
    def mutate(root, info, params):
        pass
        storage = StorageImplementation()
        interactor = ScheduleMealInteractor(storage=storage)

        schedule_meal_dto = ScheduleMealDTO(
            item_ids = params.item_ids,
            full_meal_quantities=params.full_meal_quantities,
            half_meal_quantities=params.half_meal_quantities,
            date=params.date,
            type=params.type,
            meal_type=params.meal_type
        )

        try:
            response = interactor.schedule_meal(schedule_meal_dto=schedule_meal_dto)
        except ItemNotFound:
            return ScheduleMealFailure(message= "Invalid Item ID")
        except InvalidQuantity:
            return ScheduleMealFailure(message= "Invalid Quantity")
        except InvalidDate:
            return ScheduleMealFailure(message= "Invalid Date")

        return ScheduleMealSuccess(meal_id=response.meal_id)
