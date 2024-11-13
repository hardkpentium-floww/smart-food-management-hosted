import factory

from meals.interactors.storage_interfaces.storage_interface import AccessTokenDTO, RefreshTokenDTO


class AccessTokenDTOFactory(factory.Factory):
    class Meta:
        model = AccessTokenDTO

    user_id = factory.Faker("uuid4")
    token = factory.Faker("uuid4")
    application_id = factory.Faker("random_int", min=1, max=10000)
    expires = factory.Faker("date")
    scope = factory.Faker("name")



class RefreshTokenDTOFactory(factory.Factory):
    class Meta:
        model = RefreshTokenDTO

    user_id = factory.Faker("uuid4")
    refresh_token = factory.Faker("uuid4")
    application_id = factory.Faker("random_int", min=1, max=10000)
    access_token_id = factory.Faker("random_int", min=1, max=10000)