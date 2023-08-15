import logging
import random
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode

TOKEN = "6026322841:AAF9cnKngbCM6ES6mqQIf85XKp_y_lyaruc" 

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
dp.middleware.setup(LoggingMiddleware())


# Список вдохновляющих цитат
quotes = [
    "Ты - удивительная женщина, способная на большее, чем ты думаешь.",
    "Не бойся воплощать свои мечты в реальность, потому что ты достойна успеха.",
    "Когда ты веришь в себя, мир тоже начинает верить в тебя.",
    "Сложности — это лишь шанс показать, насколько ты сильна.",
    "Пусть каждый твой день будет наполнен радостью и достижениями.",
    "Ты способна на много больше, чем ты думаешь. Вперед, к своим целям!",
    "Помни, что каждый шаг приближает тебя к твоей мечте.",
    "Ты уникальна и неповторима. Твоя улыбка способна изменить мир вокруг тебя.",
    "Не забывай дарить любовь и заботу себе так же, как ты это делаешь для других.",
    "Помни, что даже в сложные моменты у тебя есть сила и мудрость.",
]


@dp.message_handler(lambda message: any(keyword in message.text.lower() for keyword in ["помоги", "мне плохо", "мне скучно", "меня бросили", "цитата"]))
async def send_quote(message: types.Message):
    quote = random.choice(quotes)
    await message.reply(quote, parse_mode=ParseMode.MARKDOWN)


if __name__ == "__main__":
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)