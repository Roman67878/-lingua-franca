from aiogram import F, Router, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.enums.dice_emoji import DiceEmoji

import sqlite3

from aiosqlite import cursor

import helpers.keyboard as kb

import Datbase.requests as rq

router = Router()
bot = Bot(token="6904015579:AAHKEbRngR1R0ID8Kv1wD78kYPBT09gQE7w")


@router.message(CommandStart())
async def start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer("Привет, балда!!", reply_markup=kb.main_kb)
    await message.reply("Bless")



@router.message(Command('help'))
async def help_user(message: Message):
    await message.answer("Что нужно??")


@router.message(Command('play'))
async def play_games(message: Message):
    game = await message.answer_dice(DiceEmoji.BASKETBALL or DiceEmoji.DICE or DiceEmoji.BOWLING)
    print(game.dice.value)


@router.message(Command('tracks'))
async def track(message: Message):
    await message.answer("Треки: ", reply_markup=kb.tracks_kb)


@router.callback_query(F.data.startswith('item_'))
async def category(callback: CallbackQuery):
    item_data = await rq.get_item(callback.data.split('_')[1])
    await callback.answer('Вы выбрали трек')
    await callback.message.answer(f'Название: {item_data.name}\nТекст: {item_data.song_text}$')




