from enum import StrEnum, auto


class AppError(StrEnum):
    NOT_FOUND = auto()
    ALREADY_EXISTS = auto()
    INVALID_INPUT = auto()
