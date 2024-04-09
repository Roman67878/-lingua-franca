from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Старт"),
            KeyboardButton(text="Помощь"),
            KeyboardButton(text="Платина"),
            KeyboardButton(text="Играть"),

        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    selective=True,
    input_field_placeholder="Выюерите действие из меню"
)

tracks_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Genius", url="https://genius.com/Platina-time-for-fun-lyrics"),
            InlineKeyboardButton(text="Genius", url="https://genius.com/Platina-iwtfy-lyrics")
        ]
    ]
)
