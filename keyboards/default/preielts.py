from aiogram.types import ReplyKeyboardMarkup , KeyboardButton

pielts_button = ReplyKeyboardMarkup(
    keyboard=[
        [

            KeyboardButton(text='Listening Tasks For Pre-IELTS Groups 🎧: '),
            KeyboardButton(text='Reading Tasks 📚 : '),

        ],
        [

            KeyboardButton(text='Speaking topics 🗣 : '),
            KeyboardButton(text='Back'),
        ]
    ],
    resize_keyboard=True
)