from aiogram import Bot, Dispatcher, executor, types
import requests
import json
token = input("Введите токен бота>> ")
bot = Bot(token=token)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def start(message):
    await message.reply('Привет, я - бот, который может узнать подробную информацию о любом IP адресе.\nОтправь мне IP адрес мне и получишь информацию о нем!!\n')
@dp.message_handler(content_types=['text'])
async def text(message):
    if message.chat.type != "private":
        await bot.leave_chat()
    ip = message.text
    url = f'https://ipapi.co/{ip}/json/'
    try:
        json = requests.get(url).json()
        await message.reply(f'Город: {json["city"]}\nРегион: {json["region"]}\nСтрана: {json["country_name"]}\nВалюта: {json["currency"]}\nНаселение страны: {json["country_population"]}\nПровайдер: {json["org"]}')
    except:
        await message.reply('Неверный IP или произошла ошибка')
executor.start_polling(dp, skip_updates=True)