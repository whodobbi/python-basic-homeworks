"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

import asyncio

from sqlalchemy.ext.asyncio import AsyncSession

from jsonplaceholder_requests import (
    fetch_json,
    USERS_DATA_URL,
    POSTS_DATA_URL,
)
from models import Base, User, Post, engine, Session, async_engine


def create_tables():
    Base.metadata.create_all(bind=engine)


def create_users(
    session: AsyncSession,
    users_data: list[dict],
):
    for user in users_data:
        user = User(
            id=user["id"],
            name=user["name"],
            username=user["username"],
            email=user["email"],
        )
        session.add(user)


def create_posts(
    session: AsyncSession,
    posts_datta: list[dict],
):
    for post in posts_datta:
        post = Post(
            user_id=post["id"],
            title=post["title"],
            body=post["body"],
        )
        session.add(post)


async def async_main():
    async with Session() as session:
        async with async_engine.begin() as connection:
            await connection.run_sync(create_tables)
        async with async_engine.begin() as connection:
            users_data: list[dict]
            posts_data: list[dict]
            users_data, posts_data = await asyncio.gather(
                fetch_json(USERS_DATA_URL),
                fetch_json(POSTS_DATA_URL),
            )
            await connection.run_sync(
                create_users,
                session=session,
                users_data=users_data,
            )
            await connection.run_sync(
                create_posts,
                session=session,
                posts_data=posts_data,
            )
            await session.commit()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
