from datetime import datetime
from dataclasses import dataclass
from uuid import UUID
from clipcloudlib.models.redis.base import BaseModel


@dataclass
class Room(BaseModel):
    room_code: str
    owner_session_id: UUID


@dataclass
class RoomAlias():
    room_code: str
