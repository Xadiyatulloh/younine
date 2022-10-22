from aiogram import types
from aiogram.types import InputFile
from loader import dp,bot


# Echo bot
@dp.message_handler(text='To Be')
async def bot_echo(message: types.Message):
    await message.document.download()
    await message.answer(text='Dakument Qabul qilindi')
