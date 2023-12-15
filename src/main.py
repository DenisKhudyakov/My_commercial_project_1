from src.views import bot_activated
from src.utils import message_weather, message_currency, get_one_comedy


bot = bot_activated()


@bot.message_handler(content_types=["text"])
def get_text_messages(message):
    if message.text.lower() == "привет":
        bot.send_message(
            message.chat.id,
            "Привет, Я персональный бот Богов снабжения"
        )
    elif message.text.lower() == "курс":
        bot.send_message(message.chat.id, message_currency())
    elif message.text.lower() == "погода":
        bot.send_message(message.chat.id, message_weather())
    elif message.text.lower() == "ржака":
        bot.send_message(message.chat.id, get_one_comedy())



bot.infinity_polling()
