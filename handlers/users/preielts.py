from aiogram import types
from aiogram.types import InputFile
from loader import dp,bot


# Echo bot
@dp.message_handler(text='Listening Tasks For Pre-IELTS Groups 🎧:')
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/material_tg_bot/105'
    await bot.send_document(chat_id=user_id,document=rasm_manzili)
    rasm_manzili = 'https://t.me/material_tg_bot/68?single'
    await bot.send_audio(chat_id=user_id,audio=rasm_manzili)
    rasm_manzili = 'https://t.me/material_tg_bot/69?single'
    await bot.send_audio(chat_id=user_id,audio=rasm_manzili)
    rasm_manzili = 'https://t.me/material_tg_bot/70?single'
    await bot.send_audio(chat_id=user_id,audio=rasm_manzili)
    rasm_manzili = 'https://t.me/material_tg_bot/72?single'
    await bot.send_audio(chat_id=user_id,audio=rasm_manzili)
    rasm_manzili = 'https://t.me/material_tg_bot/73?single'
    await bot.send_audio(chat_id=user_id,audio=rasm_manzili)
    rasm_manzili = 'https://t.me/material_tg_bot/74?single'
    await bot.send_audio(chat_id=user_id,audio=rasm_manzili)
    rasm_manzili = 'https://t.me/material_tg_bot/75?single'
    await bot.send_audio(chat_id=user_id,audio=rasm_manzili)
    rasm_manzili = 'https://t.me/material_tg_bot/76?single'
    await bot.send_audio(chat_id=user_id,audio=rasm_manzili)
    rasm_manzili = 'https://t.me/material_tg_bot/77?single'
    await bot.send_audio(chat_id=user_id,audio=rasm_manzili)
    rasm_manzili = 'https://t.me/material_tg_bot/78?single'
    await bot.send_audio(chat_id=user_id,audio=rasm_manzili)
    rasm_manzili = 'https://t.me/material_tg_bot/79?single'
    await bot.send_audio(chat_id=user_id,audio=rasm_manzili)
    rasm_manzili = 'https://t.me/material_tg_bot/80?single'
    await bot.send_audio(chat_id=user_id,audio=rasm_manzili)
    rasm_manzili = 'https://t.me/material_tg_bot/81?single'
    await bot.send_audio(chat_id=user_id,audio=rasm_manzili)

@dp.message_handler(text='Speaking topics 🗣 :')
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/material_tg_bot/106'
    await bot.send_document(chat_id=user_id,document=rasm_manzili,caption="You can get all Speaking Topics in this app")

@dp.message_handler(text='Reading Tasks 📚 :')
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/material_tg_bot/107?single'
    await bot.send_document(chat_id=user_id,document=rasm_manzili,caption='Reading Book')
    rasm_manzili = 'https://t.me/material_tg_bot/108?single'
    await bot.send_document(chat_id=user_id,document=rasm_manzili,caption='Reading Book')