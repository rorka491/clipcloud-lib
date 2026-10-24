from uuid import UUID
from pydantic import BaseModel, ConfigDict


class FileSchema(BaseModel):
    id: UUID
    file_path: str
    file_name: str

    model_config = ConfigDict(from_attributes=True)

