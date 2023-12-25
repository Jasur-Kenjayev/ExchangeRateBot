import logging
from loader import dp
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from keyboards.inline.back import Back
from aiogram.dispatcher import FSMContext
from keyboards.inline.kursm import categoryMenu
import datetime
import pytz
import requests
import json
from pprint import pprint as print

@dp.message_handler(text = "📊 Valyuta Kursi")
async def menukurs(message:
	types.Message):
	await message.answer("<b>Marhammat Kerakli Valyutani Tanlang!</b>",reply_markup=categoryMenu)
	
@dp.callback_query_handler(text_contains="backs")
async def backs(call: CallbackQuery):
	await call.message.answer("<b>Marhammat Kerakli Valyutani Tanlang!</b>",reply_markup=categoryMenu)
	await call.message.delete()
	await call.answer(cache_time=60)

def soat():
	utc_now = pytz.utc.localize(datetime.datetime.utcnow())
	pst_now = utc_now.astimezone(pytz.timezone("Asia/Tashkent"))
	dt_string = pst_now.strftime("%d.%m.%Y-YIL\n⏰ Soat 👉 %H:%M:%S")
	return dt_string
	
@dp.callback_query_handler(text_contains="usdu")
async def usd(call: CallbackQuery):
	url1 = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/USD/UZS'
	r = requests.get(url1).json()
	result1 = (r[0]['Rate'])
	form1 = f"<b>📆 Bugun 👉 {soat()}</b>\n\n1⃣ 🇺🇸 Dollar =<b> {result1} So'm\n\n✅ @KourseBot</b>"
	await call.message.answer(form1,reply_markup=Back)
	await call.message.delete()
	await call.answer(cache_time=60)
	
@dp.callback_query_handler(text_contains="evu")
async def evro(call: CallbackQuery):
	url2 = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/EUR/UZS'
	r2 = requests.get(url2).json()
	result2 = (r2[0]['Rate'])
	form2 = f"<b>📆 Bugun 👉 {soat()}</b>\n\n1⃣ 🇪🇺 Yevro = <b>{result2} So'm\n\n✅ @KourseBot</b>"
	await call.message.answer(form2,reply_markup=Back)
	await call.message.delete()
	await call.answer(cache_time=60)
	
@dp.callback_query_handler(text_contains="ruu")
async def rub(call: CallbackQuery):
	url3 = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/RUB/UZS'
	r3 = requests.get(url3).json()
	result3 = (r3[0]['Rate'])
	form3 = f"<b>📆 Bugun 👉 {soat()}</b>\n\n1⃣ 🇷🇺 Rubl = <b>{result3} So'm\n\n✅ @KourseBot</b>"
	await call.message.answer(form3,reply_markup=Back)
	await call.message.delete()
	await call.answer(cache_time=60)
	
@dp.callback_query_handler(text_contains="somu")
async def som(call: CallbackQuery):
	url4 = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/KGS/UZS'
	r4 = requests.get(url4).json()
	result4 = (r4[0]['Rate'])
	form4 = f"<b>📆 Bugun 👉 {soat()}</b>\n\n1⃣ 🇰🇬 Som = <b>{result4} So'm\n\n✅ @KourseBot</b>"
	await call.message.answer(form4,reply_markup=Back)
	await call.message.delete()
	await call.answer(cache_time=60)
	
@dp.callback_query_handler(text_contains="afgu")
async def afgani(call: CallbackQuery):
	url5 = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/AFN/UZS'
	r5 = requests.get(url5).json()
	result5 = (r5[0]['Rate'])
	form5 = f"<b>📆 Bugun 👉 {soat()}</b>\n\n1⃣ 🇦🇫 Afg'ani = <b>{result5} So'm\n\n✅ @KourseBot</b>"
	await call.message.answer(form5,reply_markup=Back)
	await call.message.delete()
	await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains="tenu")
async def tenga(call: CallbackQuery):
	url6 = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/KZT/UZS'
	r6 = requests.get(url6).json()
	result6 = (r6[0]['Rate'])
	form6 = f"<b>📆 Bugun 👉 {soat()}</b>\n\n1⃣ 🇰🇿 Tenge = <b>{result6} So'm\n\n✅ @KourseBot</b>"
	await call.message.answer(form6,reply_markup=Back)
	await call.message.delete()
	await call.answer(cache_time=60)
	
@dp.callback_query_handler(text_contains="tjsu")
async def tjsuu(call: CallbackQuery):
	url7 = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/TJS/UZS'
	r7 = requests.get(url7).json()
	result7 = (r7[0]['Rate'])
	form7 = f"<b>📆 Bugun 👉 {soat()}</b>\n\n1⃣ 🇹🇯 Somoni = <b>{result7} So'm\n\n✅ @KourseBot</b>"
	await call.message.answer(form7,reply_markup=Back)
	await call.message.delete()
	await call.answer(cache_time=60)
	
@dp.callback_query_handler(text_contains="tmtu")
async def tmtt(call: CallbackQuery):
	url8 = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/TMT/UZS'
	r8 = requests.get(url8).json()
	result8 = (r8[0]['Rate'])
	form8 = f"<b>📆 Bugun 👉 {soat()}</b>\n\n1⃣ 🇹🇲 Manat = <b>{result8} So'm\n\n✅ @KourseBot</b>"
	await call.message.answer(form8,reply_markup=Back)
	await call.message.delete()
	await call.answer(cache_time=60)
	
@dp.callback_query_handler(text_contains="funtu")
async def funtt(call: CallbackQuery):
	url9 = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/GBP/UZS'
	r9 = requests.get(url9).json()
	result9 = (r9[0]['Rate'])
	form9 = f"<b>📆 Bugun 👉 {soat()}</b>\n\n1⃣ 🇬🇧 Funt = <b>{result9} So'm\n\n✅ @KourseBot</b>"
	await call.message.answer(form9,reply_markup=Back)
	await call.message.delete()
	await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains="yuanu")
async def yuani(call: CallbackQuery):
	url11 = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/CNY/UZS'
	r11 = requests.get(url11).json()
	result11 = (r11[0]['Rate'])
	form11 = f"<b>📆 Bugun 👉 {soat()}</b>\n\n1⃣ 🇨🇳 Yuan = <b>{result11} So'm\n\n✅ @KourseBot</b>"
	await call.message.answer(form11,reply_markup=Back)
	await call.message.delete()
	await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains="vonu")
async def vonuu(call: CallbackQuery):
	url12 = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/KRW/UZS'
	r12 = requests.get(url12).json()
	result12 = (r12[0]['Rate'])
	form12 = f"<b>📆 Bugun 👉 {soat()}</b>\n\n1⃣ 🇰🇷 Von = <b>{result12} So'm\n\n✅ @KourseBot</b>"
	await call.message.answer(form12,reply_markup=Back)
	await call.message.delete()
	await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains="lirau")
async def Lirau(call: CallbackQuery):
	url10 = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/TRY/UZS'
	r10 = requests.get(url10).json()
	result10 = (r10[0]['Rate'])
	form10 = f"<b>📆 Bugun 👉 {soat()}</b>\n\n1⃣ 🇹🇷 Lira = <b>{result10} So'm\n\n✅ @KourseBot</b>"
	await call.message.answer(form10,reply_markup=Back)
	await call.message.delete()
	await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains="arbu")
async def Arbu(call: CallbackQuery):
	url13 = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/SAR/UZS'
	r13 = requests.get(url13).json()
	result13 = (r13[0]['Rate'])
	form13 = f"<b>📆 Bugun 👉 {soat()}</b>\n\n1⃣ 🇸🇦 Riali = <b>{result13} So'm\n\n✅ @KourseBot</b>"
	await call.message.answer(form13,reply_markup=Back)
	await call.message.delete()
	await call.answer(cache_time=60)
	
@dp.callback_query_handler(text_contains="rinu")
async def Rinng(call: CallbackQuery):
	url15 = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/MYR/UZS'
	r15 = requests.get(url15).json()
	result15 = (r15[0]['Rate'])
	form15 = f"<b>📆 Bugun 👉 {soat()}</b>\n\n1⃣ 🇲🇾 Ringgit = <b>{result15} So'm\n\n✅ @KourseBot</b>"
	await call.message.answer(form15,reply_markup=Back)
	await call.message.delete()
	await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains="azman")
async def Azarbay(call: CallbackQuery):
	url17 = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/AZN/UZS'
	r17 = requests.get(url17).json()
	result17 = (r17[0]['Rate'])
	form17 = f"<b>📆 Bugun 👉 {soat()}</b>\n\n1⃣ 🇦🇿 Manat = <b>{result17} So'm\n\n✅ @KourseBot</b>"
	await call.message.answer(form17,reply_markup=Back)
	await call.message.delete()
	await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains="msrf")
async def Msrfun(call: CallbackQuery):
	url16 = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/EGP/UZS'
	r16 = requests.get(url16).json()
	result16 = (r16[0]['Rate'])
	form16 = f"<b>📆 Bugun 👉 {soat()}</b>\n\n1⃣ 🇪🇬 Funt = <b>{result16} So'm\n\n✅ @KourseBot</b>"
	await call.message.answer(form16,reply_markup=Back)
	await call.message.delete()
	await call.answer(cache_time=60)
	
	
@dp.callback_query_handler(text_contains="allkurs")
async def allkurs(call: CallbackQuery):
	url1 = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/USD/UZS'
	r = requests.get(url1).json()
	result1 = (r[0]['Rate'])
	url2 = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/EUR/UZS'
	r2 = requests.get(url2).json()
	result2 = (r2[0]['Rate'])
	url3 = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/RUB/UZS'
	r3 = requests.get(url3).json()
	result3 = (r3[0]['Rate'])
	url4 = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/KGS/UZS'
	r4 = requests.get(url4).json()
	result4 = (r4[0]['Rate'])
	url5 = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/AFN/UZS'
	r5 = requests.get(url5).json()
	result5 = (r5[0]['Rate'])
	url6 = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/KZT/UZS'
	r6 = requests.get(url6).json()
	result6 = (r6[0]['Rate'])
	url7 = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/TJS/UZS'
	r7 = requests.get(url7).json()
	result7 = (r7[0]['Rate'])
	url8 = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/TMT/UZS'
	r8 = requests.get(url8).json()
	result8 = (r8[0]['Rate'])
	url9 = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/GBP/UZS'
	r9 = requests.get(url9).json()
	result9 = (r9[0]['Rate'])
	url11 = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/CNY/UZS'
	r11 = requests.get(url11).json()
	result11 = (r11[0]['Rate'])
	url12 = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/KRW/UZS'
	r12 = requests.get(url12).json()
	result12 = (r12[0]['Rate'])
	url10 = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/TRY/UZS'
	r10 = requests.get(url10).json()
	result10 = (r10[0]['Rate'])
	url13 = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/SAR/UZS'
	r13 = requests.get(url13).json()
	result13 = (r13[0]['Rate'])
	url15 = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/MYR/UZS'
	r15 = requests.get(url15).json()
	result15 = (r15[0]['Rate'])
	url17 = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/AZN/UZS'
	r17 = requests.get(url17).json()
	result17 = (r17[0]['Rate'])
	url16 = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/EGP/UZS'
	r16 = requests.get(url16).json()
	result16 = (r16[0]['Rate'])
	utc_now = pytz.utc.localize(datetime.datetime.utcnow())
	pst_now = utc_now.astimezone(pytz.timezone("Asia/Tashkent"))
	dt_string = pst_now.strftime("%d.%m.%Y-YIL\n⏰ Soat 👉 %H:%M:%S")
	allkursu = f"<b>🇺🇿 O'zbekiston markaziy banki\n📆 Bugun 👉 {dt_string}\n</b>\n1⃣  🇺🇸 Dollar = <b>{result1} So'm</b>\n1⃣  🇪🇺 Yevro = <b>{result2} So'm</b>\n1⃣  🇷🇺 Rubl = <b>{result3} So'm</b>\n1⃣  🇰🇬 Som = <b>{result4} So'm</b>\n1⃣  🇦🇫 Afg'ani = <b>{result5} So'm</b>\n1⃣  🇰🇿 Tenge = <b>{result6} So'm</b>\n1⃣  🇹🇯 Somoni = <b>{result7} So'm</b>\n1⃣  🇹🇲 Manat = <b>{result8} So'm</b>\n1⃣  🇨🇳 Yuan = <b>{result11} So'm </b>\n1⃣  🇬🇧 Funt = <b>{result9} So'm</b>\n1⃣  🇰🇷 Von = <b>{result12} So'm </b>\n1⃣  🇹🇷 Lira = <b>{result10} So'm</b>\n1⃣  🇸🇦 Riali = <b>{result13} So'm </b>\n1⃣  🇲🇾 Ringgit = <b>{result15} So'm </b>\n1⃣  🇦🇿 Manat = <b>{result17} So'm </b>\n1⃣  🇪🇬 Funt = <b>{result16} So'm </b>\n\n<b>✅ @KourseBot</b>"
	await call.message.answer(allkursu,reply_markup=Back)
	await call.message.delete()
	await call.answer(cache_time=100)
