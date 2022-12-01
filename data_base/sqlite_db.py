import sqlite3 as sq
from create_bot import bot
# from keyboards.client_kb import inline_kb1


def sql_start():
    global base, cur
    base = sq.connect('files.db')
    cur = base.cursor()
    if base:
        print('connected!')
    base.execute(
        'CREATE TABLE IF NOT EXISTS menu (file TEXT, country TEXT, gruppa TEXT, name TEXT PRIMARY KEY, description TEXT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?,?,?,?,?)', tuple(data.values()))
        base.commit()


async def sql_read(message):
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_document(message.from_user.id, ret[0])
        await bot.send_message(message.from_user.id, f'{ret[1]}\nНазвание: {ret[2]}\nОписание: {ret[-1]}')


async def sql_all(id, call_name):
    flag=0
    if call_name == '/Справки_США':
        for ret in cur.execute('SELECT * FROM menu WHERE country="США" and gruppa="Справки"').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Инфографика_США':
        for ret in cur.execute('SELECT * FROM menu WHERE (country="США") and (gruppa="Инфографика")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')
    if call_name == '/База_знаний_США':
        for ret in cur.execute('SELECT * FROM menu WHERE (country="США") and (gruppa="База знаний")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Справки_Вьетнам':
        for ret in cur.execute('SELECT * FROM menu WHERE country="Вьетнам" and gruppa="Справки"').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Инфографика_Вьетнам':
        for ret in cur.execute('SELECT * FROM menu WHERE (country="Вьетнам") and (gruppa="Инфографика")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/База_знаний_Вьетнам':
        for ret in cur.execute('SELECT * FROM menu WHERE (country="Вьетнам") and (gruppa="База знаний")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Справки_Израиль':
        for ret in cur.execute('SELECT * FROM menu WHERE country="Израиль" and gruppa="Справки"').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Инфографика_Израиль':
        for ret in cur.execute('SELECT * FROM menu WHERE (country="Израиль") and (gruppa="Инфографика")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/База_знаний_Израиль':
        for ret in cur.execute('SELECT * FROM menu WHERE (country="Израиль") and (gruppa="База знаний")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Справки_ОАЭ':
        for ret in cur.execute('SELECT * FROM menu WHERE country="ОАЭ" and gruppa="Справки"').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Инфографика_ОАЭ':
        for ret in cur.execute('SELECT * FROM menu WHERE (country="ОАЭ") and (gruppa="Инфографика")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/База_знаний_ОАЭ':
        for ret in cur.execute('SELECT * FROM menu WHERE (country="ОАЭ") and (gruppa="База знаний")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Справки_Саудовская_Аравия':
        for ret in cur.execute('SELECT * FROM menu WHERE country="Саудовская Аравия" and gruppa="Справки"').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Инфографика_Саудовская_Аравия':
        for ret in cur.execute(
                'SELECT * FROM menu WHERE (country="Саудовская Аравия") and (gruppa="Инфографика")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/База_знаний_Саудовская_Аравия':
        for ret in cur.execute(
                'SELECT * FROM menu WHERE (country="Саудовская Аравия") and (gruppa="База знаний")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Справки_Индия':
        for ret in cur.execute('SELECT * FROM menu WHERE country="Индия" and gruppa="Справки"').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Инфографика_Индия':
        for ret in cur.execute('SELECT * FROM menu WHERE (country="Индия") and (gruppa="Инфографика")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/База_знаний_Индия':
        for ret in cur.execute('SELECT * FROM menu WHERE (country="Индия") and (gruppa="База знаний")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Справки_Аргентина':
        for ret in cur.execute('SELECT * FROM menu WHERE country="Аргентина" and gruppa="Справки"').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Инфографика_Аргентина':
        for ret in cur.execute('SELECT * FROM menu WHERE (country="Аргентина") and (gruppa="Инфографика")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/База_знаний_Аргентина':
        for ret in cur.execute('SELECT * FROM menu WHERE (country="Аргентина") and (gruppa="База знаний")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Справки_Боливия':
        for ret in cur.execute('SELECT * FROM menu WHERE country="Боливия" and gruppa="Справки"').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Инфографика_Боливия':
        for ret in cur.execute('SELECT * FROM menu WHERE (country="Боливия") and (gruppa="Инфографика")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/База_знаний_Боливия':
        for ret in cur.execute('SELECT * FROM menu WHERE (country="Боливия") and (gruppa="База знаний")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')


    if call_name == '/Справки_Бразилия':
        for ret in cur.execute('SELECT * FROM menu WHERE country="Бразилия" and gruppa="Справки"').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Инфографика_Бразилия':
        for ret in cur.execute('SELECT * FROM menu WHERE (country="Бразилия") and (gruppa="Инфографика")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/База_знаний_Бразилия':
        for ret in cur.execute('SELECT * FROM menu WHERE (country="Бразилия") and (gruppa="База знаний")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')


    if call_name == '/Справки_Колумбия':
        for ret in cur.execute('SELECT * FROM menu WHERE country="Колумбия" and gruppa="Справки"').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Инфографика_Колумбия':
        for ret in cur.execute('SELECT * FROM menu WHERE (country="Колумбия") and (gruppa="Инфографика")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/База_знаний_Колумбия':
        for ret in cur.execute('SELECT * FROM menu WHERE (country="Колумбия") and (gruppa="База знаний")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Справки_Компаративистика':
        for ret in cur.execute('SELECT * FROM menu WHERE country="Компаративистика" and gruppa="Справки"').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Инфографика_Компаративистика':
        for ret in cur.execute(
                'SELECT * FROM menu WHERE (country="Компаративистика") and (gruppa="Инфографика")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/База_знаний_Компаративистика':
        for ret in cur.execute(
                'SELECT * FROM menu WHERE (country="Компаративистика") and (gruppa="База знаний")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Справки_Куба':
        for ret in cur.execute('SELECT * FROM menu WHERE country="Куба" and gruppa="Справки"').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Инфографика_Куба':
        for ret in cur.execute('SELECT * FROM menu WHERE (country="Куба") and (gruppa="Инфографика")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/База_знаний_Куба':
        for ret in cur.execute('SELECT * FROM menu WHERE (country="Куба") and (gruppa="База знаний")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Справки_Мексика':
        for ret in cur.execute('SELECT * FROM menu WHERE country="Мексика" and gruppa="Справки"').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Инфографика_Мексика':
        for ret in cur.execute('SELECT * FROM menu WHERE (country="Мексика") and (gruppa="Инфографика")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/База_знаний_Мексика':
        for ret in cur.execute('SELECT * FROM menu WHERE (country="Мексика") and (gruppa="База знаний")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Справки_Никарагуа':
        for ret in cur.execute('SELECT * FROM menu WHERE country="Никарагуа" and gruppa="Справки"').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Инфографика_Никарагуа':
        for ret in cur.execute('SELECT * FROM menu WHERE (country="Никарагуа") and (gruppa="Инфографика")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/База_знаний_Никарагуа':
        for ret in cur.execute('SELECT * FROM menu WHERE (country="Никарагуа") and (gruppa="База знаний")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Справки_Чили':
        for ret in cur.execute('SELECT * FROM menu WHERE country="Чили" and gruppa="Справки"').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Инфографика_Чили':
        for ret in cur.execute('SELECT * FROM menu WHERE (country="Чили") and (gruppa="Инфографика")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/База_знаний_Чили':
        for ret in cur.execute('SELECT * FROM menu WHERE (country="Чили") and (gruppa="База знаний")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Справки_Эквадор':
        for ret in cur.execute('SELECT * FROM menu WHERE country="Эквадор" and gruppa="Справки"').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Инфографика_Эквадор':
        for ret in cur.execute('SELECT * FROM menu WHERE (country="Эквадор") and (gruppa="Инфографика")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/База_знаний_Эквадор':
        for ret in cur.execute('SELECT * FROM menu WHERE (country="Эквадор") and (gruppa="База знаний")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Справки_Латинская_Америка':
        for ret in cur.execute('SELECT * FROM menu WHERE country="Латинская Америка" and gruppa="Справки"').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Инфографика_Латинская_Америка':
        for ret in cur.execute(
                'SELECT * FROM menu WHERE (country="Латинская Америка") and (gruppa="Инфографика")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/База_знаний_Латинская_Америка':
        for ret in cur.execute(
                'SELECT * FROM menu WHERE (country="Латинская Америка") and (gruppa="База знаний")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Справки_Россия_и_МВ':
        for ret in cur.execute(
                'SELECT * FROM menu WHERE country="Россия и международное взаимодействие" and gruppa="Справки"').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Инфографика_Россия_и_МВ':
        for ret in cur.execute(
                'SELECT * FROM menu WHERE (country="Россия и международное взаимодействие") and (gruppa="Инфографика")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/База_знаний_Россия_и_МВ':
        for ret in cur.execute(
                'SELECT * FROM menu WHERE (country="Россия и международное взаимодействие") and (gruppa="База знаний")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Справки_Концепт_док':
        for ret in cur.execute(
                'SELECT * FROM menu WHERE country="Концептуальные документы" and gruppa="Справки"').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Инфографика_Концепт_док':
        for ret in cur.execute(
                'SELECT * FROM menu WHERE (country="Концептуальные документы") and (gruppa="Инфографика")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/База_знаний_Концепт_док':
        for ret in cur.execute(
                'SELECT * FROM menu WHERE (country="Концептуальные документы") and (gruppa="База знаний")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Справки_Китай':
        for ret in cur.execute('SELECT * FROM menu WHERE country="Китай" and gruppa="Справки"').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Инфографика_Китай':
        for ret in cur.execute('SELECT * FROM menu WHERE (country="Китай") and (gruppa="Инфографика")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/База_знаний_Китай':
        for ret in cur.execute('SELECT * FROM menu WHERE (country="Китай") and (gruppa="База знаний")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Справки_Иран':
        for ret in cur.execute('SELECT * FROM menu WHERE country="Иран" and gruppa="Справки"').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Инфографика_Иран':
        for ret in cur.execute('SELECT * FROM menu WHERE (country="Иран") and (gruppa="Инфографика")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/База_знаний_Иран':
        for ret in cur.execute('SELECT * FROM menu WHERE (country="Иран") and (gruppa="База знаний")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Справки_Турция':
        for ret in cur.execute('SELECT * FROM menu WHERE country="Турция" and gruppa="Справки"').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Инфографика_Турция':
        for ret in cur.execute('SELECT * FROM menu WHERE (country="Турция") and (gruppa="Инфографика")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/База_знаний_Турция':
        for ret in cur.execute('SELECT * FROM menu WHERE (country="Турция") and (gruppa="База знаний")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Справки_Венесуэла':
        for ret in cur.execute('SELECT * FROM menu WHERE country="Венесуэла" and gruppa="Справки"').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Инфографика_Венесуэла':
        for ret in cur.execute('SELECT * FROM menu WHERE (country="Венесуэла") and (gruppa="Инфографика")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/База_знаний_Венесуэла':
        for ret in cur.execute('SELECT * FROM menu WHERE (country="Венесуэла") and (gruppa="База знаний")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Справки_Северная_Корея':
        for ret in cur.execute('SELECT * FROM menu WHERE country="Северная Корея" and gruppa="Справки"').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Инфографика_Северная_Корея':
        for ret in cur.execute(
                'SELECT * FROM menu WHERE (country="Северная Корея") and (gruppa="Инфографика")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/База_знаний_Северная_Корея':
        for ret in cur.execute(
                'SELECT * FROM menu WHERE (country="Северная Корея") and (gruppa="База знаний")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Справки_Великобритания':
        for ret in cur.execute('SELECT * FROM menu WHERE country="Великобритания" and gruppa="Справки"').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/Инфографика_Великобритания':
        for ret in cur.execute(
                'SELECT * FROM menu WHERE (country="Великобритания") and (gruppa="Инфографика")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if call_name == '/База_знаний_Великобритания':
        for ret in cur.execute(
                'SELECT * FROM menu WHERE (country="Великобритания") and (gruppa="База знаний")').fetchall():
            flag = 1

            await bot.send_document(id, ret[0])
            await bot.send_message(id, f'{ret[1]}\nГруппа: {ret[2]}\nОписание: {ret[-1]}\n')

    if flag == 0:
        await bot.send_message(id, f'Пока нет файлов в этой категории ')


