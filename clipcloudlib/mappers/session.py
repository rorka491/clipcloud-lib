from clipcloudlib.mappers.base import BaseMapper
from clipcloudlib.models.redis.session import Session
from clipcloudlib.schemas.room import RoomMember


class SessionMapper(BaseMapper[Session]):
    def to_dict(self, obj: Session) -> dict:
        return {
            "id": self.dump_uuid(obj.id),
            "username": obj.username,
            "telegram_user_id": obj.telegram_user_id,
            "room_uuid": self.dump_uuid(obj.room_uuid),
            # "last_active": self.dump_datetime(obj.last_active),
            "created_at": self.dump_datetime(obj.created_at),
        }

    def to_obj(self, data: dict) -> Session:
        return Session( 
            id=self.get_uuid(data, "id"),
            username=self.get(data, "username"),
            room_uuid=self.get_uuid_or_none(data, "room_uuid"),
            telegram_user_id=self.get_or_none(data, "telegram_user_id"),
            # last_active=self.get_datetime(data, "last_active"),
            created_at=self.get_datetime(data, "created_at")
        )

    def sessions_to_members(self, sessions: list[Session], target_session: Session) -> list[RoomMember]:
        members = []
        for s in sessions:
            if target_session.id == s.id:
                is_owner = True
            else: 
                is_owner = False

            member = RoomMember(
                username=s.username,
                session_id=s.id,
                is_owner=is_owner
            )
            members.append(member)
        return members
        

