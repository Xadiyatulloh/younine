from aiogram import types
from aiogram.types import InputFile
from loader import dp,bot


# Echo bot
@dp.message_handler(text='Essential 4000 words  📚:')
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/material_tg_bot/14?single'
    await bot.send_document(chat_id=user_id,document=rasm_manzili)

@dp.message_handler(text='Tenses For Elementary Groups 🕚:')
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = ''
    await bot.send_message(chat_id=user_id, text='https://t.me/tencesyounineacademy  You can get all tences there')
