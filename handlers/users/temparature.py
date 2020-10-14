import logging
import requests
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.callback_datas import buy_callback, city_callback
from keyboards.inline.choice_buttons import choice, today_keyboard
from loader import dp, bot, api_gis


@dp.message_handler(Command("help"))
async def show_items(message: Message):
    await message.answer(text="Привет, хочешь узнать прогноз погоды?", reply_markup=choice)



@dp.callback_query_handler(buy_callback.filter(date_temp="today"))
async def one_day(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)# время ожидания

    logging.info(f"{callback_data=}")

    await call.message.answer(text='Выберите город', reply_markup=today_keyboard)


# @dp.callback_query_handler(buy_callback.filter(date_temp="four_days"))
# async def four_days(call: CallbackQuery, callback_data: dict):
#     await call.answer(cache_time=60)
#
#     logging.info(f"{callback_data=}")
#
#     await call.message.answer("Погода на 4 дня",
#                               reply_markup=four_days_keyboard)


@dp.callback_query_handler(city_callback.filter(city_name="moscow"))
async def moscow(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f'{callback_data}')
    URL_WITH = f'http://api.openweathermap.org/data/2.5/weather?q=Moscow&units=metric&appid={api_gis}&lang=ru'
    url_weather = requests.get(URL_WITH).json()['weather']
    url_main = requests.get(URL_WITH).json()['main']
    description = []
    for i in url_weather:
        description.append(i['description'])
    temp = url_main['temp']
    feels_like = url_main['feels_like']
    temp_min = url_main['temp_min']
    temp_max = url_main['temp_max']
    c = ''.join(description)
    await call.message.answer(f"Сегодня {c}\n"
                              f"Температура: {temp}\n"
                              f"Ощущается как: {feels_like}\n"
                              f"Минимальная температура днем: {temp_min}\n"
                              f"Максимальная температура днем: {temp_max}"
                              )


@dp.callback_query_handler(city_callback.filter(city_name="nizniy"))
async def moscow(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f'{callback_data}')
    URL_WITH = f'http://api.openweathermap.org/data/2.5/weather?q=нижний%20новгород&units=metric&appid={api_gis}&lang=ru'
    url_weather = requests.get(URL_WITH).json()['weather']
    url_main = requests.get(URL_WITH).json()['main']
    description = []
    for i in url_weather:
        description.append(i['description'])
    temp = url_main['temp']
    feels_like = url_main['feels_like']
    temp_min = url_main['temp_min']
    temp_max = url_main['temp_max']
    c = ''.join(description)
    await call.message.answer(f"Сегодня {c}\n"
                              f"Температура: {temp}\n"
                              f"Ощущается как: {feels_like}\n"
                              f"Минимальная температура днем: {temp_min}\n"
                              f"Максимальная температура днем: {temp_max}"
                              )


@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
    await call.answer("Отмена!", show_alert=True)

    await call.message.edit_reply_markup(reply_markup=None)
