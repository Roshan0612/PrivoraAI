

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


from privoraai.db.models.oauth_connection import OAuthConnection
from privoraai.db.models.user import User

__all__ = ["Base", "OAuthConnection", "User"]