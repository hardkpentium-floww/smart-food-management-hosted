from datetime import datetime

from meals.interactors.storage_interfaces.storage_interface import StorageInterface, AccessTokenDTO, RefreshTokenDTO, \
    ItemDTO, ScheduleMealDTO, MealItemDTO, AdminScheduledMealDTO
import uuid

from meals_gql.meal.types.types import AdminScheduledMeal


class StorageImplementation(StorageInterface):

    def login(self, username: str, user_id: str, password: str):
        from datetime import datetime, timedelta
        from meals.interactors.storage_interfaces.storage_interface import AccessTokenDTO, RefreshTokenDTO
        access_token_str = str(uuid.uuid4())
        refresh_token_str = str(uuid.uuid4())
        expires = datetime.now() + timedelta(days=1)
        application_id = self.get_application_id(application_name="meals")
        is_admin = self.check_admin(user_id=user_id)

        access_token_dto = AccessTokenDTO(
            user_id=user_id,
            token=access_token_str,
            application_id=application_id,
            expires=expires,
            scope="read write",
        )

        access_token = self.create_access_token(access_token_dto=access_token_dto)

        refresh_token_dto = RefreshTokenDTO(
            user_id=user_id,
            refresh_token=refresh_token_str,
            access_token_id=access_token.id,
            application_id=application_id
        )

        refresh_token = self.create_refresh_token(refresh_token_dto=refresh_token_dto)

        user_login_response = {
                    "is_admin": is_admin,
                    "access_token": access_token_str,
                    "expires_in": expires,
                    "token_type": "Bearer",
                    "scope": "read write",
                    "refresh_token": refresh_token_str
                }

        return user_login_response

    def logout(self, user_id: str, access_token:str):
        from oauth2_provider.models import AccessToken, RefreshToken
        access_token = AccessToken.objects.get(token=access_token)
        refresh_token = RefreshToken.objects.get(access_token=access_token)
        self.expire_access_token(access_token_id=access_token.id)
        self.revoke_refresh_token(refresh_token_id=refresh_token.id)

    def check_admin(self, user_id: str):
        from meals.models.user import User
        check = User.objects.get(id=user_id).is_admin
        return check

    def get_application_id(self, application_name: str):
        from oauth2_provider.models import Application
        return Application.objects.get(name=application_name).id


    def expire_access_token(self, access_token_id: str):
        from oauth2_provider.models import AccessToken
        from datetime import datetime
        access_token = AccessToken.objects.get(id=access_token_id)
        access_token.expires = datetime.now()
        access_token.save()
        return access_token

    def get_items(self,offset:int,limit:int):
        from meals.models.item import Item
        items = Item.objects.all()
        items = items[offset:offset+limit]

        item_dtos = [
            ItemDTO(
                id=item.id,
                name=item.name,
                category=item.category,
                base_size_unit=item.base_size_unit,
                serving_size_unit=item.serving_size_unit
            ) for item in items
        ]

        return item_dtos



    def revoke_refresh_token(self, refresh_token_id: str):
        from oauth2_provider.models import RefreshToken
        from datetime import datetime
        refresh_token = RefreshToken.objects.get(id=refresh_token_id)
        refresh_token.revoked = datetime.now()
        refresh_token.save()
        return refresh_token

    def get_user_acc(self,user_id:str):
        from ib_users.models import UserAccount
        user = UserAccount.objects.get(user_id=user_id)
        return user

    def get_user(self, username:str):
        from meals.models.user import  User
        user = User.objects.filter(name=username).first()
        return user

    def create_access_token(self, access_token_dto: AccessTokenDTO):
        from oauth2_provider.models import AccessToken
        access_token = AccessToken.objects.create(
            user_id = access_token_dto.user_id,
            token = access_token_dto.token,
            application_id = access_token_dto.application_id,
            expires = access_token_dto.expires,
            scope = access_token_dto.scope
        )

        return access_token

    def schedule_meal(self, schedule_meal_dto: ScheduleMealDTO):
        from meals.models.meal import Meal
        from meals.models.meal_item import MealItem
        meal = Meal.objects.create(
            id = str(uuid.uuid4()),
            date= schedule_meal_dto.date,
            meal_type= schedule_meal_dto.meal_type,
        )

        for i in range(len(schedule_meal_dto.item_ids)):
            meal_item = MealItem.objects.create(
                id = str(uuid.uuid4()),
                meal_id = meal.id,
                item_id = schedule_meal_dto.item_ids[i],
                full_meal_qty = schedule_meal_dto.full_meal_quantities[i],
                half_meal_qty = schedule_meal_dto.half_meal_quantities[i],
            )

        return meal.id


    def create_refresh_token(self, refresh_token_dto: RefreshTokenDTO):
        from oauth2_provider.models import RefreshToken
        refresh_token = RefreshToken.objects.create(
            user_id = refresh_token_dto.user_id,
            token = refresh_token_dto.refresh_token,
            application_id = refresh_token_dto.application_id,
            access_token_id = refresh_token_dto.access_token_id
        )
        return refresh_token


    def validate_item_ids(self, item_ids:[int]):
        from meals.models.item import Item

        for i in range(len(item_ids)):
            check = Item.objects.filter(id=item_ids[i]).exists()
            if not check:
                return False

        return True


    def validate_quantities(self, full_meal_quantities:[int], half_meal_quantities:[int]):
        for i in range(len(full_meal_quantities)):
            if full_meal_quantities[i] < 0 or half_meal_quantities[i] < 0:
                return False

        return True

    def validate_date(self, date:datetime):
        if date < datetime.now():
            return False

        return True


    def get_scheduled_meal_by_admin(self, date: datetime, meal_type:str):
        from meals.models.meal import Meal
        from meals.models.meal_item import MealItem
        meal =  Meal.objects.get(date=date, meal_type=meal_type)

        meal_items = MealItem.objects.filter(meal_id=meal.id)
        item_dtos = [
            MealItemDTO(
                id = meal_item.id,
                name = meal_item.item.name,
                full_meal_qty = meal_item.full_meal_qty,
                half_meal_qty = meal_item.half_meal_qty
            ) for meal_item in meal_items
        ]
        meal_dto = AdminScheduledMealDTO(
                date = date,
                meal_type = meal_type,
                items = item_dtos
            )


        return meal_dto