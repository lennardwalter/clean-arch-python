from typing import Union, TypeGuard


class Ok[T]:
    __match_args__ = ("value",)
    __slots__ = ["value"]

    value: T

    def __init__(self, value: T) -> None:
        self.value = value

    def is_ok(self) -> bool:
        return True

    def is_err(self) -> bool:
        return False


class Err[E]:
    __match_args__ = ("value",)
    __slots__ = ["value"]

    value: E

    def __init__(self, value: E) -> None:
        self.value = value

    def is_ok(self) -> bool:
        return False

    def is_err(self) -> bool:
        return True


type Result[T, E] = Union[Ok[T], Err[E]]


def is_ok[T, E](result: Result[T, E]) -> TypeGuard[Ok[T]]:
    return result.is_ok()


def is_err[T, E](result: Result[T, E]) -> TypeGuard[Err[E]]:
    return result.is_err()


__all__ = ["Result", "Ok", "Err", "is_ok", "is_err"]
