from aiogram.types import Message

from API_TOKEN import API_TOKEN
import texts

import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher()


@dp.message(Command('start', 'menu'))
async def start(message: types.Message):
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
            types.KeyboardButton(text='Домашнее задание ✏️'),
            types.KeyboardButton(text='Запись на ФЗК 🏀'),
        ],
        [
            types.KeyboardButton(text='Психологический клуб «Лифт» 🚀'),
        ],
        [
            types.KeyboardButton(text='Объединённый совет учащихся 👥💬'),
        ]
    ]

    reply_markup = types.ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True, one_time_keyboard=True,
                                             input_field_placeholder='Выбери нужный раздел')
    if message.text == '/start':
        await message.answer(texts.hello + "\n" + texts.action, reply_markup=reply_markup)
    else:
        await message.answer(texts.action, reply_markup=reply_markup)


@dp.message(F.text)
async def stud(message: types.Message):
    keyboard = [[types.InlineKeyboardButton(text='« Назад', callback_data='menu_stud')]]
    reply_markup = types.InlineKeyboardMarkup(inline_keyboard=keyboard, resize_keyboard=True, one_time_keyboard=True)

    if message.text == 'Переход с платки 📚':
        await message.answer(text=texts.become_free, reply_markup=reply_markup)

    elif message.text == 'Студпрофком 💼':
        await message.answer(text=texts.studprofcom, reply_markup=reply_markup)

    elif message.text == 'Центр карьеры 🔍':
        await message.answer(text=texts.career, reply_markup=reply_markup)

    elif message.text == 'Домашнее задание ✏️':
        await message.answer(text=texts.homework, reply_markup=reply_markup)

    elif message.text == 'Запись на ФЗК 🏀':
        await message.answer(text=texts.phys_ed, reply_markup=reply_markup)

    elif message.text == 'Психологический клуб «Лифт» 🚀':
        await message.answer(text=texts.education, reply_markup=reply_markup)

    elif message.text == 'Объединённый совет учащихся 👥💬':
        await message.answer(text=texts.oso, reply_markup=reply_markup)

    else:
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


@dp.callback_query(F.data)
async def st(callback: types.CallbackQuery):
    keyboard = [[types.InlineKeyboardButton(text='« Назад', callback_data='st')]]
    reply_markup = types.InlineKeyboardMarkup(inline_keyboard=keyboard, resize_keyboard=True, one_time_keyboard=True)
    await callback.answer()

    if callback.data == 'st_named':
        await callback.message.edit_text(text=f'<b>Именные стипендии</b>', reply_markup=None)
        await callback.message.answer(text=texts.st_named, reply_markup=reply_markup)

    elif callback.data == 'st_acad':
        await callback.message.edit_text(text=f'<b>Академическая стипендия</b>', reply_markup=None)
        await callback.message.answer(text=texts.st_acad, reply_markup=reply_markup)

    elif callback.data == 'st_acad_pow':
        await callback.message.edit_text(text=f'<b>Повышенная академическая стипендия</b>', reply_markup=None)
        await callback.message.answer(text=texts.st_acad_pow, reply_markup=reply_markup)

    elif callback.data == 'st_gov':
        await callback.message.edit_text(text=f'<b>Государственная социальная стипендия</b>', reply_markup=None)
        await callback.message.answer(text=texts.st_gov, reply_markup=reply_markup)

    elif callback.data == 'st_gov_plus':
        await callback.message.edit_text(text=f'<b>Государственная социальная стипендия 1-2 курсов (стимулирующая выплата)</b>', reply_markup=None)
        await callback.message.answer(text=texts.st_gov_plus, reply_markup=reply_markup)

    elif callback.data == 'st_prez':
        await callback.message.edit_text(text=f'<b>Стипендии президента и правительства РФ</b>', reply_markup=None)
        await callback.message.answer(text=texts.st_prez, reply_markup=reply_markup)

    elif callback.data == 'menu_stud':
        await callback.message.edit_reply_markup(reply_markup=None)
        await start(callback.message)

    elif callback.data == 'st':
        await callback.message.edit_reply_markup(reply_markup=None)
        await stud(callback.message)


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
