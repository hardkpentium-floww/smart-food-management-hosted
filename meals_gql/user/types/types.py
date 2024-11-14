import graphene

from graphql_service.custom_scalars import GQLDateTimeScalar
from meals_gql.enums import MealTypeEnum, MealPreferenceEnum, MealStatusEnum


class AddMealForUserParams(graphene.InputObjectType):
    user_id = graphene.String()
    item_ids = graphene.List(graphene.Int)
    quantities = graphene.List(graphene.Int)
    date = GQLDateTimeScalar()
    type = graphene.Field(MealTypeEnum)
    meal_type = graphene.Field(MealPreferenceEnum)
    skip_meal = graphene.Field(MealStatusEnum)

class MealAddSuccess(graphene.ObjectType):
    user_meal_id = graphene.String()

class MealAddFailure(graphene.ObjectType):
    message = graphene.String()


class AddMealForUserResponse(graphene.Union):
    class Meta:
        types = (MealAddSuccess, MealAddFailure)

class UpdateIncampusStatusParams(graphene.InputObjectType):
    user_id = graphene.String()
    in_campus = graphene.Boolean()

class UpdateIncampusStatusResponse(graphene.ObjectType):
    message = graphene.String()