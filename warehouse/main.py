import os
import dotenv
import funcs
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from asgiref.sync import sync_to_async
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
dotenv.load_dotenv(Path(BASE_DIR, 'venv', '.env'))
token = os.environ['BOT_TOKEN']
bot = Bot(token=token)
dp = Dispatcher(bot)


# start division____________________________________________________________
@dp.message_handler()
async def start(msg: types.Message):
    status = await sync_to_async(funcs.is_client_registered)(msg.from_user.username)
    # await status
    if status:
        await msg.answer(f'{status}')
    else:
        await msg.answer('You are not registered')


@dp.message_handler()
async def send_name(msg: types.Message):
    await msg.answer((f'hello dear full {msg.from_user.full_name}\nand  first {msg.from_user.first_name}'
                      f'\nand last {msg.from_user.username}\nand id {msg.from_user.id}'))


executor.start_polling(dp)
