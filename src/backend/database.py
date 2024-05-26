from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class User(db.Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column()
    secure_code: Mapped[str] = mapped_column(unique=True)


class Message(db.Model):
    __tablename__ = "message"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    message_content: Mapped[str]
    messages_owner: Mapped[int] = mapped_column(ForeignKey("user.id"))
