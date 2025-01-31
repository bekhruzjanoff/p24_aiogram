# from pprint import pprint
#
# from aiogram import Bot
# from aiogram.fsm.context import FSMContext
# from aiogram.types import Message
#
# from states import SignUp
#
#
# async def info(message: Message, bot: Bot, state: FSMContext):
#     profile = await bot.get_chat(chat_id=message.from_user.id)
#     user = message.from_user
#     data = f""" Sizning ismingiz : {user.first_name} \nId raqamingiz: {user.id} \n"""
#     if user.username:
#         data += f"Sizning usernameingiz @{user.username}\n"
#     if user.last_name:
#         data += f"Sizning familiyangiz {user.last_name}\n"
#     if profile.bio:
#         data += f"Sizning bioingiz {profile.bio}\n"
#     pprint(data)
#     await message.answer(text=data)
#
#
# async def helps(message: Message, bot: Bot, state: FSMContext):
#     await message.answer("""
# /start -> Botni ishga tushirish
# /help -> Commandlarni ko'rish
# /vacancy -> E'lon berish
#
#     """)
#
#
# async def vacancy(message: Message, bot: Bot, state: FSMContext):
#     await message.answer(
#         "Ismingnizni kiriting: "
#     )
#     await state.set_state(SignUp.name)
#
#
# async def register_name(message: Message, bot: Bot, state: FSMContext):
#     await state.update_data(name=message.text)
#     await message.answer("Telefon raqamizni kiriting: ")
#     await state.set_state(SignUp.phone)
#
#
# async def register_phone(message: Message, bot: Bot, state: FSMContext):
#     await state.update_data(phone=message.text)
#     await message.answer("Manzilni kiriting: ")
#     await state.set_state(SignUp.address)
#
#
# async def register_address(message: Message, bot: Bot, state: FSMContext):
#     await state.update_data(address=message.text)
#     await message.answer("Lavozimni kiriting: ")
#     await state.set_state(SignUp.position)
#
#
# async def register_position(message: Message, bot: Bot, state: FSMContext):
#     await state.update_data(position=message.text)
#     await message.answer("Maoshni kiriting: ")
#     await state.set_state(SignUp.salary)
#
#
# async def register_finish(message: Message, bot: Bot, state: FSMContext):
#     await state.update_data(salary=message.text)
#     data = await state.get_data()
#     txt = f'''Xodim kerak:
#     Ism: {data.get("name")}
#     Telefon: {data.get("phone")}
#     Manzil: {data.get("address")}
#     Lavozim: {data.get("position")}
#     <b>Maosh: {data.get("salary")} </b>
#     '''
#     await message.answer(text=txt, parse_mode="html")
#     await message.answer("Tez Orada Kanalda Chop etiladi")
#     await bot.send_message(chat_id="751843547", text=txt)
#
#
# async def start_menu(message: Message, bot: Bot, state: FSMContext):
#     await message.answer(f"Assalomu Alaykun {message.from_user.first_name} /help orqali menularni ko'ring")
#
#
# async def start(bot: Bot):
#     await bot.send_message(chat_id="1321230134", text="Bot Ishga tushdi ✅")
#
#
# async def stop(bot: Bot):
#     await bot.send_message(chat_id="1321230134", text="Bot To'xtadi ⚠️")
