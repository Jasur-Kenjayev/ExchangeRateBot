import sqlite3
from aiogram.types import ParseMode, Message
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menuKeyboard import menu
from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
    	pass

    await message.answer(f"*👋 Assalomu Alaykum Xurmatli {message.from_user.full_name}\n\n🤖 Ushbu Bot Orqali 💶Kurslarni 📈Ko'tarlishi va Tushushni📉 Kuzatib Borishingiz Mumkun.\n\n✅ @KourseBot*",parse_mode=ParseMode.MARKDOWN,reply_markup=menu)
    count = db.count_users()[0]
    msg = f"*{message.from_user.full_name} 💡Bazaga Yangi 👤Foydalanuvchi ➕Qo'shildi. Bazada {count} ta Foydalanuvchi Bor✅*"
    await bot.send_message(chat_id=ADMINS[0], text=msg,parse_mode=ParseMode.MARKDOWN)