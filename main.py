from API_TOKEN import API_TOKEN
import texts

import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, Text
from aiogram.utils.keyboard import InlineKeyboardBuilder

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher()


@dp.message(Command('start', 'role'))
async def start(message: types.Message):
    if message.text == '/start':
        await message.answer(texts.hello)

    keyboard = [[
        types.KeyboardButton(text='Для абитуриента 🎒'),
        types.KeyboardButton(text='Для студента 🎓')
    ]]

    reply_markup = types.ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True,
                                             input_field_placeholder='Подскажи, кто ты?')
    await message.answer('Какую информацию ты хочешь видеть?', reply_markup=reply_markup)


@dp.message(Text('Для абитуриента 🎒'))
async def menu_abit(message: types.Message):
    keyboard = [
        [
            types.KeyboardButton(text='Поступление 📄'),
            types.KeyboardButton(text='Общежития 🏠'),
        ],
        [
            types.KeyboardButton(text='Направления подготовки 👉'),
            types.KeyboardButton(text='Контакты приёмной комиссии ☎️'),
        ]
    ]

    reply_markup = types.ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True, one_time_keyboard=True,
                                             input_field_placeholder='Выбери нужный раздел')
    await message.answer(texts.okay, reply_markup=reply_markup)


@dp.message(Text('Для студента 🎓'))
async def menu_stud(message: types.Message):
    keyboard = [
        [
            types.KeyboardButton(text='Стипендии 💰'),
            types.KeyboardButton(text='Переход с платки 📚'),
        ],
        [
            types.KeyboardButton(text='Студпрофком 💼'),
            types.KeyboardButton(text='Центр карьеры 🔍'),
        ],
        [
            types.KeyboardButton(text='Личный кабинет 🔑'),
            types.KeyboardButton(text='Запись на ФЗК 🏀'),
        ],
        [
            types.KeyboardButton(text='Объединённый совет учащихся 👥💬'),
        ]
    ]

    reply_markup = types.ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True, one_time_keyboard=True,
                                             input_field_placeholder='Выбери нужный раздел')
    await message.answer(texts.okay, reply_markup=reply_markup)


@dp.message(Text('Поступление 📄'))
@dp.message(Text('Общежития 🏠'))
@dp.message(Text('Направления подготовки 👉'))
@dp.message(Text('Контакты приёмной комиссии ☎️'))
async def abit(message: types.Message):
    text = ''
    keyboard = [[types.InlineKeyboardButton(text='« Назад', callback_data='menu_abit')]]
    reply_markup = types.InlineKeyboardMarkup(inline_keyboard=keyboard, resize_keyboard=True, one_time_keyboard=True)

    if message.text == 'Направления подготовки 👉':
        text = texts.directions

    if message.text == 'Общежития 🏠':
        text = texts.hostel

    elif message.text == 'Поступление 📄':
        text = texts.entrance

    elif message.text == 'Контакты приёмной комиссии ☎️':
        text = texts.comission

    await message.answer(text=text, reply_markup=reply_markup)


@dp.message(Text('Переход с платки 📚'))
@dp.message(Text('Студпрофком 💼'))
@dp.message(Text('Центр карьеры 🔍'))
@dp.message(Text('Личный кабинет 🔑'))
@dp.message(Text('Запись на ФЗК 🏀'))
@dp.message(Text('Объединённый совет учащихся 👥💬'))
async def stud(message: types.Message):
    keyboard = [[types.InlineKeyboardButton(text='« Назад', callback_data='menu_stud')]]
    reply_markup = types.InlineKeyboardMarkup(inline_keyboard=keyboard, resize_keyboard=True, one_time_keyboard=True)

    if message.text == 'Переход с платки 📚':
        text = texts.become_free
        file = 'BQACAgIAAxkBAAIFOGRhRWXeQ-DM_rFLLxly6iGHoksbAAJ-MAACzgwJS7KAwbbVesiqLwQ'
        await message.answer_document(file)
        await message.answer(text=text, reply_markup=reply_markup)

    elif message.text == 'Студпрофком 💼':
        text = texts.studprofcom
        await message.answer(text=text, reply_markup=reply_markup)

    elif message.text == 'Центр карьеры 🔍':
        text = texts.career
        await message.answer(text=text, reply_markup=reply_markup)

    elif message.text == 'Личный кабинет 🔑':
        text = texts.lk
        photos = [
            types.InputMediaPhoto(
                media='AgACAgIAAxkBAAIFVWRhR0e4w2zYB14ZfJkkA5sYT1IYAAIczTEbzgwJS9dKTqpYROf0AQADAgADeQADLwQ'),
            types.InputMediaPhoto(
                media='AgACAgIAAxkBAAIFVmRhR04al8KY1HMkzyiIiaWnUmAjAAIdzTEbzgwJSxWTCRhseLmRAQADAgADeQADLwQ')
        ]

        await message.answer_media_group(photos)
        await message.answer(text=text, reply_markup=reply_markup)

    elif message.text == 'Запись на ФЗК 🏀':
        text = texts.phys_ed
        photo = 'AgACAgIAAxkBAAIFV2RhR1Lr-Mk5AAF3SLjBPwgXZCwj5wACHs0xG84MCUsQpYTDJJyyUAEAAwIAA3kAAy8E'
        await message.answer_photo(photo=photo, caption=text, reply_markup=reply_markup)

    elif message.text == 'Объединённый совет учащихся 👥💬':
        text = texts.oso
        await message.answer(text=text, reply_markup=reply_markup)


@dp.message(Text('Стипендии 💰'))
async def get_money(message: types.Message):
    keyboard = [
        [types.InlineKeyboardButton(text='Академическая стипендия', callback_data='st_acad')],
        [types.InlineKeyboardButton(text='Повышенная академическая стипендия', callback_data='st_acad_pow')],
        [types.InlineKeyboardButton(text='Государственная социальная стипендия', callback_data='st_gov')],
        [types.InlineKeyboardButton(text='Государственная социальная стипендия 1-2 курсов (стимулирующая выплата)',
                                    callback_data='st_gov_plus')],
        [types.InlineKeyboardButton(text='Стипендии президента и правительства РФ', callback_data='st_prez')],
        [types.InlineKeyboardButton(text='Именные стипендии', callback_data='st_named')],
        [types.InlineKeyboardButton(text='« Назад', callback_data='menu_stud')],
    ]

    reply_markup = types.InlineKeyboardMarkup(inline_keyboard=keyboard, resize_keyboard=True, one_time_keyboard=True)
    await message.answer(text='Выбери интересующую тебя стипендию и я о ней расскажу', reply_markup=reply_markup)


@dp.callback_query(Text("st_acad"))
@dp.callback_query(Text("st_acad_pow"))
@dp.callback_query(Text("st_gov"))
@dp.callback_query(Text("st_gov_plus"))
@dp.callback_query(Text("st_prez"))
@dp.callback_query(Text("st_named"))
async def redirect(callback: types.CallbackQuery):
    text, header = '', ''
    keyboard = [[types.InlineKeyboardButton(text='« Назад', callback_data='st')]]
    reply_markup = types.InlineKeyboardMarkup(inline_keyboard=keyboard, resize_keyboard=True, one_time_keyboard=True)
    await callback.answer()

    if callback.data == 'st_named':
        await callback.message.edit_text(text='<b>Именные стипендии</b>', reply_markup=None)

        files = [
            types.InputMediaDocument(
                media='BQACAgIAAxkBAAIHbWRhZ2htrznZOSEdaqanv9EdBUSpAALCMAACzgwJS1Yv-LFVQgfaLwQ'),
            types.InputMediaDocument(
                media='BQACAgIAAxkBAAIHbmRhZ3RUJIWnzDjFGjihrmZKKq-fAALDMAACzgwJS7Qsh4cC56LJLwQ')
        ]

        await callback.message.answer_media_group(files)
        await callback.message.answer(text=texts.st_named, reply_markup=reply_markup)

    else:
        if callback.data == 'st_acad':
            header = 'Академическая стипендия'
            text = texts.st_acad

        elif callback.data == 'st_acad_pow':
            header = 'Повышенная академическая стипендия'
            text = texts.st_acad_pow

        elif callback.data == 'st_gov':
            header = 'Государственная социальная стипендия'
            text = texts.st_gov

        elif callback.data == 'st_gov_plus':
            header = 'Государственная социальная стипендия 1-2 курсов (стимулирующая выплата)'
            text = texts.st_gov_plus

        elif callback.data == 'st_prez':
            header = 'Стипендии президента и правительства РФ'
            text = texts.st_prez

        await callback.message.edit_text(text=f'<b>{header}</b>', reply_markup=None)
        await callback.message.answer(text=text, reply_markup=reply_markup)


@dp.callback_query(Text("menu_stud"))
@dp.callback_query(Text("menu_abit"))
@dp.callback_query(Text("st"))
async def redirect(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_reply_markup(reply_markup=None)
    if callback.data == 'menu_abit':
        await menu_abit(callback.message)

    elif callback.data == 'menu_stud':
        await menu_stud(callback.message)

    elif callback.data == 'st':
        await get_money(callback.message)


"""@dp.message(F.photo)
async def get_photo_id(message: types.Message):
    print(message.photo[-1].file_id)"""


"""@dp.message()
async def get_doc_id(message: types.Message):
    print(message.document.file_id)"""


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
