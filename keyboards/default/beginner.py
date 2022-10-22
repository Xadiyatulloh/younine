from aiogram.types import ReplyKeyboardMarkup , KeyboardButton

beginner_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Present Simple'),
            KeyboardButton(text='Present Continuous')
        ],
        [
            KeyboardButton(text='Past Simple'),
            KeyboardButton(text='Future Simple'),
            KeyboardButton(text='Back 🔙🔙')
        ]
    ],
    resize_keyboard=True
)