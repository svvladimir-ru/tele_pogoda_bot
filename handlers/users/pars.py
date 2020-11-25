import re
import os.path
import requests
from bs4 import BeautifulSoup as BS
from urllib.parse import urlparse
from loader import dp, bot, api_gis


# коды для эмодзи
thunderstorm = u'\U0001F4A8'    # Code: 200's, 900, 901, 902, 905
drizzle = u'\U0001F4A7'         # Code: 300's
rain = u'\U00002614'            # Code: 500's
snowflake = u'\U00002744'       # Code: 600's snowflake
snowman = u'\U000026C4'         # Code: 600's snowman, 903, 906
atmosphere = u'\U0001F301'      # Code: 700's foogy
clearSky = u'\U00002600'        # Code: 800 clear sky
fewClouds = u'\U000026C5'       # Code: 801 sun behind clouds
clouds = u'\U00002601'          # Code: 802-803-804 clouds general
hot = u'\U0001F525'             # Code: 904
defaultEmoji = u'\U0001F300'    # default emojis

city_name = 'Мегион'
def text_with(city_name):
    URL_WITH = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={api_gis}&lang=ru'
    try:
        url_weather = requests.get(URL_WITH).json()['weather']
        url_main = requests.get(URL_WITH).json()['main']
        description = []
        weather_id = []
        for i in url_weather:
            weather_id.append(i['id'])
            description.append(i['description'])
        emoji = getEmoji(weather_id[0])
        temp = url_main['temp']
        feels_like = url_main['feels_like']
        temp_min = url_main['temp_min']
        temp_max = url_main['temp_max']
        c = ''.join(description)
        text = (
                f"Сегодня {c} {emoji}\n"
                f"Температура: {temp}\n"
                f"Ощущается как: {feels_like}\n"
                f"Минимальная температура днем: {temp_min}\n"
                f"Максимальная температура днем: {temp_max}"
                )

    except:
        text = 'Город не найден'

    return text


def getEmoji(weatherID):
    if weatherID:
        if weatherID == 900 or weatherID == 901 or weatherID == 902 or weatherID == 905:
            return thunderstorm
        elif weatherID == 300:
            return drizzle
        elif weatherID == 500:
            return rain
        elif weatherID == 600 or weatherID == 903 or weatherID == 906:
            return snowflake + ' ' + snowman
        elif weatherID == 700:
            return atmosphere
        elif weatherID == 800:
            return clearSky
        elif weatherID == 801:
            return fewClouds
        elif weatherID == 802 or weatherID == 803 or weatherID == 804:
            return clouds
        elif weatherID == 904:
            return hot
        else:
            return defaultEmoji    # Default emoji

    else:
        return defaultEmoji   # Default emoji
