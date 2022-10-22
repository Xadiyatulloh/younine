from aiogram import types
from aiogram.types import InputFile
from loader import dp,bot


# Echo bot
@dp.message_handler(text='Present Simple')
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/material_tg_bot/6'
    await bot.send_video(chat_id=user_id,video=rasm_manzili)

@dp.message_handler(text='Present Continuous')
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/material_tg_bot/8'
    await bot.send_video(chat_id=user_id,video=rasm_manzili)

@dp.message_handler(text='Present Simple')
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/material_tg_bot/7'
    await bot.send_video(chat_id=user_id,video=rasm_manzili)


@dp.message_handler(text='Future Simple')
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/material_tg_bot/9'
    await bot.send_video(chat_id=user_id,video=rasm_manzili)

@dp.message_handler(text='Past Simple')
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/material_tg_bot/110'
    await bot.send_video(chat_id=user_id,video=rasm_manzili)
