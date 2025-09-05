from itsdangerous import BadSignature, SignatureExpired, TimestampSigner

from security.config import settings

signer = TimestampSigner(settings.SECRET_KEY)

COOKIE_NAME = "session_token"


def create_signed_cookie(user_id: str) -> str:
    return signer.sign(user_id.encode()).decode()


def verify_signed_cookie(token: str, max_age: int = 3600) -> str | None:
    try:
        data = signer.unsign(token, max_age=max_age)
        return data.decode()
    except SignatureExpired:
        return None  # если подпись была верна, но устарела
    except BadSignature:
        return None  # если подпись неверная
