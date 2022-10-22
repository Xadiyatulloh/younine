from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery

from  keyboards.default.menu import menu_button
from keyboards.default.level import level_button
from keyboards.default.beginner import beginner_button
from keyboards.default.elementry import elementary_button
from keyboards.default.preinter import intermediate_button
from keyboards.default.preielts import pielts_button
from keyboards.inline.tillar_uchun import rasmiy_kanal
from keyboards.default.ielts import ielts_button

from loader import dp, bot



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/XUDOBERDI_GAYRATOV/15"
    await bot.send_photo(chat_id=user_id, photo=video_manzili, caption=f"👋 Assalomu alaykum {message.from_user.full_name} !\n@IT_Subject Obuna Bolishni Unutmang😇✅",reply_markup=rasmiy_kanal)
    await message.answer("<b>Bot Egasi 😎:</b> @MrXadiyatulloh",reply_markup=menu_button)

@dp.callback_query_handler(text="start")
async def bot_echo(message: CallbackQuery):
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id,text="Botdan foidalanishingiz mumkin",reply_markup=menu_button)


@dp.message_handler(text='Choose your level 📈 :')
async def bot_start(message: types.Message):
    ism=message.from_user.first_name
    await message.answer(f'Hello Welcome to Respect`s Bot  {ism}😀✌',reply_markup=level_button)




from aiogram import types
from keyboards.default.level import level_button
from loader import dp
# Echo bot
@dp.message_handler(text="Back 🔙")
async def bot_echo(message: types.Message):
    await message.answer(text="You back again",reply_markup=menu_button)

@dp.message_handler(text='Beginner')
async def bot_start(message: types.Message):
    await message.answer(text="You`re in a beginner section 👶",reply_markup=beginner_button)

from aiogram import types
from keyboards.default.level import level_button
from loader import dp
# Echo bot
@dp.message_handler(text="Back 🔙🔙")
async def bot_echo(message: types.Message):
    await message.answer(text="You back again",reply_markup=level_button)

@dp.message_handler(text='Elementary')
async def bot_start(message: types.Message):
    await message.answer(text="You`re in a elementary section 👦 ",reply_markup=elementary_button)

@dp.message_handler(text="Back ◀")
async def bot_echo(message: types.Message):
    await message.answer(text="You back again",reply_markup=level_button)

@dp.message_handler(text='Pre Intermediate')
async def bot_start(message: types.Message):
    await message.answer(text="You`re in a Pre Intermediate section 🧑 ",reply_markup=intermediate_button)

@dp.message_handler(text="Back ◀◀")
async def bot_echo(message: types.Message):
    await message.answer(text="You back again",reply_markup=level_button)

@dp.message_handler(text='Pre IELTS')
async def bot_start(message: types.Message):
    await message.answer(text="You`re in a Pre IELTS section 👨🏻 ",reply_markup=pielts_button)

@dp.message_handler(text="Back")
async def bot_echo(message: types.Message):
    await message.answer(text="You back again",reply_markup=level_button)

@dp.message_handler(text='IELTS')
async def bot_start(message: types.Message):
    await message.answer(text="You`re in a  IELTS section 📌 ",reply_markup=ielts_button)

@dp.message_handler(text="Back Menu")
async def bot_echo(message: types.Message):
    await message.answer(text="You back again",reply_markup=level_button)
