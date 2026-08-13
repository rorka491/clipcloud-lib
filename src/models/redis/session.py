from typing import Annotated, Optional
from uuid import UUID
from dataclasses import dataclass
from src.required import Required
from src.exceptions import MissingAttributeError
from src.models.redis.base import BaseModel


@dataclass
class Session(BaseModel):
    username: str
    _room_uuid: UUID | None = None
    _telegram_user_id: int | None = None

    @property
    def room_uuid(self) -> UUID:
        if self._room_uuid is None:
            raise MissingAttributeError(
                "The user has not joined the room"
            )
        return self._room_uuid

    @room_uuid.setter
    def room_uuid(self, value: UUID | None) -> None:
        self._room_uuid = value

    @property
    def telegram_user_id(self) -> int:
        if self._telegram_user_id is None:
            raise MissingAttributeError("The user does not have telegram_user_id")
        return self._telegram_user_id

    @telegram_user_id.setter
    def telegram_user_id(self, value: int | None=None) -> None:
        self._telegram_user_id = value
