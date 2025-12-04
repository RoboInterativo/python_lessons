import telebot

bot = telebot.TeleBot('вставьте_ваш_токен_здесь')

@bot.message_handler(commands = ['start'])
def say_hi(message):
   bot.send_message(message.chat.id, 'Привет, пользователь!')

@bot.message_handler(commands=['squire'])
def find_squire(message):
   bot.send_message(message.chat.id, 'Введи имя человека и его качество')

   traits = set()

   @bot.message_handler(commands=['join_traits'])
   def join_traits(new_message):
       sorted_traits = sorted(traits)
       bot.send_message(new_message.chat.id, f'Качества оруженосца: {" ".join(sorted_traits)}')

   @bot.message_handler()
   def input_trait(new_message):
       if ': ' in new_message.text:
           _, item = new_message.text.split(': ')
           traits.add(item)
       else:
           bot.send_message(new_message.chat.id, 'Имя и качество введены некорректно! Повторите ввод')

bot.polling(none_stop=True)
