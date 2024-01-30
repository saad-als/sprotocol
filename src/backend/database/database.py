from sqlalchemy import create_engine, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

engine = create_engine(
    "sqlite+pysqlite:///src//backend//database//db.sqlite3", echo=True)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    code = mapped_column(ForeignKey("secure_codes.id"))

    def __repr__(self) -> str:
        return f'username: ({self.name})\n id = [ {self.id} ]'


class Message(Base):
    __tablename__ = "messages"

    message_id: Mapped[int] = mapped_column(primary_key=True)
    message_text: Mapped[str] = mapped_column(String)
    owner = mapped_column(ForeignKey("users.id"))

    def __repr__(self) -> str:
        return f'Message from ({self.owner}) message id = {self.message_id}\n message =[\n {self.message_text} \n]'


class Codes(Base):
    __tablename__ = "secure_codes"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    owner = mapped_column(ForeignKey("users.id"))

    def __repr__(self) -> str:
        return f'owner ({self.owner})\n CODE = [ {self.id} ]'


class Manage:

    def send_to_db(self, data):
        with engine.connect() as conn:
            conn.execute(data)
            conn.commit()


Base.metadata.create_all(engine)
