from aiogram import F, Router, Bot
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.enums.dice_emoji import DiceEmoji

import sqlite3

import helpers.keyboard as kb

router = Router()
bot = Bot(token="6904015579:AAHKEbRngR1R0ID8Kv1wD78kYPBT09gQE7w")


@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет, балда!!", reply_markup=kb.main_kb)
    await message.reply("Bless")


@router.message(Command('help'))
async def help_user(message: Message):
    await message.answer("Что нужно??")


@router.message(Command('play'))
async def play_games(message: Message):
    game = await message.answer_dice(DiceEmoji.BASKETBALL)
    print(game.dice.value)


@router.message(Command('tracks'))
async def track(message: Message):
    await message.answer("Треки: ", reply_markup=kb.tracks_kb)


