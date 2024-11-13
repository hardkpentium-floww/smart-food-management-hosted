import graphene

from graphql_service.custom_scalars import GQLDateTimeScalar
from meals_gql.enums import TypeEnum, MealTypeEnum


class Meal(graphene.ObjectType):
    id = graphene.String()
    date = graphene.DateTime()
    type = graphene.Field(TypeEnum)


class ScheduleMealParams(graphene.InputObjectType):
    item_ids = graphene.List(graphene.String)
    full_meal_quantities = graphene.List(graphene.Int)
    half_meal_quantities = graphene.List(graphene.Int)
    date = GQLDateTimeScalar()
    type = graphene.Field(TypeEnum)
    meal_type = graphene.Field(MealTypeEnum)

class ScheduleMealSuccess(graphene.ObjectType):
    meal_id = graphene.String()

class ScheduleMealFailure(graphene.ObjectType):
    message = graphene.String()


class ScheduleMealResponse(graphene.Union):
    class Meta:
        types = (ScheduleMealSuccess, ScheduleMealFailure)
