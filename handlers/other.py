from aiogram import types, Dispatcher
from create_bot import dp



async def echo_send(message: types.Message):
    if message.text=='привет':
        await message.answer('и тебе привет')





def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)

