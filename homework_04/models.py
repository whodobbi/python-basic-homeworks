"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os

from sqlalchemy import Column, Integer, String, Text, create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declared_attr, relationship

PG_CONN_URI = (
    os.environ.get("SQLALCHEMY_PG_CONN_URI")
    or "postgresql+asyncpg://postgres:password@localhost/postgres"
)

engine = create_engine(
    url=PG_CONN_URI,
    echo=False,
)

async_engine = create_async_engine(
    url=PG_CONN_URI, echo=False,
)


class Base:
    id = Column(Integer, primary_key=True)

    @declared_attr
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"


Base = declarative_base(cls=Base)
Session = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class User(Base):
    name = Column(String(30), nullable=False)
    username = Column(String(30), nullable=False)
    email = Column(String(50), nullable=False)

    posts = relationship(
        "Post",
        back_populates="user",
        uselist=True,
    )

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            f"User("
            f" name={self.name},"
            f" username={self.username!r},"
            f" email={self.email!r}"
        )


class Post(Base):
    user_id = Column(Integer, primary_key=True)
    title = Column(
        String(100),
        nullable=False,
        default="",
        server_default="",
    )
    body = Column(Text, nullable=False)

    posts = relationship(
        "User",
        back_populates="posts",
        uselist=False,
    )

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            f"Post(id={self.id}, "
            f"(title={self.title!r}), "
            f"body={self.body!r}, "
        )
