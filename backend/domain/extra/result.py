from __future__ import annotations

from typing import Union


class Ok[T]:
    __match_args__ = ("value",)
    __slots__ = ["value"]

    value: T

    def __init__(self, value: T) -> None:
        self.value = value


class Err[E]:
    __match_args__ = ("value",)
    __slots__ = ["value"]

    value: E

    def __init__(self, value: E) -> None:
        self.value = value


type Result[T, E] = Union[Ok[T], Err[E]]


__all__ = ["Result", "Ok", "Err"]
