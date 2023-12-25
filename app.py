from aiogram import executor

from loader import dp, db, bot
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
import aioschedule, asyncio
import datetime
import pytz
import requests
import json
from pprint import pprint as print

async def will_send():
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
	dt_string = pst_now.strftime("%d.%m.%Y-YIL\n<b>⏰ Soat 👉%H:%M:%S</b>")
	forall= f"<b>😊 Salom Xayrli Tong ☕️\n\n🏦 O'zbekiston markaziy banki\n📆 Bugun 👉 {dt_string}</b>\n\n1⃣  🇺🇸 Dollar = <b>{result1} So'm</b>\n1⃣  🇪🇺 Yevro = <b>{result2} So'm</b>\n1⃣  🇷🇺 Rubl = <b>{result3} So'm</b>\n1⃣  🇰🇬 Som = <b>{result4} So'm</b>\n1⃣  🇦🇫 Afg'ani = <b>{result5} So'm</b>\n1⃣  🇰🇿 Tenge = <b>{result6} So'm</b>\n1⃣  🇹🇯 Somoni = <b>{result7} So'm</b>\n1⃣  🇹🇲 Manat = <b>{result8} So'm</b>\n1⃣  🇨🇳 Yuan = <b>{result11} So'm </b>\n1⃣  🇬🇧 Funt = <b>{result9} So'm</b>\n1⃣  🇰🇷 Von = <b>{result12} So'm </b>\n1⃣  🇹🇷 Lira = <b>{result10} So'm</b>\n1⃣  🇸🇦 Riali = <b>{result13} So'm </b>\n1⃣  🇲🇾 Ringgit = <b>{result15} So'm </b>\n1⃣  🇦🇿 Manat = <b>{result17} So'm </b>\n1⃣  🇪🇬 Funt = <b>{result16} So'm </b>\n\n<b>@KourseBot - Aktual Kurs✅</b>"
	await bot.send_message(-1001668684500, forall)
   
async def scheduler():
    aioschedule.every().day.at("1:00").do(will_send)
    while True:
       await aioschedule.run_pending()
       await asyncio.sleep(0.03)    
       
async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    
    try:
        db.create_table_users()
    except Exception as err:
    	pass

    await on_startup_notify(dispatcher)
    asyncio.create_task(scheduler())

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

