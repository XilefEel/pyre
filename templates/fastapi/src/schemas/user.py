from sqlmodel import SQLModel


class UserCreate(SQLModel):
    name: str
    email: str


class UserResponse(SQLModel):
    id: int
    name: str
    email: str
