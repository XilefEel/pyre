from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from db.session import get_session
from errors import AppError
from models.user import User
from schemas.user import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=list[UserResponse])
def list_users(session: Session = Depends(get_session)) -> list[User]:
    users = session.exec(select(User)).all()
    return list(users)


@router.post("/", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate, session: Session = Depends(get_session)) -> User:
    existing = session.exec(select(User).where(User.email == user.email)).first()
    if existing:
        raise HTTPException(status_code=409, detail=AppError.ALREADY_EXISTS)

    db_user = User(name=user.name, email=user.email)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, session: Session = Depends(get_session)) -> User:
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail=AppError.NOT_FOUND)
    return user
