from pprint import pprint

from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from states import SignUp


async def info(message: Message, bot: Bot, state: FSMContext):
    profile = await bot.get_chat(chat_id=message.from_user.id)
    user = message.from_user
    data = f""" Sizning ismingiz : {user.first_name} \nId raqamingiz: {user.id} \n"""
    if user.username:
        data += f"Sizning usernameingiz @{user.username}\n"
    if user.last_name:
        data += f"Sizning familiyangiz {user.last_name}\n"
    if profile.bio:
        data += f"Sizning bioingiz {profile.bio}\n"
    pprint(data)
    await message.answer(text=data)


async def helps(message: Message, bot: Bot, state: FSMContext):
    await message.answer("""
/start -> Botni ishga tushirish    
/help -> Commandlarni ko'rish    
/vacancy -> E'lon berish    

    """)


async def vacancy(message: Message, bot: Bot, state: FSMContext):
    await message.answer(
        "Texnologiyani kiriting: "
    )
    await state.set_state(SignUp.texnologiya)


async def register_texnologiya(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(texnologiya=message.text)
    await message.answer("Usernamingizni kiriting: ")
    await state.set_state(SignUp.username)


async def register_username(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(username=message.text)
    await message.answer("Telefoningizni kiriting: ")
    await state.set_state(SignUp.aloqa)


async def register_aloqa(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(aloqa=message.text)
    await message.answer("Hududingizni  kiriting: ")
    await state.set_state(SignUp.hudud)


async def register_hudud(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(hudud=message.text)
    await message.answer("Murojaat vaqtini  kiriting: ")
    await state.set_state(SignUp.murojat_vaqti)


async def register_murojat_vaqti(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(murojat_vaqti=message.text)
    await message.answer("Xohlayotgan maoshingizni kiriting: ")
    await state.set_state(SignUp.maosh)


async def register_maosh(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(maosh=message.text)
    await message.answer("Qo'shimcha malumot kiritishingiz mumkin: ")
    await state.set_state(SignUp.qoshimcha)


async def register_finish(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(qoshimcha=message.text)
    data = await state.get_data()
    txt = f'''Ma'lumotlaringiz: 
    📚Texnologiya:{data.get("texnologiya")}
    🖥Telegram:@{data.get("username")}
    📞Aloqa:{data.get("aloqa")}
    🌐Hudud:{data.get("hudud")}
    🕰Murojaat vaqti:{data.get("murojat_vaqti")}
    💰Maosh:{data.get("maosh")}
    ‼️Qoshimcha:{data.get("qoshimcha")}
    '''
    await message.answer(text=txt, parse_mode="html")
    await message.answer("Tez Orada Kanalda Chop etiladi")
    await bot.send_message(chat_id="1", text=txt)


async def start_menu(message: Message, bot: Bot, state: FSMContext):
    await message.answer(f"Assalomu Alaykum {message.from_user.first_name} /help orqali menularni ko'ring")


async def start(bot: Bot):
    await bot.send_message(chat_id="1321230134", text="Bot Ishga tushdi ✅")


async def stop(bot: Bot):
    await bot.send_message(chat_id="1321230134", text="Bot To'xtadi ⚠️")
