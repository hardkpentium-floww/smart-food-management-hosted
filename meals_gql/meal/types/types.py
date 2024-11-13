import graphene

from graphql_service.custom_scalars import GQLDateTimeScalar
from meals_gql.enums import TypeEnum, MealTypeEnum, MealStatusEnum


class Meal(graphene.ObjectType):
    id = graphene.String()
    date = graphene.DateTime()
    meal_preference = graphene.Field(TypeEnum)


class ScheduleMealParams(graphene.InputObjectType):
    item_ids = graphene.List(graphene.String)
    full_meal_quantities = graphene.List(graphene.Int)
    half_meal_quantities = graphene.List(graphene.Int)
    date = GQLDateTimeScalar()
    meal_preference = graphene.Field(TypeEnum)
    meal_type = graphene.Field(MealTypeEnum)

class ScheduleMealSuccess(graphene.ObjectType):
    meal_id = graphene.String()

class ScheduleMealFailure(graphene.ObjectType):
    message = graphene.String()


class ScheduleMealResponse(graphene.Union):
    class Meta:
        types = (ScheduleMealSuccess, ScheduleMealFailure)

class MealNotScheduled(graphene.ObjectType):
    message = graphene.String()

class Item(graphene.ObjectType):
    id = graphene.String()
    name = graphene.String()
    full_meal_quantity = graphene.Int()
    half_meal_quantity = graphene.Int()


class AdminScheduledMeal(graphene.ObjectType):
    date = GQLDateTimeScalar()
    meal_type = graphene.Field(MealTypeEnum)
    items = graphene.List(Item)

class GetScheduledMealByAdminResponse(graphene.Union):
    class Meta:
        types = (AdminScheduledMeal, MealNotScheduled)

class GetScheduledMealByAdminParams(graphene.InputObjectType):
    date = GQLDateTimeScalar()
    meal_type = graphene.Field(MealTypeEnum)

class GetScheduledMealForUserParams(graphene.InputObjectType):
    date = GQLDateTimeScalar()
    user_id = graphene.String()

class UserMeal(graphene.ObjectType):
    meal_type = graphene.Field(MealTypeEnum)
    meal_id = graphene.String()
    meal_preference = graphene.Field(MealTypeEnum)
    items = graphene.Field(Item)

class UserScheduledMeal(graphene.ObjectType):
    date = GQLDateTimeScalar()
    meals = graphene.List(UserMeal)

class GetScheduledMealForUserResponse(graphene.Union):
    class Meta:
        types = (UserScheduledMeal, MealNotScheduled)


class GetMealPreferenceParams(graphene.InputObjectType):
    user_id = graphene.String()
    meal_id = graphene.String()
    meal_type = graphene.Field(MealTypeEnum)

class UserMealStatus(graphene.ObjectType):
    meal_status = graphene.Field(MealStatusEnum)

class GetMealPreferenceResponse(graphene.Union):
    class Meta:
        types = (UserMealStatus, )

