import uuid

from fastapi_users import schemas, models
from pydantic import EmailStr


# YOU CAN USE BASE OR DICT MODEL

class UserRead(schemas.BaseUser[uuid.UUID]):
    id: models.ID
    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False


class UserCreate(schemas.CreateUpdateDictModel):
    email: EmailStr
    password: str
