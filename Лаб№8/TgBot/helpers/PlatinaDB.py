import asyncio
import sqlite3

import os
import tracemalloc
tracemalloc.start()

conn = sqlite3.connect('songs.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS songs (
        id INTEGER PRIMARY KEY,
        text TEXT
    )
''')
conn.commit()


async def add_song_from_file(file_path: str):
    if not file_path.endswith('.txt'):
        print("Invalid file format. Please provide a .txt file.")
    if not os.path.exists(file_path):
        print("File not found.")
    with open(file_path, 'r', encoding='cp1251') as file:
        text = file.read()
        cursor.execute('INSERT INTO songs (text) VALUES (?)', (text,))
        conn.commit()


# Функция для получения текста песни по его номеру
async def get_song_text(song_id: int):
    cursor.execute('SELECT text FROM songs WHERE id = ?', (song_id,))
    row = cursor.fetchone()

    if row:
        return row[0]
    else:
        return "Песня с таким номером не найдена"


# @dp.message(Command('get_song'))
# async def get_song(message: types.Message):
#    await message.answer("Введите номер песни:")


# @dp.message()
# async def process_message(message: Message):
    try:
        song_id = int(message.text)
        song_text = await get_song_text(song_id)
        await message.answer(song_text)
    except ValueError:
        await message.answer("Некорректный номер песни")


# async def main():
#    await dp.start_polling(bot)

# if __name__ == '__main__':
#    asyncio.run(main())


async def main():
    await add_song_from_file(file_path='C:/Users/localadm/PycharmProjects/TgBot/helpers/platina2.txt')

asyncio.run(main())

get_song_text(song_id=1)




