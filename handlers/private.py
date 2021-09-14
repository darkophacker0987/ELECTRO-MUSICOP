from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help_(client: Client, message: Message):
      await message.reply_text("""𝙄𝙏 𝙄𝙎 𝘼𝘿𝙑𝘼𝙉𝘾𝙀𝘿 𝙈𝙐𝙎𝙄𝘾 𝘽𝙊𝙏 𝙈𝘼𝘿𝙀 𝙁𝙊𝙍 𝙇𝙄𝙎𝙏𝙀𝙉 𝙈𝙐𝙎𝙄𝘾 """,
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ßƐSŦĪƐS ZᎾИƐ", url="https://t.me/BONDOFBESTIZZ")
                ]
            ]
        )
   )
