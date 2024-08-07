from sqlalchemy import select, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column()
    secure_code: Mapped[str] = mapped_column(unique=True)

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r}, secureCode={self.secure_code!r})"


class Message(Base):
    __tablename__ = "message"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    message_content: Mapped[str]
    messages_owner: Mapped[int] = mapped_column(ForeignKey("user.id"))

    def __repr__(self) -> str:
        return f"Message(id={self.id!r}, messageContent={self.message_content!r}, messageOwner={self.messages_owner!r})"
