import graphene

class TypeEnum(graphene.Enum):
    BREAKFAST = "BREAKFAST"
    LUNCH = "LUNCH"
    DINNER = "DINNER"

class FoodItemCategoryEnum(graphene.Enum):
    RICE = "RICE"
    PANCAKE = "PANCAKE"
    BEVERAGES = "BEVERAGES"

class BaseSizeUnitEnum(graphene.Enum):
    KG = "KG"
    PISCES = "PISCES"
    LITTERS = "LITTERS"

class ServingSizeUnitEnum(graphene.Enum):
    PISCES = "PISCES"
    LADDLE = "LADDLE"
    GLASS = "GLASS"


class MealTypeEnum(graphene.Enum):
    FULL= "FULL"
    HALF= "HALF"
    CUSTOM= "CUSTOM"
