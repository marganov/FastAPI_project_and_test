from hashlib import sha256
from uuid import uuid4

from fastapi import APIRouter, HTTPException, Request, Response, status

from data.data_base import db
from models.user_model import User
from security.cookies import (
    COOKIE_NAME,
    create_signed_cookie,
    set_session_cookie,
    verify_signed_cookie,
)

router = APIRouter()


@router.post("/login")
def login(user: User, response: Response):
    # хэшируем пароль
    user.password = sha256(user.password.encode()).hexdigest()
    # проверка юзера в базе
    if user in db:
        user_id = str(uuid4())  # генерим UUID
        session_token = create_signed_cookie(user_id)

        set_session_cookie(response, session_token)
        return {"message": "Login successful", "user_id": user_id}

    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")


@router.get("/profile")
def get_profile(request: Request):
    session_token = request.cookies.get(COOKIE_NAME)

    if not session_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized"
        )

    user_id = verify_signed_cookie(session_token)

    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized"
        )

    return {"message": "Welcome!", "user_id": user_id}


@router.get("/user")
def get_user(request: Request):
    session_token = request.cookies.get(COOKIE_NAME, "invalid_session_token")
    return {"session_token": session_token}
