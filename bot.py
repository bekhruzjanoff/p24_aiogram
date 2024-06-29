import os
from asyncio import run

from aiogram.filters import Command
from aiogram.types import BotCommand, Message
from dotenv import load_dotenv

from functions import start, info, stop, vacancy, helps, start_menu, register_texnologiya, register_username, \
    register_aloqa, register_hudud, register_murojat_vaqti, register_maosh, register_finish
from states import SignUp

load_dotenv()

from aiogram import Bot, Dispatcher

TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()


async def main(dp) -> None:
    bot = Bot(token=TOKEN)
    await bot.set_my_commands(
        [
            BotCommand(command="/start", description="Bot ni ishga tushirish"),
            BotCommand(command="/info", description="Shaxsiy ma'lumotlarni olish"),
            BotCommand(command="/vacancy", description="Ishga e'lon berish"),
            BotCommand(command="/help", description="Yordam")
        ]
    )
    dp.startup.register(start)
    dp.message.register(vacancy, Command('vacancy'))
    dp.message.register(register_texnologiya, SignUp.texnologiya)
    dp.message.register(register_username, SignUp.username)
    dp.message.register(register_aloqa, SignUp.aloqa)
    dp.message.register(register_hudud, SignUp.hudud)
    dp.message.register(register_murojat_vaqti, SignUp.murojat_vaqti)
    dp.message.register(register_maosh, SignUp.maosh)
    dp.message.register(register_finish, SignUp.qoshimcha)
    dp.message.register(info, Command('info'))
    dp.message.register(start_menu, Command('start'))
    dp.message.register(helps, Command('help'))
    dp.shutdown.register(stop)
    await dp.start_polling(bot)


if __name__ == "__main__":
    run(main(dp))
