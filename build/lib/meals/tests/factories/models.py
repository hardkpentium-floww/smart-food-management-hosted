import factory
from ib_users.models import UserAccount
from oauth2_provider.models import Application, AccessToken, RefreshToken

from meals.models.user import User

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    id = factory.Faker("uuid4")
    name = factory.Faker('name')
    in_campus = factory.Faker('boolean')


class UserAccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserAccount

    user_id = factory.Faker("uuid4")
    username = factory.Faker("name")

class ApplicationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Application

    id = factory.Faker("random_int", min=1, max=10000)
    user_id = factory.Faker("uuid4")
    name = factory.Faker("name")


class AccessTokenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AccessToken

    user_id = factory.Faker("uuid4")
    token = factory.Faker("uuid4")
    application_id = factory.Faker("uuid4")
    expires = factory.Faker("random_int", min=1000, max=10000),
    scope = factory.Faker("name")


class RefreshTokenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RefreshToken

    user_id = factory.Faker("uuid4")
    token = factory.Faker("uuid4")
    application_id = factory.Faker("uuid4")
    access_token_id = factory.Faker("uuid4")

