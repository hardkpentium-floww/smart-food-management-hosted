import graphene

from graphql_service.custom_scalars import GQLDateTimeScalar
from meals_gql.enums import MealTypeEnum, MealPreferenceEnum, MealStatusEnum

class MealItemParams(graphene.InputObjectType):
    item_id = graphene.String()
    quantity = graphene.Int()


class AddMealForUserParams(graphene.InputObjectType):
    meal_items = graphene.List(MealItemParams)
    date = GQLDateTimeScalar()
    meal_type = graphene.Field(MealTypeEnum)
    meal_status = graphene.Field(MealStatusEnum)
    meal_preference = graphene.Field(MealPreferenceEnum)

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