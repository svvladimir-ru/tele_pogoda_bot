from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu
from loader import dp


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Выберите день недели", reply_markup=menu)


@dp.message_handler(Text(equals=["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]))
async def get_food(message: Message):
    await message.answer(f"Вы выбрали {message.text}", reply_markup=ReplyKeyboardRemove())