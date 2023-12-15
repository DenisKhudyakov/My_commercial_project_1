from src.views import api_cbr, api_weather
from datetime import datetime

def get_usd() -> tuple:
    """Получаем кортэж курса доллара"""
    return api_cbr()["Valute"]["USD"]["Name"], api_cbr()["Valute"]["USD"]["Value"]


def get_eur() -> tuple:
    """Получаем кортэж курса доллара"""
    return api_cbr()["Valute"]["EUR"]["Name"], api_cbr()["Valute"]["EUR"]["Value"]


def message_weather() -> str:
    weather = api_weather()
    now_date = datetime.strptime(weather['current']['last_updated'][:-6], '%Y-%m-%d').strftime('%d.%m.%Y')
    return f'Привет Богам, погода в {weather['location']['name']}e {now_date} {weather['current']['temp_c']} градуса'


def message_currency() -> str:
    now_date = datetime.now().strftime('%d.%m.%Y')
    return f'Курсы валют на {now_date}\n{get_usd()[0]}: {get_usd()[1]}\n{get_eur()[0]}: {get_eur()[1]}'