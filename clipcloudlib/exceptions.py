class ObjectNotFound(Exception):
    def __init__(self, message: str = "Object not found"):
        super().__init__(message)


class MissingAttributeError(Exception):
    def __init__(self, message: str = "Attribute not found"):
        super().__init__(message)


class CanNotCreateRoomCommand(Exception):
    def __init__(self, message: str = "Can not create room"):
        super().__init__(message)


class InvalidTokenException(Exception):
    
    def __init__(self, message: str = "Invalid token") -> None:
        super().__init__(message)
