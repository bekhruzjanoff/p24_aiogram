from aiogram.fsm.state import StatesGroup, State


class SignUp(StatesGroup):
    texnologiya = State()
    username = State()
    aloqa = State()
    hudud = State()
    murojat_vaqti = State()
    maosh = State()
    qoshimcha = State()
