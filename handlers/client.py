from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards.client_kb import kb_client, inline_kb_USA, inline_kb_Vietnam, inline_kb_Israel, inline_kb_UAE, \
    inline_kb_Saudi_Arabia, inline_kb_India
from keyboards.client_kb import inline_kb_Argentina, inline_kb_Bolivia, inline_kb_Brazilia, inline_kb_Kolumbia
from keyboards.client_kb import inline_kb_Komparativistika, inline_kb_Kuba, inline_kb_Mexico, inline_kb_Nicaragua
from keyboards.client_kb import inline_kb_Chile, inline_kb_Ecuador, inline_kb_Latin_America, inline_kb_RussiaAndIC
from keyboards.client_kb import inline_kb_Concept_Papers, inline_kb_China, inline_kb_Iran, inline_kb_Turkey, \
    inline_kb_Venezuela, inline_kb_North_Korea, inline_kb_Great_Britain

from data_base import sqlite_db

ID = None
country = None


async def comand_start(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Что Вам угодно?', reply_markup=kb_client)
    await message.delete()


@dp.message_handler(commands=['меню'])
async def menu(message: types.Message):
    await sqlite_db.sql_read(message)


@dp.message_handler(commands=['США'])
async def USA(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите группу', reply_markup=inline_kb_USA)

    @dp.callback_query_handler(lambda call: True)
    async def callback_worker(call: types.CallbackQuery):
        await sqlite_db.sql_all(call.from_user.id, call.data)


@dp.message_handler(commands=['Вьетнам'])
async def Vietnam(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите группу', reply_markup=inline_kb_Vietnam)

    @dp.callback_query_handler(lambda call: True)
    async def callback_worker(call):
        await sqlite_db.sql_all(call.from_user.id, call.data)


@dp.message_handler(commands=['Израиль'])
async def Israel(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите группу', reply_markup=inline_kb_Israel)

    @dp.callback_query_handler(lambda call: True)
    async def callback_worker(call):
        await sqlite_db.sql_all(call.from_user.id, call.data)


@dp.message_handler(commands=['ОАЭ'])
async def UAE(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите группу', reply_markup=inline_kb_UAE)

    @dp.callback_query_handler(lambda call: True)
    async def callback_worker(call):
        await sqlite_db.sql_all(call.from_user.id, call.data)


@dp.message_handler(commands=['Саудовская_Аравия'])
async def Saudi_Arabia(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите группу', reply_markup=inline_kb_Saudi_Arabia)

    @dp.callback_query_handler(lambda call: True)
    async def callback_worker(call):
        await sqlite_db.sql_all(call.from_user.id, call.data)


@dp.message_handler(commands=['Индия'])
async def India(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите группу', reply_markup=inline_kb_India)

    @dp.callback_query_handler(lambda call: True)
    async def callback_worker(call):
        await sqlite_db.sql_all(call.from_user.id, call.data)


@dp.message_handler(commands=['Аргентина'])
async def Argentina(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите группу', reply_markup=inline_kb_Argentina)

    @dp.callback_query_handler(lambda call: True)
    async def callback_worker(call):
        await sqlite_db.sql_all(call.from_user.id, call.data)


@dp.message_handler(commands=['Боливия'])
async def Bolivia(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите группу', reply_markup=inline_kb_Bolivia)

    @dp.callback_query_handler(lambda call: True)
    async def callback_worker(call):
        await sqlite_db.sql_all(call.from_user.id, call.data)


@dp.message_handler(commands=['Бразилия'])
async def Brazilia(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите группу', reply_markup=inline_kb_Brazilia)

    @dp.callback_query_handler(lambda call: True)
    async def callback_worker(call):
        await sqlite_db.sql_all(call.from_user.id, call.data)


@dp.message_handler(commands=['Колумбия'])
async def Kolumbia(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите группу', reply_markup=inline_kb_Kolumbia)

    @dp.callback_query_handler(lambda call: True)
    async def callback_worker(call):
        await sqlite_db.sql_all(call.from_user.id, call.data)


@dp.message_handler(commands=['Компаративистика'])
async def Komparativistika(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите группу', reply_markup=inline_kb_Komparativistika)

    @dp.callback_query_handler(lambda call: True)
    async def callback_worker(call):
        await sqlite_db.sql_all(call.from_user.id, call.data)


@dp.message_handler(commands=['Куба'])
async def Kuba(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите группу', reply_markup=inline_kb_Kuba)

    @dp.callback_query_handler(lambda call: True)
    async def callback_worker(call):
        await sqlite_db.sql_all(call.from_user.id, call.data)


@dp.message_handler(commands=['Мексика'])
async def Mexico(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите группу', reply_markup=inline_kb_Mexico)

    @dp.callback_query_handler(lambda call: True)
    async def callback_worker(call):
        await sqlite_db.sql_all(call.from_user.id, call.data)


@dp.message_handler(commands=['Никарагуа'])
async def Nicaragua(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите группу', reply_markup=inline_kb_Nicaragua)

    @dp.callback_query_handler(lambda call: True)
    async def callback_worker(call):
        await sqlite_db.sql_all(call.from_user.id, call.data)


@dp.message_handler(commands=['Чили'])
async def Chile(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите группу', reply_markup=inline_kb_Chile)

    @dp.callback_query_handler(lambda call: True)
    async def callback_worker(call):
        await sqlite_db.sql_all(call.from_user.id, call.data)


@dp.message_handler(commands=['Эквадор'])
async def Ecuador(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите группу', reply_markup=inline_kb_Ecuador)

    @dp.callback_query_handler(lambda call: True)
    async def callback_worker(call):
        await sqlite_db.sql_all(call.from_user.id, call.data)


@dp.message_handler(commands=['Латинская_Америка'])
async def Latin_America(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите группу', reply_markup=inline_kb_Latin_America)

    @dp.callback_query_handler(lambda call: True)
    async def callback_worker(call):
        await sqlite_db.sql_all(call.from_user.id, call.data)


@dp.message_handler(commands=['Россия_и_международное_взаимодействие'])
async def RussiaAndIC(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите группу', reply_markup=inline_kb_RussiaAndIC)

    @dp.callback_query_handler(lambda call: True)
    async def callback_worker(call):
        await sqlite_db.sql_all(call.from_user.id, call.data)


@dp.message_handler(commands=['Концептуальные_документы'])
async def Concept_Papers(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите группу', reply_markup=inline_kb_Concept_Papers)

    @dp.callback_query_handler(lambda call: True)
    async def callback_worker(call):
        await sqlite_db.sql_all(call.from_user.id, call.data)


@dp.message_handler(commands=['Китай'])
async def China(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите группу', reply_markup=inline_kb_China)

    @dp.callback_query_handler(lambda call: True)
    async def callback_worker(call):
        await sqlite_db.sql_all(call.from_user.id, call.data)


@dp.message_handler(commands=['Иран'])
async def Iran(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите группу', reply_markup=inline_kb_Iran)

    @dp.callback_query_handler(lambda call: True)
    async def callback_worker(call):
        await sqlite_db.sql_all(call.from_user.id, call.data)


@dp.message_handler(commands=['Турция'])
async def Turkey(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите группу', reply_markup=inline_kb_Turkey)

    @dp.callback_query_handler(lambda call: True)
    async def callback_worker(call):
        await sqlite_db.sql_all(call.from_user.id, call.data)


@dp.message_handler(commands=['Венесуэла'])
async def Venezuela(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите группу', reply_markup=inline_kb_Venezuela)

    @dp.callback_query_handler(lambda call: True)
    async def callback_worker(call):
        await sqlite_db.sql_all(call.from_user.id, call.data)


@dp.message_handler(commands=['Северная_Корея'])
async def North_Korea(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите группу', reply_markup=inline_kb_North_Korea)

    @dp.callback_query_handler(lambda call: True)
    async def callback_worker(call):
        await sqlite_db.sql_all(call.from_user.id, call.data)

@dp.message_handler(commands=['Великобритания'])
async def Great_Britain(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите группу', reply_markup=inline_kb_Great_Britain)

    @dp.callback_query_handler(lambda call: True)
    async def callback_worker(call):
        await sqlite_db.sql_all(call.from_user.id, call.data)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(comand_start, commands=['start', 'help'], is_chat_admin=True)
    dp.register_message_handler(menu, commands=['меню'])
    dp.register_message_handler(USA, commands=['США'])
    dp.register_message_handler(Vietnam, commands=['Вьетнам'])
    dp.register_message_handler(Israel, commands=['Израиль'])
    dp.register_message_handler(UAE, commands=['ОАЭ'])
    dp.register_message_handler(Saudi_Arabia, commands=['Саудовская_Аравия'])
    dp.register_message_handler(India, commands=['Индия'])
    dp.register_message_handler(Argentina, commands=['Аргентина'])
    dp.register_message_handler(Bolivia, commands=['Боливия'])
    dp.register_message_handler(Brazilia, commands=['Бразилия'])
    dp.register_message_handler(Kolumbia, commands=['Колумбия'])
    dp.register_message_handler(Komparativistika, commands=['Компаративистика'])
    dp.register_message_handler(Kuba, commands=['Куба'])
    dp.register_message_handler(Mexico, commands=['Мексика'])
    dp.register_message_handler(Nicaragua, commands=['Никарагуа'])
    dp.register_message_handler(Chile, commands=['Чили'])
    dp.register_message_handler(Ecuador, commands=['Эквадор'])
    dp.register_message_handler(Latin_America, commands=['Латинская_Америка'])
    dp.register_message_handler(RussiaAndIC, commands=['Россия_и_международное_взаимодействие'])
    dp.register_message_handler(Concept_Papers, commands=['Концептуальные_документы'])
    dp.register_message_handler(China, commands=['Китай'])
    dp.register_message_handler(Iran, commands=['Иран'])
    dp.register_message_handler(Turkey, commands=['Турция'])
    dp.register_message_handler(Venezuela, commands=['Венесуэла'])
    dp.register_message_handler(North_Korea, commands=['Северная_Корея'])
    dp.register_message_handler(Great_Britain, commands=['Великобритания'])
