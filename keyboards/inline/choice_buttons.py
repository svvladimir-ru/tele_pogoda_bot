from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_datas import buy_callback, city_callback


choice = InlineKeyboardMarkup(row_width=2)

today = InlineKeyboardButton(text="Сегодня", callback_data="date:today")
choice.insert(today)

four_days = InlineKeyboardButton(text="На 4 дня", callback_data="date:four_days")
choice.insert(four_days)

cancel_button = InlineKeyboardButton(text="Отмена", callback_data="cancel")
choice.insert(cancel_button)

# А теперь клавиатуры со ссылками на товары
today_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Погода в Москве", callback_data='city:moscow')
    ],
    [
        InlineKeyboardButton(text="Нижний Новгород", callback_data='city:nizniy')
    ]
])
four_days_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Нижний Новгород", callback_data='city:or')
    ]
])