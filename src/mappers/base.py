from datetime import datetime
from uuid import UUID
import json
from typing import Any, Generic, TypeVar
from abc import abstractmethod, ABC


M = TypeVar("M")


class BaseMapper(Generic[M], ABC):
    
    @abstractmethod
    def to_dict(self, obj: M) -> dict: ...

    @abstractmethod
    def to_obj(self, data: dict) -> M: ...

    @staticmethod
    def get(data: dict, key: str) -> Any:
        value = data.get(key)
        if not value:
            raise ValueError(f"Missing or empty field: {key}")
        return value
    
    @staticmethod
    def get_or_none(data: dict, key: str) -> str | None:
        value = data.get(key)
        return value if value else None

    
    @staticmethod
    def get_uuid(data: dict, key: str) -> UUID:
        value = data.get(key)
        if not value:
            raise ValueError(f"Missing or empty UUID field: {key}")
        return UUID(value)
    
    @staticmethod
    def get_uuid_or_none(data: dict, key: str) -> UUID | None:
        value = data.get(key)
        return UUID(value) if value else None

    @staticmethod
    def get_datetime(data: dict, key: str) -> datetime:
        value = datetime.fromisoformat(data[key])
        if not value:
            raise ValueError(f"Missing or empty datetime field: {key}")
        return value

    @staticmethod
    def dump_uuid(value: UUID | None) -> str | None:
        return str(value) if value else None

    @staticmethod
    def dump_datetime(value: datetime) -> str:
        return value.isoformat()
    
    @staticmethod
    def clean_dict(data: dict) -> dict:
        return {k: v for k, v in data.items() if v is not None}