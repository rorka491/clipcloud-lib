from uuid import UUID
from dataclasses import dataclass
from clipcloudlib.models.redis.base import BaseModel


@dataclass
class Session(BaseModel):
    username: str
    room_uuid: UUID | None = None
    telegram_user_id: str | None = None


# @dataclass
# class WebsocketSession:
#     id: UUID
#     last_active: datetime

#     @classmethod
#     def model_name(cls) -> str:
#         return cls.__name__.lower()





