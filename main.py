import logging
import config
from sqliter import SQLighter
import asyncio

from datetime import datetime

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot=Bot(token=config.API_TOKEN)
dp=Dispatcher(bot)
db=SQLighter('db.db')



@dp.message_handler(commands=['subscribe'])
async def subscribe(message:types.Message):

    if (not db.subscriber_exists(message.from_user.id)):

        db.add_subscriber(message.from_user.id)
    else:
        db.update_subscriber(message.from_user.id,True)
    await message.answer('Вы успешно подписались на рассылку')

@dp.message_handler(commands=['unsubscribe'])
async def unsubscribe(message:types.Message):
    if (not db.subscriber_exists(message.from_user.id)):
        db.add_subscriber(message.from_user.id, False)
        await message.answer('Вы не подписаны')
    else:
        db.update_subscriber(message.from_user.id,False)
        await message.answer('Вы успешно отписались от рассылки')


async def scheduled(wait_for):
    while True:

        await asyncio.sleep(wait_for)

        now=datetime.utcnow()
        await bot.send_message(1280790245,f"{now}", disable_notification=True)



if __name__ == '__main__':
    #dp.loop.create_task(scheduled(10))
    executor.start_polling(dp,skip_updates=True)



