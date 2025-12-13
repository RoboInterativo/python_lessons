from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
import sys
import os
import asyncio
from aiogram import Bot, Dispatcher, types, F  # импортируем объект F


from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command

from dotenv import load_dotenv


# Загружает переменные из .env файла в окружение
load_dotenv()

# Теперь можно использовать os.getenv()
token = os.getenv('TOKEN')


bot = Bot(token=token)
dp = Dispatcher()


@dp.message(Command('get_photo'))
async def get_photo(message: types.Message):
   await message.answer_photo(
       photo='https://i.pinimg.com/originals/7e/1b/fd/7e1bfd1191112533fe9872ef47398823.jpg',
       caption='Я отправил тебе картинку'
   )

@dp.message(F.photo)
async def photo_handler(message: types.Message):
   await message.reply(f'ID фото: {message.photo[-1].file_id}')

@dp.message(F.text == 'Как дела?')
async def text_handler(message: types.Message):
   await message.answer('У меня все хорошо) Спасибо за беспокойство<3')

@dp.message(CommandStart())
async def command_start_handler(message: types.Message):
   await message.answer('Привет, пользователь!')


async def main(): # объявляем функцию для запуска основного кода
   await dp.start_polling(bot)

# Точка входа
if __name__ == '__main__': # проверяем название программы
   asyncio.run(main()) # вызываем функцию для запуска основной программы
