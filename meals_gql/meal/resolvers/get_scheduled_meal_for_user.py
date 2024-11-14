from meals.storages.storage_implementation import StorageImplementation
from meals_gql.meal.types.types import UserScheduledMeal, UserMeal


def resolve_get_scheduled_meal_for_user(self, info,params):

    storage = StorageImplementation()
    # interactor = GetScheduledMealForUser(storage=storage)

    # user_scheduled_meal_dto = interactor.get_scheduled_meal_for_user(user_id=info.context.user_id, date=params.date)
    #
    # meals_type = [
    #     UserMeal(
    #         meal_type=user_scheduled_meal_dto.
    #     )
    # ]
    #
    # return UserScheduledMeal(
    #     date = params.date,
    #     meals = meals_type
    # )


    #
    # get_destinations_dto = GetDestinationsDTO(
    #     tag = params.tag,
    #     offset = params.offset,
    #     limit = params.limit
    # )
    #
    #
    # destination_dtos = interactor.get_destinations(get_destinations_dto=get_destinations_dto)
    #
    # return Destinations(destinations= [Destination(
    #         id=destination_dto.id,
    #         name=destination_dto.name,
    #         description=destination_dto.description,
    #         tags=destination_dto.tags,
    #         user_id=destination_dto.user_id
    #     )
    #     for destination_dto in destination_dtos])
    pass