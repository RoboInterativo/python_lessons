import telebot
import os
from dotenv import load_dotenv


# Загружает переменные из .env файла в окружение
load_dotenv()

# Теперь можно использовать os.getenv()
token = os.getenv('TOKEN')


bot = telebot.TeleBot(token)

# Глобальное хранилище
user_context = {}
user_states = {}

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    user_states[user_id] = 'start'
    bot.send_message(message.chat.id, "Для запуска поиска острова набрать /rest")

@bot.message_handler(commands=['rest'])
def start(message):
    user_id = message.from_user.id
    user_states[user_id] = 'waiting_size'
    bot.send_message(message.chat.id, "Введите размер идеального острова")


@bot.message_handler(func=lambda m: user_states.get(m.from_user.id) == 'waiting_size')
def get_name(message):
    user_id = message.from_user.id
    user_context[user_id] = {'size': message.text}
    user_states[user_id] = 'waiting_name'
    bot.send_message(message.chat.id, "Введите имя идеального острова")

@bot.message_handler(func=lambda m: user_states.get(m.from_user.id) == 'waiting_name')
def get_age(message):
    user_id = message.from_user.id
    user_context[user_id]['name'] = message.text
    user_states[user_id] = 'waiting_mul'
    bot.send_message(message.chat.id, "Введите количество букв для совпадения")

@bot.message_handler(func=lambda m: user_states.get(m.from_user.id) == 'waiting_mul')
def get_age(message):
    user_id = message.from_user.id
    user_context[user_id]['mul'] = message.text
    user_states[user_id] = 'waiting_island'
    user_context[user_id]['islands'] = []
    bot.send_message(message.chat.id, "Введите имя осрова, размер который вы можете посетить и его размер через запятую. Для завершения наберите stop")

@bot.message_handler(func=lambda m: user_states.get(m.from_user.id) == 'waiting_island')
def get_age(message):
    user_id = message.from_user.id
    if message.text=="stop":
        mul=int(user_context[user_id]['mul'])
        name=user_context[user_id]['name']
        islands=[]
        for item in user_context[user_id]['islands']:
            n,s=item.split(",")
            islands.append(n)
        islands=set(islands)
        matched=[]
        for island_name in islands:
            common_letters = set(island_name.lower()) & set(name.lower())
            if len(common_letters)>=mul:
                matched.append(island_name)
        # Очищаем состояние
        del user_states[user_id]
        del user_context[user_id]

        bot.send_message(message.chat.id, f"Подходящие острова {",".join (matched)}")
    else:
       user_context[user_id]['islands'].append( message.text)
       #user_states[user_id] = 'waiting_mul'
       bot.send_message(message.chat.id, "Введите имя осрова, размер который вы можете посетить и его размер через запятую")





bot.polling(none_stop=True)
