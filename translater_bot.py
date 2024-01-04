import logging
from googletrans import Translator
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = ''
translator = Translator()
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(f"Salom {message.from_user.full_name}")



@dp.message_handler()
async def echo(message: types.Message):
    matn = message.text
    trans_soz = translator.translate(matn, dest="en")
    await message.answer(trans_soz.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)