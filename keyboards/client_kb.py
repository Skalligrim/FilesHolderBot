from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup

b1=KeyboardButton('/Индия')
b2=KeyboardButton('/США')
b3=KeyboardButton('/Саудовская_Аравия')
b4=KeyboardButton('/Вьетнам')
b5=KeyboardButton('/Израиль')
b6=KeyboardButton('/ОАЭ')
b7=KeyboardButton('/Аргентина')
b8=KeyboardButton('/Боливия')
b9=KeyboardButton('/Бразилия')
b10=KeyboardButton('/Колумбия')
b11=KeyboardButton('/Великобритания')
b12=KeyboardButton('/Куба')
b13=KeyboardButton('/Мексика')
b14=KeyboardButton('/Никарагуа')
b15=KeyboardButton('/Чили')
b16=KeyboardButton('/Эквадор')
b17=KeyboardButton('/Латинская_Америка')
b18=KeyboardButton('/Россия_и_международное_взаимодействие')
b19=KeyboardButton('/Северная_Корея')
b20=KeyboardButton('/Китай')
b21=KeyboardButton('/Иран')
b22=KeyboardButton('/Турция')
b23=KeyboardButton('/Венесуэла')
b24=KeyboardButton('/Компаративистика')
b25=KeyboardButton('/Концептуальные_документы')

b26=KeyboardButton('/меню')

kb_client=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23).row(b24,b25)

inline_btn_1 = InlineKeyboardButton(text='/Справки', callback_data='/Справки_США')
inline_btn_2 = InlineKeyboardButton(text='/База_знаний', callback_data='/База_знаний_США')
inline_btn_3 = InlineKeyboardButton(text='/Инфографика', callback_data='/Инфографика_США')
inline_kb_USA = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2).add(inline_btn_3)

inline_btn_1 = InlineKeyboardButton(text='/Справки', callback_data='/Справки_Вьетнам')
inline_btn_2 = InlineKeyboardButton(text='/База_знаний', callback_data='/База_знаний_Вьетнам')
inline_btn_3 = InlineKeyboardButton(text='/Инфографика', callback_data='/Инфографика_Вьетнам')
inline_kb_Vietnam = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2).add(inline_btn_3)

inline_btn_1 = InlineKeyboardButton(text='/Справки', callback_data='/Справки_Израиль')
inline_btn_2 = InlineKeyboardButton(text='/База_знаний', callback_data='/База_знаний_Израиль')
inline_btn_3 = InlineKeyboardButton(text='/Инфографика', callback_data='/Инфографика_Израиль')
inline_kb_Israel = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2).add(inline_btn_3)

inline_btn_1 = InlineKeyboardButton(text='/Справки', callback_data='/Справки_ОАЭ')
inline_btn_2 = InlineKeyboardButton(text='/База_знаний', callback_data='/База_знаний_ОАЭ')
inline_btn_3 = InlineKeyboardButton(text='/Инфографика', callback_data='/Инфографика_ОАЭ')
inline_kb_UAE = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2).add(inline_btn_3)

inline_btn_1 = InlineKeyboardButton(text='/Справки', callback_data='/Справки_Саудовская_Аравия')
inline_btn_2 = InlineKeyboardButton(text='/База_знаний', callback_data='/База_знаний_Саудовская_Аравия')
inline_btn_3 = InlineKeyboardButton(text='/Инфографика', callback_data='/Инфографика_Саудовская_Аравия')
inline_kb_Saudi_Arabia = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2).add(inline_btn_3)

inline_btn_1 = InlineKeyboardButton(text='/Справки', callback_data='/Справки_Индия')
inline_btn_2 = InlineKeyboardButton(text='/База_знаний', callback_data='/База_знаний_Индия')
inline_btn_3 = InlineKeyboardButton(text='/Инфографика', callback_data='/Инфографика_Индия')
inline_kb_India = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2).add(inline_btn_3)

inline_btn_1 = InlineKeyboardButton(text='/Справки', callback_data='/Справки_Аргентина')
inline_btn_2 = InlineKeyboardButton(text='/База_знаний', callback_data='/База_знаний_Аргентина')
inline_btn_3 = InlineKeyboardButton(text='/Инфографика', callback_data='/Инфографика_Аргентина')
inline_kb_Argentina = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2).add(inline_btn_3)

inline_btn_1 = InlineKeyboardButton(text='/Справки', callback_data='/Справки_Боливия')
inline_btn_2 = InlineKeyboardButton(text='/База_знаний', callback_data='/База_знаний_Боливия')
inline_btn_3 = InlineKeyboardButton(text='/Инфографика', callback_data='/Инфографика_Боливия')
inline_kb_Bolivia = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2).add(inline_btn_3)

inline_btn_1 = InlineKeyboardButton(text='/Справки', callback_data='/Справки_Бразилия')
inline_btn_2 = InlineKeyboardButton(text='/База_знаний', callback_data='/База_знаний_Бразилия')
inline_btn_3 = InlineKeyboardButton(text='/Инфографика', callback_data='/Инфографика_Бразилия')
inline_kb_Brazilia = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2).add(inline_btn_3)

inline_btn_1 = InlineKeyboardButton(text='/Справки', callback_data='/Справки_Колумбия')
inline_btn_2 = InlineKeyboardButton(text='/База_знаний', callback_data='/База_знаний_Колумбия')
inline_btn_3 = InlineKeyboardButton(text='/Инфографика', callback_data='/Инфографика_Колумбия')
inline_kb_Kolumbia = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2).add(inline_btn_3)

inline_btn_1 = InlineKeyboardButton(text='/Справки', callback_data='/Справки_Компаративистика')
inline_btn_2 = InlineKeyboardButton(text='/База_знаний', callback_data='/База_знаний_Компаративистика')
inline_btn_3 = InlineKeyboardButton(text='/Инфографика', callback_data='/Инфографика_Компаративистика')
inline_kb_Komparativistika = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2).add(inline_btn_3)

inline_btn_1 = InlineKeyboardButton(text='/Справки', callback_data='/Справки_Куба')
inline_btn_2 = InlineKeyboardButton(text='/База_знаний', callback_data='/База_знаний_Куба')
inline_btn_3 = InlineKeyboardButton(text='/Инфографика', callback_data='/Инфографика_Куба')
inline_kb_Kuba = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2).add(inline_btn_3)


inline_btn_1 = InlineKeyboardButton(text='/Справки', callback_data='/Справки_Мексика')
inline_btn_2 = InlineKeyboardButton(text='/База_знаний', callback_data='/База_знаний_Мексика')
inline_btn_3 = InlineKeyboardButton(text='/Инфографика', callback_data='/Инфографика_Мексика')
inline_kb_Mexico = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2).add(inline_btn_3)

inline_btn_1 = InlineKeyboardButton(text='/Справки', callback_data='/Справки_Никарагуа')
inline_btn_2 = InlineKeyboardButton(text='/База_знаний', callback_data='/База_знаний_Никарагуа')
inline_btn_3 = InlineKeyboardButton(text='/Инфографика', callback_data='/Инфографика_Никарагуа')
inline_kb_Nicaragua = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2).add(inline_btn_3)

inline_btn_1 = InlineKeyboardButton(text='/Справки', callback_data='/Справки_Чили')
inline_btn_2 = InlineKeyboardButton(text='/База_знаний', callback_data='/База_знаний_Чили')
inline_btn_3 = InlineKeyboardButton(text='/Инфографика', callback_data='/Инфографика_Чили')
inline_kb_Chile = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2).add(inline_btn_3)

inline_btn_1 = InlineKeyboardButton(text='/Справки', callback_data='/Справки_Эквадор')
inline_btn_2 = InlineKeyboardButton(text='/База_знаний', callback_data='/База_знаний_Эквадор')
inline_btn_3 = InlineKeyboardButton(text='/Инфографика', callback_data='/Инфографика_Эквадор')
inline_kb_Ecuador = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2).add(inline_btn_3)


inline_btn_1 = InlineKeyboardButton(text='/Справки', callback_data='/Справки_Латинская_Америка')
inline_btn_2 = InlineKeyboardButton(text='/База_знаний', callback_data='/База_знаний_Латинская_Америка')
inline_btn_3 = InlineKeyboardButton(text='/Инфографика', callback_data='/Инфографика_Латинская_Америка')
inline_kb_Latin_America = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2).add(inline_btn_3)

inline_btn_1 = InlineKeyboardButton(text='/Справки', callback_data='/Справки_Россия_и_МВ')
inline_btn_2 = InlineKeyboardButton(text='/База_знаний', callback_data='/База_знаний_Россия_и_МВ')
inline_btn_3 = InlineKeyboardButton(text='/Инфографика', callback_data='/Инфографика_Россия_и_МВ')
inline_kb_RussiaAndIC = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2).add(inline_btn_3)

inline_btn_1 = InlineKeyboardButton(text='/Справки', callback_data='/Справки_Концепт_док')
inline_btn_2 = InlineKeyboardButton(text='/База_знаний', callback_data='/База_знаний_Концепт_док')
inline_btn_3 = InlineKeyboardButton(text='/Инфографика', callback_data='/Инфографика_Концепт_док')
inline_kb_Concept_Papers = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2).add(inline_btn_3)

inline_btn_1 = InlineKeyboardButton(text='/Справки', callback_data='/Справки_Китай')
inline_btn_2 = InlineKeyboardButton(text='/База_знаний', callback_data='/База_знаний_Китай')
inline_btn_3 = InlineKeyboardButton(text='/Инфографика', callback_data='/Инфографика_Китай')
inline_kb_China = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2).add(inline_btn_3)

inline_btn_1 = InlineKeyboardButton(text='/Справки', callback_data='/Справки_Иран')
inline_btn_2 = InlineKeyboardButton(text='/База_знаний', callback_data='/База_знаний_Иран')
inline_btn_3 = InlineKeyboardButton(text='/Инфографика', callback_data='/Инфографика_Иран')
inline_kb_Iran = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2).add(inline_btn_3)

inline_btn_1 = InlineKeyboardButton(text='/Справки', callback_data='/Справки_Турция')
inline_btn_2 = InlineKeyboardButton(text='/База_знаний', callback_data='/База_знаний_Турция')
inline_btn_3 = InlineKeyboardButton(text='/Инфографика', callback_data='/Инфографика_Турция')
inline_kb_Turkey = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2).add(inline_btn_3)

inline_btn_1 = InlineKeyboardButton(text='/Справки', callback_data='/Справки_Венесуэла')
inline_btn_2 = InlineKeyboardButton(text='/База_знаний', callback_data='/База_знаний_Венесуэла')
inline_btn_3 = InlineKeyboardButton(text='/Инфографика', callback_data='/Инфографика_Венесуэла')
inline_kb_Venezuela = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2).add(inline_btn_3)

inline_btn_1 = InlineKeyboardButton(text='/Справки', callback_data='/Справки_Северная_Корея')
inline_btn_2 = InlineKeyboardButton(text='/База_знаний', callback_data='/База_знаний_Северная_Корея')
inline_btn_3 = InlineKeyboardButton(text='/Инфографика', callback_data='/Инфографика_Северная_Корея')
inline_kb_North_Korea = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2).add(inline_btn_3)

inline_btn_1 = InlineKeyboardButton(text='/Справки', callback_data='/Справки_Великобритания')
inline_btn_2 = InlineKeyboardButton(text='/База_знаний', callback_data='/База_знаний_Великобритания')
inline_btn_3 = InlineKeyboardButton(text='/Инфографика', callback_data='/Инфографика_Великобритания')
inline_kb_Great_Britain = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2).add(inline_btn_3)




