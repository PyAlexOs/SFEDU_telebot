from API_TOKEN import API_TOKEN
import texts

import asyncio
import logging

from aiogram import Bot, Dispatcher, types
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
            types.KeyboardButton(text='Направления подготовки 👉'),
            types.KeyboardButton(text='Поступление 📄'),
        ],
        [
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
            types.KeyboardButton(text='Общежития 🏠'),
        ],
        [
            types.KeyboardButton(text='Переход с платки 📚'),
            types.KeyboardButton(text='Студпрофком 💼'),
        ],
        [
            types.KeyboardButton(text='Центр карьеры 🔍'),
            types.KeyboardButton(text='Личный кабинет 🔑'),
        ],
        [
            types.KeyboardButton(text='Запись на физическую культуру 🏀'),
            types.KeyboardButton(text='Объединённый совет учащихся 👥💬'),
        ]
    ]

    reply_markup = types.ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True, one_time_keyboard=True,
                                             input_field_placeholder='Выбери нужный раздел')
    await message.answer(texts.okay, reply_markup=reply_markup)


@dp.message(Text('Направления подготовки 👉'))
@dp.message(Text('Поступление 📄'))
@dp.message(Text('Контакты приёмной комиссии ☎️'))
async def abit(message: types.Message):
    text = ''
    keyboard = [[types.InlineKeyboardButton(text='« Назад', callback_data='menu_abit')]]
    reply_markup = types.InlineKeyboardMarkup(inline_keyboard=keyboard, resize_keyboard=True, one_time_keyboard=True)

    if message.text == 'Направления подготовки 👉':
        text = texts.directions

    elif message.text == 'Поступление 📄':
        text = texts.entrance

    elif message.text == 'Контакты приёмной комиссии ☎️':
        text = texts.comission

    await message.answer(text=text, reply_markup=reply_markup)


@dp.message(Text('Общежития 🏠'))
@dp.message(Text('Переход с платки 📚'))
@dp.message(Text('Студпрофком 💼'))
@dp.message(Text('Центр карьеры 🔍'))
@dp.message(Text('Личный кабинет 🔑'))
@dp.message(Text('Запись на физическую культуру 🏀'))
@dp.message(Text('Объединённый совет учащихся 👥💬'))
async def stud(message: types.Message):
    keyboard = [[types.InlineKeyboardButton(text='« Назад', callback_data='menu_stud')]]
    reply_markup = types.InlineKeyboardMarkup(inline_keyboard=keyboard, resize_keyboard=True, one_time_keyboard=True)

    await message.answer(texts.hostel, reply_markup=reply_markup)


@dp.callback_query(Text("menu_stud"))
@dp.callback_query(Text("menu_abit"))
async def redirect_abit(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_reply_markup(reply_markup=None)
    if callback.data == 'menu_abit':
        await menu_abit(callback.message)

    elif callback.data == 'menu_stud':
        await menu_stud(callback.message)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
