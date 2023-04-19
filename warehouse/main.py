import os
import dotenv
import asyncio
import funcs
from emoji import emojize
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
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


class UserState(StatesGroup):
    mail = State()
    phone = State()


# start division____________________________________________________________
@dp.message_handler(lambda msg: not msg.text[0] == '/' or msg.text == '/start')
async def start_conversation(msg: types.Message):
    status = await sync_to_async(funcs.identify_user)(msg.from_user.username)
    if status == 'owner':
        await msg.answer(
            f'hello owner, please add to the field "chat_id for Bot" in admin {msg.from_user.id}\n for continue type /next')
        await msg.answer(f'glad to see you {emojize(":eyes:")}')
    elif type(status) is int:
        await msg.answer(f'hi {msg.from_user.first_name} you have {status} orders')
    else:
        await msg.answer(f'Hello dear {msg.from_user.first_name},\nsorry, but you are not registered')
        await msg.answer('some .................\ncool..................\npromotion')
        await msg.answer('Wanna join? type /registration')


# end start division___________________________________________________________________________________

# client div____________________________________________________________________________________________
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
async def accept_registration(msg: types.Message, state: FSMContext):
    chat_id = msg.from_user.id
    tg_account = msg.from_user.username
    mail = msg.text
    await sync_to_async(funcs.registration_client)(tg_account, chat_id, mail)
    await bot.send_message(owner_id, f'new client has been registered,\nchat_id: {chat_id}\ntg_account: {tg_account}')
    await msg.answer('You have been registered')
    await state.finish()


@dp.message_handler(lambda msg: msg.text[0] == '/', state=UserState.mail)
async def accept_registration(msg: types.Message):
    await msg.answer('Incorrect email, repeat input')

executor.start_polling(dp)
