from aiogram.types import ReplyKeyboardMarkup , KeyboardButton

level_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Beginner"),
            KeyboardButton(text='Elementary'),
            KeyboardButton(text='Pre Intermediate')
        ],
        [
            KeyboardButton(text='Pre IELTS'),
            KeyboardButton(text='IELTS'),
            KeyboardButton(text='Back 🔙')
        ]
    ],
    resize_keyboard=True
)