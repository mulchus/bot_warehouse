import os
import dotenv
import datetime
import asyncio
import funcs
import markups as m
from emoji import emojize
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from asgiref.sync import sync_to_async
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
dotenv.load_dotenv(Path(BASE_DIR, 'venv', '.env'))
token = os.environ['BOT_TOKEN']
owner_id = os.environ['OWNER_ID']
bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)
today = datetime.date.today()

previous_markup = []


class UserState(StatesGroup):
    mail = State()
    phone = State()
    storage = State()


# start division____________________________________________________________
@dp.message_handler(lambda msg: not msg.text[0] == '/' or msg.text == '/start')
async def start_conversation(msg: types.Message):
    await msg.answer("""Welcome to the Self Storage service!
Seasonal items that take up a lot of space in the apartment are not always convenient to store.
In many cases, there is no place in the apartment for them.
It also happens that things get boring, accumulate and take up all the space, interfering with life, \
but it's a pity to get rid of them.
Renting a small warehouse will solve your problem.""")
    status = await sync_to_async(funcs.identify_user)(msg.from_user.username)
    if status == 'owner':
        await msg.answer(
            f'hello owner, please add to the field "chat_id for Bot" in admin {msg.from_user.id}\n '
            f'for continue type /next')
        await msg.answer(f'glad to see you {emojize(":eyes:")}')
    elif type(status) is int:
        await msg.answer(f'Hi, {msg.from_user.first_name}. You have {status} orders.\n For new order type /cost')
        await msg.answer('Main menu', reply_markup=m.client_start_markup)
    else:
        await msg.answer(f'Hello dear {msg.from_user.first_name},\nbelow you can see FAQ for terms of using our service')
        await msg.answer('Here wee have to input FAQ\nHere wee have to input FAQ\nHere wee have to input FAQ\nHere wee have to input FAQ\n')
        await msg.answer('for calculate cost type /cost')

@dp.message_handler(commands=['cost'])
async def choose_weight(msg: types.Message):
    await msg.answer('choose weight(kg):\n/0_10\n/10_25\n/25_40\n/40_70\n/70_100\n/100_')


@dp.message_handler(commands=['0_10', '10_25', '25_40', '40_70', '70_100', '100_'])
async def get_weigt_component_price(msg: types.Message):
    await msg.answer('koeff')


# end start division___________________________________________________________________________________

# client div____________________________________________________________________________________________
@dp.callback_query_handler(text='faq')
async def callback_inline(call: types.CallbackQuery):
    global previous_markup
    await call.message.delete()
    previous_markup.append('client_start_markup')
    await call.message.answer('Storage conditions... Blah blah blah ....', reply_markup=m.exit_markup)
    await call.answer()


@dp.callback_query_handler(text='put_things')
async def callback_inline(call: types.CallbackQuery):
    global previous_markup
    await call.message.delete()
    previous_markup.append('client_start_markup')
    await call.message.answer('Put things in storage', reply_markup=m.client_put_markup)
    await call.answer()


@dp.callback_query_handler(text='boxes')
async def callback_inline(call: types.CallbackQuery):
    global previous_markup
    await call.message.delete()
    previous_markup.append('client_start_markup')
    await call.message.answer('My boxes: ... \n1.....\n2......\n3.......', reply_markup=m.exit_markup)
    # здесь поместить запрос к БД на отображение списка ячеек хранения с нумерацией
    await call.answer()


@dp.callback_query_handler(text='receiving_addresses')
async def callback_inline(call: types.CallbackQuery):
    global previous_markup
    await call.message.delete()
    previous_markup.append('client_put_markup')
    await call.message.answer('Addresses of receiving items: ... \n1....\n2.....\n3......',
                              reply_markup=m.exit_markup)
    # здесь поместить запрос к БД на отображение списка адресов хранения
    await call.answer()


@dp.callback_query_handler(text='free_shipping')
async def callback_inline(call: types.CallbackQuery):
    global previous_markup
    await call.message.delete()
    previous_markup.append('client_put_markup')
    await call.message.answer('Order free shipping', reply_markup=m.client_things_info_markup)
    # здесь установить признак "Вариант 1"
    await call.answer()


@dp.callback_query_handler(text='bring_myself')
async def callback_inline(call: types.CallbackQuery):
    global previous_markup
    await call.message.delete()
    previous_markup.append('client_put_markup')
    await call.message.answer('I\'ll bring it myself', reply_markup=m.client_things_info_markup)
    # здесь установить признак "Вариант 2"
    await call.answer()


@dp.callback_query_handler(text="exit")
async def callback_inline(call: types.CallbackQuery):
    await call.message.delete()
    if previous_markup[-1] == 'client_start_markup':
        previous_markup.pop()
        await call.message.answer('Main menu', reply_markup=m.client_start_markup)
    elif previous_markup[-1] == 'client_put_markup':
        previous_markup.pop()
        await call.message.answer('Put things in storage', reply_markup=m.client_put_markup)
    elif previous_markup[-1] == 'client_things_info_markup':
        previous_markup.pop()
        await call.message.answer('Put things in storage', reply_markup=m.client_things_info_markup)
    # elif previous_markup[-1] == '':
    #     previous_markup.pop()
    #     await call.message.answer('', reply_markup=m.)
    await call.answer()


@dp.message_handler(commands=['registration'])
async def propose_registration(msg: types.Message):
    chat_id = msg.from_user.id
    await msg.answer('for registration please read document')
    await bot.send_document(chat_id=chat_id, document=open('permitted.pdf', 'rb'))
    await msg.answer('if you agree, type /accept')
    await msg.answer('if you dont agree, type /cancel')


@dp.message_handler(commands=['cancel'])
async def cancel_registration(msg: types.Message):
    await msg.answer('Take care')


@dp.message_handler(commands=['accept'])
async def accept_registration(msg: types.Message):
    client = await sync_to_async(funcs.identify_user)(msg.from_user.username)
    if client == 'Not_reg':
        await msg.answer('Input your email')
        await UserState.mail.set()
    else:
        await msg.answer('You are registered')


@dp.message_handler(lambda msg: not msg.text[0] == '/', state=UserState.mail)
async def registrate_client(msg: types.Message, state: FSMContext):
    chat_id = msg.from_user.id
    tg_account = msg.from_user.username
    mail = msg.text
    await sync_to_async(funcs.registration_client)(tg_account, chat_id, mail)
    await bot.send_message(owner_id, f'new client has been registered,\nchat_id: {chat_id}\ntg_account: {tg_account}')
    await msg.answer('You have been registered\n for list storages type /storages')
    await state.finish()


@dp.message_handler(lambda msg: msg.text[0] == '/', state=UserState.mail)
async def catch_invalid_eail(msg: types.Message):
    await msg.answer('Incorrect email, repeat input')


@dp.message_handler(commands=['storages'])
async def output_list_sorages(msg: types.Message):
    storages = await sync_to_async(funcs.get_available_storages)()
    for storage in storages:
        await msg.answer(
            f'№ storage: {storage.id}\naddress storage: {storage.address}\navailable area: {await sync_to_async(storage.free_space)()}\n===========')
    await msg.answer('for make new order type № of storage\nfor cancel type /cancel')
    await UserState.storage.set()


@dp.message_handler(lambda msg: msg.text[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
                    state=UserState.storage)
async def choose_storage(msg: types.Message, state: FSMContext):
    await msg.answer('all is good')
    await state.finish()


@dp.message_handler(lambda msg: msg.text[0] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
                    state=UserState.storage)
async def catch_invalid_storage(msg: types.Message):
    await msg.answer('Incorrect №, repeat input')


async def sentinel():
    while 1:
        whole_orders = await sync_to_async(funcs.get_terms_orders)()
        for orders in whole_orders[:-1]:
            for order in orders:
                await bot.send_message(order['chat_id'],
                                       f'{-order["expired days"]} days till expired your order {order["order"]}')
        for order in whole_orders[-1]:
            await bot.send_message(order['chat_id'],
                                   f'expired order: {order["order"]},\nclient: {order["client"]}\nstorage: {order["storage"]}\n'
                                   f'expired days: {order["expired days"]}\n===========')
            await bot.send_message(owner_id,
                                   f'expired order: {order["order"]},\nclient: {order["client"]}\nstorage: {order["storage"]}\n'
                                   f'expired days: {order["expired days"]}\n===========')
        await asyncio.sleep(86400)


async def on_startup(_):
    asyncio.create_task(sentinel())


executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
