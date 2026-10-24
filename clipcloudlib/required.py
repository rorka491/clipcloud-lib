from clipcloudlib.exceptions import MissingAttributeError


class Required:

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self

        value = instance.__dict__.get(self.name)
        if value is None:
            raise MissingAttributeError(
                f"{self.name} is not set"
            )

        return value

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value