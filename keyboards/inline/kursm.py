from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🇺🇸 Dollar / So'm", callback_data="usdu"), InlineKeyboardButton(text="🇪🇺 Evro \ So'm", callback_data="evu"),
        ],
        [
        InlineKeyboardButton(text="🇷🇺 Rubl / So'm", callback_data="ruu"), InlineKeyboardButton(text="🇰🇬 Som \ So'm", callback_data="somu"),
        ],
        [
        InlineKeyboardButton(text="🇦🇫 Afg'ani / So'm", callback_data="afgu"), InlineKeyboardButton(text="🇰🇿 Tenge \ So'm", callback_data="tenu"),
        ],
        [
        InlineKeyboardButton(text="🇹🇯 Somoni / So'm", callback_data="tjsu"), InlineKeyboardButton(text="🇹🇲 Manat \ So'm", callback_data="tmtu"),
        ],
        [
        InlineKeyboardButton(text="🇬🇧 Funt / So'm", callback_data="funtu"), InlineKeyboardButton(text="🇨🇳 Yuan \ So'm", callback_data="yuanu"),
        ],
        [
        InlineKeyboardButton(text="🇰🇷 Von / So'm", callback_data="vonu"), InlineKeyboardButton(text="🇹🇷 Lira \ So'm", callback_data="lirau"),
       ],
       [
       InlineKeyboardButton(text="🇸🇦 Riali / So'm", callback_data="arbu"), InlineKeyboardButton(text="🇲🇾 Ringgit \ So'm", callback_data="rinu"),
       ],
       [
       InlineKeyboardButton(text="🇦🇿 Manat / So'm", callback_data="azman"), InlineKeyboardButton(text="🇪🇬 Funt \ So'm", callback_data="msrf"),
       ],
       [
       InlineKeyboardButton(text="📇 Barcha Valyuta Kurslari ✅", callback_data="allkurs"),
    ]]
)
