from aiogram import types
from aiogram.dispatcher import FSMContext
from states.holatlar import Murojaat
from keyboards.default.menu import  menu_button,tasdiqlash_button
from loader import dp,bot



@dp.message_handler(text="Adminga Yozish 📤")
async def bot_echo(message: types.Message):
    await message.answer(text="🙍‍♂️Biz bilan bog'lanish uchun Ismingizni kiriting:")
    await Murojaat.Ism_holati.set()

@dp.message_handler(state=Murojaat.Ism_holati)
async def bot_echo(message:types.Message,state:FSMContext):

    ism = message.text
    await state.update_data({"ism": ism})
    await message.answer(text="️Familyangiz")
    await Murojaat.Familya_holati.set()

@dp.message_handler(state=Murojaat.Familya_holati)
async def bot_echo(message: types.Message, state: FSMContext):
    fam = message.text
    await state.update_data({"FAm": fam})
    await message.answer(text="🕹Yoshingiz")
    await Murojaat.Yoshi_holati.set()

@dp.message_handler(state=Murojaat.Yoshi_holati)
async def bot_echo(message: types.Message, state: FSMContext):
    yosh = message.text
    await state.update_data({"yosh": yosh})
    await message.answer(text="📱️Raqamingiz\n\nMisol uchun : +998913272554")
    await Murojaat.Raqami_holati.set()

@dp.message_handler(state=Murojaat.Raqami_holati)
async def bot_echo(message: types.Message, state: FSMContext):
    nom = message.text
    await state.update_data({"num": nom})
    await message.answer(text="💬Murojatingizni Kiriting")
    await Murojaat.Xabar_holati.set()

@dp.message_handler(state=Murojaat.Xabar_holati)
async def bot_echo(message: types.Message, state: FSMContext):
    txt = message.text
    user_id = message.from_user.id
    await state.update_data({"text": txt})

    malumot= await state.get_data()

    ismi = malumot.get("ism")
    familya = malumot.get("FAm")
    yoshi = malumot.get("yosh")
    nomeri = malumot.get("num")
    xabri = malumot.get("text")

    ekranga_chiqarish = f"🙍🏻‍♂️Ism :{ismi}\n" \
                        f"🙍🏻‍♂️Familya : {familya}\n"\
                        f"🕹Yosh : {yoshi}\n" \
                        f"📱️Raqam : {nomeri}\n" \
                        f"💬Murojat : {xabri}\n"

    await bot.send_message(chat_id=user_id,text=ekranga_chiqarish,reply_markup=tasdiqlash_button)
    await Murojaat.tasdiqlash_holati.set()

@dp.message_handler(state=Murojaat.tasdiqlash_holati,text="Tasdiqlash ✔️")
async def bot_echo(message: types.Message, state: FSMContext):
    txt = message.text
    user_id = message.from_user.id
    malumot = await state.get_data()

    ismi = malumot.get("ism")
    familya = malumot.get("FAm")
    yoshi = malumot.get("yosh")
    nomeri = malumot.get("num")
    xabri = malumot.get("text")

    ekranga_chiqarish = f"{ismi}Dan murojaat kelib tushdi\n" \
                        f"🙍🏻‍♂️Ism : {ismi}\n" \
                        f"🙍🏻‍♂️Familya : {familya}\n"\
                        f"🕹Yosh : {yoshi}\n" \
                        f"📱️Raqam : {nomeri}\n" \
                        f"💬Murojat : {xabri}\n"
    await bot.send_message(chat_id="5742635856",text=ekranga_chiqarish)
    await bot.send_message(chat_id=user_id,text="Adminga Yuborildi ✅",reply_markup=menu_button)
    await state.finish()

@dp.message_handler(state=Murojaat.tasdiqlash_holati,text="Bekor Qilish ❌️")
async def bot_echo(message: types.Message, state: FSMContext):
    txt = message.text
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id,text="Murojaatingiz Bekor qilindi ❌",reply_markup=menu_button)
    await state.finish()