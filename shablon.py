# import os
# from asyncio import run
#
# from aiogram.fsm.context import FSMContext
# from aiogram.types import Message
# from dotenv import load_dotenv
#
# load_dotenv()
#
# from aiogram import Bot, Dispatcher
#
# TOKEN = os.getenv("BOT_TOKEN")
#
# dp = Dispatcher()
#
#
# async def echo(message: Message, bot: Bot, state: FSMContext):
#     # await message.answer(message.text) bu faqat text qaytaradi
#     await message.copy_to(chat_id=message.from_user.id, message=message)
#
#
# async def start(bot: Bot):
#     await bot.send_message(chat_id="1321230134", text="Bot Ishga tushdi ✅")
#
#
# async def stop(bot: Bot):
#     await bot.send_message(chat_id="1321230134", text="Bot To'xtadi ⚠️")
#
#
# async def main(dp) -> None:
#     bot = Bot(token=TOKEN)
#     dp.startup.register(start)
#     dp.message.register(echo)
#     dp.shutdown.register(stop)
#     await dp.start_polling(bot)
#
#
# if __name__ == "__main__":
#     run(main(dp))
