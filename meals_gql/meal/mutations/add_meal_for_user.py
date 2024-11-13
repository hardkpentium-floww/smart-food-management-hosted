import graphene

from meals_gql.user.types.types import AddMealForUserParams, AddMealForUserResponse


class AddMealForUser(graphene.Mutation):
    class Arguments:
        params = AddMealForUserParams(required=True)

    Output = AddMealForUserResponse
    #
    # @staticmethod
    def mutate(root, info, params):
        pass
    #     storage = StorageImplementation()
    #     interactor = AddDestinationInteractor(storage=storage)
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
