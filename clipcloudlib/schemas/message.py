from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, model_validator, Field, ConfigDict

from clipcloudlib.schemas.file import FileSchema




class MessageSchema(BaseModel):
    id: UUID
    created_at: datetime
    text: str | None
    username: str
    session_id: UUID
    file: FileSchema | None = None


    model_config = ConfigDict(from_attributes=True)


class MessageCreateSchema(BaseModel):
    text: str | None = Field(default=None, max_length=5000)
    file_id: UUID | None = None

    @model_validator(mode="after")
    def validate_content(self):
        if not self.text and not self.file_id:
            raise ValueError("Either 'text' or 'file_id' must be provided.")
        return self


class MessageUpdateSchema(BaseModel):
    text: str

    