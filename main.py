import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ParseMode

API_TOKEN = '5350342940:AAF9LOwZTQx5XtyymigSC-K8Hg3UNYE1ko0'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


def number_seperator(string):
    result = []
    if string:
        for i in string:
            if i in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '/', '*', 'x', '(', ')', '.']:
                result += i
            else:
                pass
        return result


def formatter(string: str):
    try:
        exercise = number_seperator(string)
        if exercise[0] in ['/', '*', '+', '.']:
            del exercise[0]
            if exercise[-1] in ['/', '*', '+', '.']:
                del exercise[-1]
        absolute = ''
        for i in exercise:
            absolute += i
        return eval(absolute)

    except:
        return 'Noto\'ri formatdan foydalandingiz!⚠️'


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(
        "Assalomu alaykum MathBot imizga xush kelibsiz!\nSiz bu bot da tutli qiyinchilikdagi misollarni\nishlashingiz mumkin.")


@dp.message_handler(commands='author')
async def author(message: types.Message):
    await message.answer(
        '<b>Muallif</b>: <code>AlisherITGroup</code>\n'
        '<b>Murojat:</b> @alisher_developer_2005',
        parse_mode=ParseMode.HTML
    )


@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.answer(
        '/start botni ishga tushirish uchun\n'
        '/help yordam uchun\n'
        '/author muallif\n'
        '<b>Botdan quyidagicha foydalanasiz:</b>\n'
        'Qo\'shish: <code>12+1</code>\n'
        'Ayirish: <code>12-3</code>\n'
        'Ko\'paytirish: <code>12*3</code>\n'
        'Bo\'lish: <code>12/3</code>\n'
        'Ifodalarni hisoblash: <code>12+(56-4)/5</code>\n'
        , parse_mode=ParseMode.HTML
    )


@dp.message_handler()
async def echo(message: types.Message):
    msg = message.text
    answer = formatter(msg)
    await message.answer(answer)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
