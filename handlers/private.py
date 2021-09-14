from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def help_(client: Client, message: Message):
      await message.reply_text("""𝐇𝐞𝐲, 𝐈'𝐦 𝐕𝐜 𝐁𝐨𝐭❤️🔥. 
𝐈 𝐂𝐚𝐧 𝐏𝐥𝐚𝐲 𝐌𝐮𝐬𝐢𝐜 𝐈𝐧 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭.
𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐀𝐧𝐝 𝐏𝐥𝐚𝐲 𝐌𝐮𝐬𝐢𝐜 𝐅𝐫𝐞𝐞𝐥𝐲! 
/help - 𝐓𝐨 𝐆𝐞𝐭 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬.✅""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ßƐSŦĪƐS ZᎾИƐ", url="https://t.me/BONDOFBESTIZZ")
                ]
            ]
        )
   )
