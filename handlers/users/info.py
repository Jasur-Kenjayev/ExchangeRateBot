from aiogram.types import Message
from loader import dp

@dp.message_handler(text="✅ Channel")
async def kanal(message:
Message):
	msg = "<b>💡Bizning Rasmiy Kanalmiz!\n\n🛠 Quydagi kanalda biz yaratgan yangi turdagi botlarni joylan boramiz ➕Azo bo'lishni unutmang👇\n\n📡 Channel 👉 https://t.me/Python_Koderuz\n\n✅ @KourseBot</b>"
	photo_id = "AgACAgIAAxkBAAIOp2I2EgsCJfubHbeHVLtcR0pKXp9sAAKCuTEbOtWxSULGROTxdizlAQADAgADeQADIwQ"
	await message.answer_photo(photo_id,caption=msg)
	
@dp.message_handler(text="🤖 Bot help")
async def helpi(message:
Message):
	msgi = "<b>🤖 Ushbu Botimiz haqida qisqacha malumot!\n\n📊 Botdagi Valyuta Kursi Malummotlari O'zbekiston Respublikasi Markaziy Bankidan Olinadi ✅\n\n💰Valyuta Kurslari Xar Kuni Ertalab @Valyutalar_Kursiuz Kanaliga Joylanadi Aftamatik Bot Tomonidan ✅\n\n🧮 Botdagi Kalkulyator funksiyasi orqali botmizdagi barcha valyuta kurslarni So'mga hisoblashingiz mumkun✅\n\n💬 Savollar bo'lsa 👉 @SavoIborBot\n\n✅ @KourseBot</b>"
	photo = "AgACAgIAAxkBAAIOpWI2EgclEhXuMb_KHVh5A6a0XVj9AAKBuTEbOtWxSWz3V2mp09MkAQADAgADeAADIwQ"
	await message.answer_photo(photo,caption=msgi)
