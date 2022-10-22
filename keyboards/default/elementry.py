from aiogram.types import ReplyKeyboardMarkup , KeyboardButton

elementary_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Essential 4000 words  📚: "),
            KeyboardButton(text='Tenses For Elementary Groups 🕚: '),


        ],
        [
            KeyboardButton(text='Back ◀')
        ]
    ],
    resize_keyboard=True
)