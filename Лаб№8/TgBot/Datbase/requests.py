from Datbase.things import async_session
from Datbase.things import User, Song

from sqlalchemy import select


async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()


async def get_song(item_id):
    async with async_session() as session:
        return await session.scalar(select(Song).where(Song.id == item_id))



