import graphene

from meals.interactors.add_meal_for_user_interactor import AddMealForUserInteractor
from meals.interactors.storage_interfaces.storage_interface import AddMealDTO, UserMealItemDTO
from meals.storages.storage_implementation import StorageImplementation
from meals_gql.user.types.types import AddMealForUserParams, AddMealForUserResponse, MealAddSuccess


class AddMealForUser(graphene.Mutation):
    class Arguments:
        params = AddMealForUserParams(required=True)

    Output = AddMealForUserResponse
    #
    # @staticmethod
    def mutate(root, info, params):
        storage = StorageImplementation()
        interactor = AddMealForUserInteractor(storage=storage)

        meal_items = [
            UserMealItemDTO(
                item_id = item.item_id,
                quantity = item.quantity
            ) for item in params.meal_items
        ]

        add_meal_dto = AddMealDTO(
            user_id = info.context.user_id,
            meal_id = params.meal_id,
            meal_type = params.meal_type,
            meal_preference = params.meal_preference,
            date = params.date,
            meal_items= meal_items,
            meal_status=params.meal_status
        )

        user_meal_id = interactor.add_meal_for_user(add_meal_dto=add_meal_dto)

        return MealAddSuccess(user_meal_id = user_meal_id)

    #
    #     add_destination_dto = AddDestinationDTO(
    #         name = params.name,
    #         description = params.description,
    #         tags = params.tags,
    #         user_id = info.context.user_id
    #     )
    #
    #     add_hotel_dtos = []
    #
    #     hotels = params.hotels
    #
    #     if hotels:
    #         add_hotel_dtos = [
    #             AddHotelDTO(
    #                 name = hotel.name,
    #                 description = hotel.description,
    #                 tariff = hotel.tariff,
    #                 image_urls = hotel.image_urls,
    #                 destination_id = hotel.destination_id
    #             )
    #             for hotel in hotels
    #         ]
    #
    #
    #
    #     try:
    #         destination_dto = interactor.add_destination(add_destination_dto=add_destination_dto, add_hotel_dtos=add_hotel_dtos)
    #     except InvalidAdminUser:
    #         return UserNotAdmin(user_id= info.context.user_id)
    #     except InvalidDestination:
    #         return DestinationNotFound()
    #
    #     return  Destination(
    #             id = destination_dto.id,
    #             name = destination_dto.name,
    #             description = destination_dto.description,
    #             tags = destination_dto.tags,
    #             user_id = destination_dto.user_id
    #         )
