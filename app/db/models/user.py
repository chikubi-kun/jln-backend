
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column as column

from .base_model import BaseModel


class User(BaseModel):
    id: Mapped[int] = column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str]

