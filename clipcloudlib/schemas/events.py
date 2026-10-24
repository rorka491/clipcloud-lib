from typing import Annotated, ClassVar, Self, Union, Literal
from uuid import UUID
from pydantic import Field, RootModel, BaseModel, model_validator
from clipcloudlib.enums import EventTypeEnum, EventTargetEnum


class EventRoute(BaseModel):
    target: EventTargetEnum
    session_id: UUID | None = None
    room_id: UUID | None = None

    __target_required: ClassVar[dict[EventTargetEnum, tuple[str, ...]]] = {
        EventTargetEnum.ROOM: ("room_id",),
        EventTargetEnum.ROOM_EXCEPT: ("session_id", "room_id"),
        EventTargetEnum.USER: ("session_id",)
    }

    @model_validator(mode="after")
    def validate_fields(self,) -> Self:
        required_fields = self.__target_required.get(self.target, ())
        for field in required_fields:
            if getattr(self, field) is None:
                raise ValueError(f"Target is {self.target}: {field} not provided")
        return self


class ToggleRoomAccessStatusEvent(BaseModel):
    type: Literal[EventTypeEnum.TOGGLE_ROOM_ACCESS] = EventTypeEnum.TOGGLE_ROOM_ACCESS
    payload: dict


class DeleteMessageEvent(BaseModel):
    type: Literal[EventTypeEnum.DELETE_MESSAGE] = EventTypeEnum.DELETE_MESSAGE
    payload: dict


class ChangeMessageEvent(BaseModel):
    type: Literal[EventTypeEnum.CHANGE_MESSAGE] = EventTypeEnum.CHANGE_MESSAGE
    payload: dict


class SetUsernameEvent(BaseModel):
    type: Literal[EventTypeEnum.SET_USERNAME] = EventTypeEnum.SET_USERNAME
    payload: dict


class PromoEvent(BaseModel):
    type: Literal[EventTypeEnum.PROMO] = EventTypeEnum.PROMO
    payload: dict


class QuitRoomEvent(BaseModel):
    type: Literal[EventTypeEnum.QUIT_ROOM] = EventTypeEnum.QUIT_ROOM
    payload: dict


class JoinRoomEvent(BaseModel):
    type: Literal[EventTypeEnum.USER_JOIN_THE_ROOM] = EventTypeEnum.USER_JOIN_THE_ROOM
    payload: dict


class PairingEvent(BaseModel):
    type: Literal[EventTypeEnum.PAIRING] = EventTypeEnum.PAIRING
    payload: dict


class MessageEvent(BaseModel):
    type: Literal[EventTypeEnum.MESSAGE] = EventTypeEnum.MESSAGE
    payload: dict


class ChangeRoomCodeEvent(BaseModel):
    type: Literal[EventTypeEnum.CHANGE_ROOM_CODE] = EventTypeEnum.CHANGE_ROOM_CODE
    payload: dict


class UserTypingEvent(BaseModel):
    type: Literal[EventTypeEnum.USER_TYPING] = EventTypeEnum.USER_TYPING
    payload: dict


class UserOnlineEvent(BaseModel):
    type: Literal[EventTypeEnum.USER_ONLINE] = EventTypeEnum.USER_ONLINE
    payload: dict


class UserOfflineEvent(BaseModel):
    type: Literal[EventTypeEnum.USER_OFFLINE] = EventTypeEnum.USER_OFFLINE
    payload: dict




EventUnion = Annotated[
    Union[
        ToggleRoomAccessStatusEvent,
        DeleteMessageEvent,
        ChangeMessageEvent,
        SetUsernameEvent,
        PromoEvent,
        QuitRoomEvent,
        JoinRoomEvent,
        PairingEvent,
        MessageEvent,
        ChangeRoomCodeEvent,
        UserTypingEvent,
        UserOnlineEvent,
        UserOfflineEvent,
    ],
    Field(discriminator="type"),
]


class EventSchema(RootModel[EventUnion]): ...