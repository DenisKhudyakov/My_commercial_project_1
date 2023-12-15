import random

from src.views import api_cbr, api_weather, get_comedy
from datetime import datetime


def get_usd_and_eur() -> tuple:
    """Получаем кортэж курса доллара евро"""
    any_dict = api_cbr()
    return any_dict["Valute"]["EUR"]["Name"], any_dict["Valute"]["EUR"]["Value"], any_dict["Valute"]["USD"]["Name"], any_dict["Valute"]["USD"]["Value"]


def message_weather() -> str:
    """Получаем сообщение о погоде на текущий день"""
    weather = api_weather()
    now_date = datetime.strptime(weather['current']['last_updated'][:-6], '%Y-%m-%d').strftime('%d.%m.%Y')
    return f'Погода в {weather["location"]["name"]}e {now_date}\n{weather["current"]["temp_c"]} градуса'


def message_currency() -> str:
    """получаем сообщение о крусе валюты на текущий день"""
    now_date = datetime.now().strftime('%d.%m.%Y')
    return f'Курсы валют на {now_date}\n{get_usd_and_eur()[0]}: {get_usd_and_eur()[1]}\n{get_usd_and_eur()[2]}: {get_usd_and_eur()[3]}'

def get_one_comedy():
    """получаем рандомный анекдот"""
    return random.choice(get_comedy())
