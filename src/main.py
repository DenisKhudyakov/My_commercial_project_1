from src.views import bot_activated
from src.utils import message_weather, message_currency


bot = bot_activated()


# @bot.message_handler(content_types=["text"])
# def get_text_messages(message):
#     if message.text.lower() == "привет":
#         bot.send_message(
#             message.from_user.id,
#             "Привет, Я персональный Ваш персональный бот Богов снабжения"
#         )
#     elif message.text.lower() == "курс":
#         bot.send_message(message.from_user.id, message_currency())
#     elif message.text.lower() == "погода":
#         bot.send_message(message.from_user.id, message_weather())

@bot.message_handler(content_types=['text'])
def get_message(message):
    if message.text == 'привет':
        bot.send_message(message.from_user.id, 'привет')


bot.infinity_polling()
