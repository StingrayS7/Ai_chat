import os
from aiogram import Bot
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

# создаем бота
bot = Bot(token=API_TOKEN)

# функция отправки сообщения о низком балансе
async def send_low_balance_notification(message='Ваш баланс заканчивается! Пожалуйста, пополните счет.'):
    await bot.send_message(chat_id=CHAT_ID, text=message)
