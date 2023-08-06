import logging

from aiogram import Bot, Dispatcher,types
from aiogram.utils import executor
from deep_translator import GoogleTranslator

def tarjimon(text):
    tarjima = GoogleTranslator(source='uz',target='en').translate(text)
    return tarjima

API_TOKEN = '6298374293:AAHEtQO8xkRfJlGqA6qG4yo0LJt_qvhls1I'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("salom bu tarjimon bot \n ushubu bot en -> uz")

@dp.message_handler(content_types='text')
async def send_welcome(message: types.Message):
    texts = message.text
    tarjima = tarjimon(text=texts)
    await message.answer(tarjima)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)