from aiogram import types
from aiogram.types import InputFile
from loader import dp,bot


# Echo bot
@dp.message_handler(text='Articles for IELTS Groups')
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/material_tg_bot/140'
    await bot.send_document(chat_id=user_id,document=rasm_manzili)
    rasm_manzili = 'https://t.me/material_tg_bot/141'
    await bot.send_document(chat_id=user_id,document=rasm_manzili)
    rasm_manzili = 'https://t.me/material_tg_bot/139'
    await bot.send_document(chat_id=user_id,document=rasm_manzili)
    rasm_manzili = 'https://t.me/material_tg_bot/138'
    await bot.send_document(chat_id=user_id,document=rasm_manzili)
    rasm_manzili = 'https://t.me/material_tg_bot/137'
    await bot.send_document(chat_id=user_id,document=rasm_manzili)
@dp.message_handler(text='Full Mock Exams For IELTS Groups 🗂 :')
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/material_tg_bot/117'
    await bot.send_document(chat_id=user_id,document=rasm_manzili,caption='Reading Practice')
    rasm_manzili = 'https://t.me/material_tg_bot/128'
    await bot.send_document(chat_id=user_id,document=rasm_manzili,caption='Listening Practice')
    rasm_manzili='https://t.me/material_tg_bot/118'
    await bot.send_audio(chat_id=user_id, audio=rasm_manzili)
    rasm_manzili='https://t.me/material_tg_bot/119'
    await bot.send_audio(chat_id=user_id, audio=rasm_manzili)
    rasm_manzili='https://t.me/material_tg_bot/120'
    await bot.send_audio(chat_id=user_id, audio=rasm_manzili)
    rasm_manzili='https://t.me/material_tg_bot/121'
    await bot.send_audio(chat_id=user_id, audio=rasm_manzili)
    rasm_manzili='https://t.me/material_tg_bot/122'
    await bot.send_audio(chat_id=user_id, audio=rasm_manzili)
    rasm_manzili='https://t.me/material_tg_bot/123'
    await bot.send_audio(chat_id=user_id, audio=rasm_manzili)
    rasm_manzili='https://t.me/material_tg_bot/124'
    await bot.send_audio(chat_id=user_id, audio=rasm_manzili)
    rasm_manzili='https://t.me/material_tg_bot/125'
    await bot.send_audio(chat_id=user_id, audio=rasm_manzili)
    rasm_manzili='https://t.me/material_tg_bot/126'
    await bot.send_audio(chat_id=user_id, audio=rasm_manzili)
    rasm_manzili='https://t.me/material_tg_bot/127'
    await bot.send_audio(chat_id=user_id, audio=rasm_manzili)

