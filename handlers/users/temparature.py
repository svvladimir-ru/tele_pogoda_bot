import logging
import requests
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from keyboards.inline.callback_datas import buy_callback, city_callback
from keyboards.inline.choice_buttons import choice, today_keyboard
from loader import dp, bot, api_gis
from .pars import text_with


@dp.message_handler(Command("start"))
async def show_items(message: Message):
    await message.answer(text="Привет, хочешь узнать прогноз погоды?", reply_markup=choice)


@dp.callback_query_handler(buy_callback.filter(date_temp="today"))
async def one_day(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)# время ожидания

    logging.info(f"{callback_data=}")

    await call.message.answer(text='Выберите город, либо введите свой', reply_markup=today_keyboard)


@dp.message_handler()
async def echo(message: Message):
    logging.info(f'{message}')
    message_lower = message.text
    city_name = message_lower.lower()
    await message.answer(text_with(city_name))


@dp.callback_query_handler(city_callback.filter(city_name="moscow"))
async def moscow(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f'{callback_data}')
    await call.message.answer(text_with('moscow')
                              )


@dp.callback_query_handler(city_callback.filter(city_name="nizniy"))
async def nizniy(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f'{callback_data}')
    await call.message.answer(text_with('Нижний Новгород')
                              )

# Кнопка отмены, связана с keyboard
@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
    await call.answer("Отмена!", show_alert=True)

    await call.message.edit_reply_markup(reply_markup=None)
