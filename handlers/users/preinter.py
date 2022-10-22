from aiogram import types
from aiogram.types import InputFile
from loader import dp,bot


# Echo bot
@dp.message_handler(text='Books for Pre-Intermediate Groups  📚:')
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/material_tg_bot/26'
    await bot.send_document(chat_id=user_id,document=rasm_manzili)

@dp.message_handler(text='Listening Tasks For Pre-Intermediate Groups 🎧:')
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili='https://t.me/material_tg_bot/27'
    await bot.send_document(chat_id=user_id, document=rasm_manzili)
    rasm_manzili = 'https://t.me/material_tg_bot/28'
    await bot.send_audio(chat_id=user_id,audio=rasm_manzili)
    rasm_manzili='https://t.me/material_tg_bot/29'
    await bot.send_audio(chat_id=user_id, audio=rasm_manzili)
    rasm_manzili='https://t.me/material_tg_bot/30'
    await bot.send_audio(chat_id=user_id, audio=rasm_manzili)
    rasm_manzili='https://t.me/material_tg_bot/31'
    await bot.send_audio(chat_id=user_id, audio=rasm_manzili)
    rasm_manzili='https://t.me/material_tg_bot/32'
    await bot.send_audio(chat_id=user_id, audio=rasm_manzili)
    rasm_manzili='https://t.me/material_tg_bot/33'
    await bot.send_audio(chat_id=user_id, audio=rasm_manzili)
    rasm_manzili='https://t.me/material_tg_bot/34'
    await bot.send_audio(chat_id=user_id, audio=rasm_manzili)
    rasm_manzili='https://t.me/material_tg_bot/35'
    await bot.send_audio(chat_id=user_id, audio=rasm_manzili)
    rasm_manzili='https://t.me/material_tg_bot/36'
    await bot.send_audio(chat_id=user_id, audio=rasm_manzili)
    rasm_manzili='https://t.me/material_tg_bot/37'
    await bot.send_audio(chat_id=user_id, audio=rasm_manzili)
    rasm_manzili='https://t.me/material_tg_bot/38'
    await bot.send_audio(chat_id=user_id, audio=rasm_manzili)