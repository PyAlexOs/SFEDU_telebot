import texts
import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, Text

logging.basicConfig(level=logging.INFO)
bot = Bot(token='', parse_mode="HTML")
dp = Dispatcher()


@dp.message(Command('start'))
async def start(message: types.Message):
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

    reply_markup = types.ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True,
                                             input_field_placeholder='Выбери нужный раздел')
    await message.answer('Отлично! Что ты хочешь узнать?', reply_markup=reply_markup)


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

    reply_markup = types.ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True,
                                             input_field_placeholder='Выбери нужный раздел')
    await message.answer('Отлично! Что ты хочешь узнать?', reply_markup=reply_markup)


@dp.message(Text('Направления подготовки 👉'))
async def directions(message: types.Message):
    keyboard = [[types.KeyboardButton(text='« Назад')]]

    reply_markup = types.ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
    await message.answer(texts.directions, reply_markup=reply_markup)


@dp.message(Text('Поступление 📄'))
async def entrance(message: types.Message):
    keyboard = [[types.KeyboardButton(text='« Назад')]]

    reply_markup = types.ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
    await message.answer(texts.entrance, reply_markup=reply_markup)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
