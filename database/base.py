from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase

from settings.config import settings


class Base(DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(
        naming_convention=settings.db.naming_convention,
    )

