from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="📊 Valyuta Kursi"),
         ],
         [
         	KeyboardButton(text="✅ Channel"), KeyboardButton(text="🤖 Bot help"),
       ],
       [
       	KeyboardButton(text="🧮 Kalkulyator"),
    ],
    ],
    resize_keyboard=True
)

bekor2 = ReplyKeyboardMarkup(
    keyboard = [
        [
        	KeyboardButton(text="◀️ Orqaga"),
        ],
     ],
     resize_keyboard=True
)
