import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    user_info = {
        "first_name": message.from_user.first_name,
        "last_name": message.from_user.last_name,
    }
    greeting_message = (
        f"Hello, {user_info.get('first_name')} {user_info.get('last_name')}!"
    )
    bot.send_message(message.chat.id, greeting_message)


bot.polling(none_stop=True)
