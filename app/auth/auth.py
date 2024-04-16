from fastapi_users.authentication import CookieTransport, JWTStrategy, AuthenticationBackend, BearerTransport

from app.config import SECRET

cookie_transport = CookieTransport(cookie_max_age=36000, cookie_name="JWT")
# cookie_transport = BearerTransport("/auth/jwt/login")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
