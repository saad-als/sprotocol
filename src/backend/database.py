from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    secure_code: Mapped[str] = mapped_column(unique=True)


class Message(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    message_content: Mapped[str]
