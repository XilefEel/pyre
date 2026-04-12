from dataclasses import dataclass
from typing import (
    NamedTuple,
    Protocol,
    ReadOnly,
    TypedDict,
)

# Type Aliases
# (TypeScript: type Name = string)
type Name = str
type Age = int


# TypedDict
# (TypeScript: interface User { readonly name: Name; readonly age: Age })
class User(TypedDict):
    name: ReadOnly[Name]
    age: ReadOnly[Age]


# NamedTuple
# (Rust: struct Point(f64, f64))
class Point(NamedTuple):
    x: float
    y: float


# Protocol
# (Rust: trait Describable)
class Describable(Protocol):
    def describe(self) -> str: ...


# Dataclass
# (Rust: struct Config { host: String, port: u16 })
@dataclass(frozen=True)
class Config:
    host: str
    port: int = 8080
