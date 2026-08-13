from typing import Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict


class SessionSchema(BaseModel):
    id: UUID
    username: str
    room_uuid: Optional[UUID] = None
    telegram_user_id: Optional[int] = None
    model_config = ConfigDict(from_attributes=True)


class SessionSchemaAccessToken(BaseModel):
    id: UUID
    username: str
    room_uuid: Optional[UUID] = None
    access_token: str

    model_config = ConfigDict(from_attributes=True)
