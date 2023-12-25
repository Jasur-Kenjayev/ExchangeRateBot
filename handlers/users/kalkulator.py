from aiogram.types import Message
from loader import dp
from states.savol import PersonalData2
from aiogram.dispatcher import FSMContext
from keyboards.default.menuKeyboard import menu, bekor2
from aiogram import types
import requests
import json
import asyncio

@dp.message_handler(text= "◀️ Orqaga",state=PersonalData2.adss2)
async def cancel1(message:
	types.Message, state: FSMContext):
	await state.finish()
	await message.answer("<b>🤖Orqaga Muvafaqiyatli qaytdingiz✅</b>",reply_markup=menu)

@dp.message_handler(text="🧮 Kalkulyator")
async def islomsavol(message: Message):
	await message.answer("<b>📊 Barcha aktual Valyutalarni Ko'rsatadi. Ya'ni masalan 500 raqamini kiritsangiz:\n500 Valyuta = 500 x So'm✅\n\n✏️ Marhammat Hisoblash Uchun Bironta Son Kiriting👇</b>",reply_markup=bekor2)
	await PersonalData2.adss2.set()

@dp.message_handler(state=PersonalData2.adss2)
async def savolislom(message: types.Message, state: FSMContext):
    text = message.text
    await message.reply("<i>⏳ iltmos biroz kuting natija yuborilmoqda....</i>")
    
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
    
    try:
    	mesg = float(text)
    	
    	usd = float(result1)
    	dollor = usd * mesg
    	dollorr = "%.2f" % dollor
    	evr = float(result2)
    	evro = evr * mesg
    	evroo = "%.2f" % evro
    	rub = float(result3)
    	rubl = rub * mesg
    	rubll = "%.2f" % rubl
    	kgi = float(result4)
    	kgs = kgi * mesg
    	kgss = "%.2f" % kgs
    	afg = float(result5)
    	afga = afg * mesg
    	afgaa = "%.2f" % afga
    	ten = float(result6)
    	kzt = ten * mesg
    	kztt = "%.2f" % kzt
    	taj = float(result7)
    	tjs = taj * mesg
    	tjss = "%.2f" % tjs
    	tutmt = float(result8)
    	tmtt = tutmt * mesg
    	tmttt = "%.2f" % tmtt
    	fung = float(result9)
    	funt = fung * mesg
    	funtt = "%.2f" % funt
    	yux = float(result11)
    	yuan = yux * mesg
    	yuann = "%.2f" % yuan
    	kvon = float(result12)
    	von = kvon * mesg
    	vonn = "%.2f" % von
    	tlira = float(result10)
    	lira = tlira * mesg
    	liraa = "%.2f" % lira
    	ariali = float(result13)
    	riali = ariali * mesg
    	rialii = "%.2f" % riali
    	mring = float(result15)
    	ringgi = mring * mesg
    	ringgii = "%.2f" % ringgi
    	amana = float(result17)
    	amanat = amana * mesg
    	amanatt = "%.2f" % amanat
    	fmsr = float(result16)
    	misr = fmsr * mesg
    	misrr = "%.2f" % misr
    	
    	await message.reply(f"<b>{text}</b> 🇺🇸 Dollar = <b>{dollorr} So'm</b>\n<b>{text}</b> 🇪🇺 Yevro = <b>{evroo} So'm</b>\n<b>{text}</b> 🇷🇺 Rubl = <b>{rubll} So'm</b>\n<b>{text}</b> 🇰🇬 Som = <b>{kgss} So'm</b>\n<b>{text}</b> 🇦🇫 Afg'ani = <b>{afgaa} So'm</b>\n<b>{text}</b> 🇰🇿 Tenge = <b>{kztt} So'm</b>\n<b>{text}</b> 🇹🇯 Somoni = <b>{tjss} So'm</b>\n<b>{text}</b> 🇹🇲 Manat = <b>{tmttt} So'm</b>\n<b>{text}</b> 🇨🇳 Yuan = <b>{yuann} So'm</b>\n<b>{text}</b> 🇬🇧 Funt = <b>{funtt} So'm</b>\n<b>{text}</b> 🇰🇷 Von = <b>{vonn} So'm</b>\n<b>{text}</b> 🇹🇷 Lira = <b>{liraa} So'm</b>\n<b>{text}</b> 🇸🇦 Riali = <b>{rialii} So'm</b>\n<b>{text}</b> 🇲🇾 Ringgit = <b>{ringgii} So'm</b>\n<b>{text}</b> 🇦🇿 Manat = <b>{amanatt} So'm</b>\n<b>{text}</b> 🇪🇬 Funt = <b>{misrr} So'm\n\n✅ @KourseBot</b>",reply_markup=menu)
    	await state.finish()
    except:
    	await message.reply("<b>❕Faqat raqam yuborish mumkin!\nButun qismli sonlarni esa nuqta bilan (Maslan: 10.7) kiriting!\nVergul, bo'sh joy va belgilarsiz faqat raqam kiriting.</b>")