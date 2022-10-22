from aiogram.types import ReplyKeyboardMarkup , KeyboardButton

ielts_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Articles for IELTS Groups"),
            KeyboardButton(text='Back Menu'),
        ],
        [
            KeyboardButton(text='Full Mock Exams For IELTS Groups 🗂 : '),
        ]
    ],
    resize_keyboard=True
)