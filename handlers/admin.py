from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db

ID=None


class FSM_admin(StatesGroup):
    document=State()
    country= State()
    group = State()
    name = State()
    disc = State()

#Получаем ID пользователя
#@dp.message_handler(commands=['moderator'], is_chat_admin=True)
async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Что Вам угодно?')
    await message.delete()



#Начало диалога с ботом для загрузки файлов

async def cm_start(message: types.Message):
    if message.from_user.id == ID:
        await FSM_admin.document.set()
        await message.reply('Загрузите файл')

#отмена действия
async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('OK')

#ловим первый ответ(файл)
async def load_file(message: types.Message, state:FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['document'] = message.document.file_id

        await FSM_admin.next()
        await message.reply("Теперь введите страну")


#Ловим второй ответ(страну)

async def load_country(message: types.Message, state:FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['country'] = message.text
        await FSM_admin.next()
        await message.reply("Теперь введите подгруппу")


async def load_group(message: types.Message, state:FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['group'] = message.text
        await FSM_admin.next()
        await message.reply("Теперь введите название")

#Ловим третий ответ(название)
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text

        await FSM_admin.next()
        await message.reply("Теперь введите описание")

async def load_disc(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['disc'] = message.text

        await sqlite_db.sql_add_command(state)
        await state.finish()





def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)
    dp.register_message_handler(cm_start, commands=['Загрузить'], state=None)
    dp.register_message_handler(cancel_handler, state="*", commands='отмена')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(load_file, content_types=['document'], state=FSM_admin.document)
    dp.register_message_handler(load_country, state=FSM_admin.country)
    dp.register_message_handler(load_group, state=FSM_admin.group)
    dp.register_message_handler(load_name, state=FSM_admin.name)
    dp.register_message_handler(load_disc, state=FSM_admin.disc)

