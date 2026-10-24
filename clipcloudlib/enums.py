from enum import StrEnum


class EventTypeEnum(StrEnum):
    TOGGLE_ROOM_ACCESS = "toggle_room_access"
    DELETE_MESSAGE = "delete_message"
    MESSAGE = "message"
    PAIRING = "pairing"
    QUIT_ROOM = "quit_room"
    USER_JOIN_THE_ROOM = "user_join_the_room"
    CHANGE_ROOM_CODE = "change_room_code"
    USER_TYPING = "user_typing"
    PROMO = "promo"
    SET_USERNAME = "set_username"
    CHANGE_MESSAGE = "change_message"
    USER_ONLINE = "user_online"
    USER_OFFLINE = "user_offline"

class EventTargetEnum(StrEnum):
    ROOM = "room"
    ROOM_EXCEPT = "room_except"
    USER = "user"
    ALL = "all"