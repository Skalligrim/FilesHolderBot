from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()

bot = Bot(token='5480484463:AAEKj74BvV8mAUI39VQQHIeypP0_Zgh_rjI')
dp = Dispatcher(bot, storage=storage)

