import os
import telebot
import requests
from dotenv import find_dotenv, load_dotenv

def api_cbr() -> dict:
    """Получаем от сайте ЦБ РФ данные в формате JSON по крусам валют"""
    if not find_dotenv():
        exit("Переменные окружения не найдены, отсутствует .env файл")
    else:
        load_dotenv()
        URL_CBR = os.getenv("URL_CURRENCY")
        response = requests.get(url=URL_CBR).json()
        return response


def api_weather() -> dict:
    """Получаем данные о прогнозе погоды"""
    if not find_dotenv():
        exit("Переменные окружения не найдены, отсутствует .env файл")
    else:
        load_dotenv()
        API_WEATHER = os.getenv("API_WEATHER")
        response = requests.get(
            url=f"http://api.weatherapi.com/v1/current.json?key={API_WEATHER}&q=Челябинск&aqi=no"
        ).json()
        return response


def bot_activated():
    if not find_dotenv():
        exit("Переменные окружения не найдены, отсутствует .env файл")
    else:
        load_dotenv()
        KEY_BOT = os.getenv("TELEGRAM_API_KEY")
        return telebot.TeleBot(KEY_BOT)
