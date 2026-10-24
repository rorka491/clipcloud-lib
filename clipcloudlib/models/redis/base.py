from datetime import datetime
from uuid import UUID
from dataclasses import dataclass 


@dataclass
class BaseModel:
    id: UUID
    created_at: datetime

    @classmethod
    def model_name(cls) -> str:
        return cls.__name__.lower()
    
