from aiogram.types import ReplyKeyboardMarkup , KeyboardButton

menu_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Choose your level 📈 :"),
            KeyboardButton(text='Adminga Yozish 📤')
        ]
    ],
    resize_keyboard=True
)

tasdiqlash_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Tasdiqlash ✔️"),
            KeyboardButton(text="Bekor Qilish ❌️"),

        ]
    ],
    resize_keyboard=True
)