from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, ConfigDict


class RoomSchema(BaseModel):
    id: UUID
    room_code: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class RoomMember(BaseModel):
    session_id: UUID
    username: str
    is_owner: bool = False