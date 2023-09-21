from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hlink
from pars import main, get_date


TOKEN = '6433976747:AAFN3nhTGjvivAFnY6IffPPLGybE7-OHUVg'
url = 'https://kaktus.media/?lable=8&date=2023-09-21&order=time'

bot = Bot(TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
date = str
data = []

@dp.message_handler(commands='start')
async def start(message: types.Message):
    global date, data
    btn1 = types.InlineKeyboardButton('Вывести все новости', callback_data='button1')
    inline_kb1 = types.InlineKeyboardMarkup().row(btn1)
    btn2 = 'Quit'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(btn2)


    await message.answer("Сбор новостей за сегодня...", reply_markup=markup)
    date = get_date(url)
    data = main(url)
    await message.answer("Сбор новостей завершен, что делать", reply_markup=inline_kb1)

@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Ща все будет')
    await bot.send_message(callback_query.from_user.id, f'Дата новостей {date}')

    

    count = 1
    for i in range(len(data)):
        keys = str(data[i].keys())[12:-3]
        links = str(data[i].values())[14:-3]
        new = f'{count}.{hlink(str(keys), str(links))}'
        await bot.send_message(callback_query.from_user.id, new)
        count += 1
    

@dp.message_handler(Text(equals='Quit'))
async def get_quit(message: types.Message):
    await message.answer('Досвидания')


executor.start_polling(dp)




