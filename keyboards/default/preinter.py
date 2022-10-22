from aiogram.types import ReplyKeyboardMarkup , KeyboardButton

intermediate_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Books for Pre-Intermediate Groups  📚: "),
            KeyboardButton(text='Listening Tasks For Pre-Intermediate Groups 🎧: '),

        ],
        [
            
            KeyboardButton(text='Back ◀◀'),
        ]
    ],
    resize_keyboard=True
)