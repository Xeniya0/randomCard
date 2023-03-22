from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import random
from datetime import datetime
from filesTarot import TOKEN, Taro, keys_list
import schedule
import time


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🃏 Карта")
    btn2 = types.KeyboardButton("🃏 Карта раз в день")
    markup.add(btn1)
    markup.add(btn2)
    await bot.send_message(message.chat.id, text="Привет, Я отправлю тебе карту", reply_markup=markup)


async def send_mes(message):
    x = random.choice(keys_list)
    await bot.send_photo(message.from_user.id, photo=open(x, 'rb'))
    await bot.send_message(message.from_user.id, text=Taro[x])

# @dp.message_handler(content_types=['text'])
# async def process_message(message: types.Message):
#     if message.text == "🃏 Карта":
#         await send_mes(message)

# day_card = 0

# while True:
#



@dp.message_handler(content_types=['text'])
async def every_day(message: types.Message):
    if message.text == "🃏 Карта раз в день":
        await schedule.every().day.at("14:14").do(send_mes(message))
        while True:
            schedule.run_pending()
            time.sleep(1)








#             x = random.choice(keys_list)
#             now = datetime.now()
#             current_time = now.strftime("%H:%M")
#             if current_time == '23:16':
#                 await bot.send_photo(message.from_user.id, photo=open(x, 'rb'))
#                 await bot.send_message(message.from_user.id, text=Taro[x])
#                 break






if __name__ == '__main__':
    executor.start_polling(dp)