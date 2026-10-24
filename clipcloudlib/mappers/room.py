from uuid import UUID
from datetime import datetime
from clipcloudlib.mappers.base import BaseMapper
from clipcloudlib.models.redis.room import Room, RoomAlias


class RoomMapper(BaseMapper[Room]):

    def to_dict(self, obj: Room) -> dict:
        return {
            "id": self.dump_uuid(obj.id),
            "room_code": obj.room_code,
            "created_at": obj.created_at.isoformat(),
            "owner_session_id": self.dump_uuid(obj.owner_session_id)
        }
    
    def to_obj(self, data: dict) -> Room:
        return Room(
            id=UUID(data.get("id")),
            room_code=str(data.get("room_code")),
            created_at=datetime.fromisoformat(data["created_at"]),
            owner_session_id=UUID(data.get("owner_session_id"))
        )

class RoomAliasMapper(BaseMapper[RoomAlias]):
    
    def to_dict(self, obj: RoomAlias) -> dict:
        return {
            "room_code": obj.room_code,
        }

    def to_obj(self, data: dict) -> RoomAlias:
        return RoomAlias(
            room_code=self.get(data, "room_code")
        )