import graphene


class UpdateIncampusStatus(graphene.Mutation):
    class Arguments:
        params = UpdateIncampusStatusParams(required=True)

    Output = UpdateIncampusStatusResponse

    @staticmethod
    def mutate(root, info, params):
        # storage = StorageImplementation()
        # interactor = UpdateDestinationInteractor(storage=storage)
        #
        # update_destination_dto = MutateDestinationDTO(
        #     name = params.name,
        #     description = params.description,
        #     tags = params.tags,
        #     id=params.destination_id,
        #     user_id=info.context.user_id
        # )
        # try:
        #     destination_dto = interactor.update_destination(destination_id=params.destination_id, update_destination_dto=update_destination_dto)
        # except InvalidAdminUser:
        #     return UserNotAdmin(user_id= info.context.user_id)
        # except InvalidDestination:
        #     return DestinationNotFound(destination_id=params.destination_id)
        #
        # return Destination(
        #         id = destination_dto.id,
        #         name = destination_dto.name,
        #         description = destination_dto.description,
        #         tags = destination_dto.tags,
        #         user_id = destination_dto.user_id
        #     )
        pass