from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
      await message.reply_text(
        """๐๐๐ฒ, ๐'๐ฆ ๐๐ ๐๐จ๐ญโค๏ธ๐ฅ. 
๐ ๐๐๐ง ๐๐ฅ๐๐ฒ ๐๐ฎ๐ฌ๐ข๐ ๐๐ง ๐๐จ๐ฎ๐ซ ๐๐ซ๐จ๐ฎ๐ฉ ๐๐จ๐ข๐๐ ๐๐ก๐๐ญ.
๐๐๐ ๐๐ ๐๐จ ๐๐จ๐ฎ๐ซ ๐๐ซ๐จ๐ฎ๐ฉ ๐๐ง๐ ๐๐ฅ๐๐ฒ ๐๐ฎ๐ฌ๐ข๐ ๐๐ซ๐๐๐ฅ๐ฒ! 
/help - ๐๐จ ๐๐๐ญ ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ.โ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ถOแดกษดแดสโค๐ฅ", url="https://t.me/itz_cyberking_xd")
                  ],[
                    InlineKeyboardButton(
                        "๐ฅรฦSลฆฤชฦS Zแพะฦ๐ฅ", url="https://t.me/BONDOFBESTIZZ"
                    ),
                    InlineKeyboardButton(
                        "๐ฎ Channel ๐ฎ", url="https://t.me/INCREDIBLE_SPAM_BOT"
                    )    
                ],[ 
                    InlineKeyboardButton(
                        "โAแดแด แดแด สแดแดส ษขสแดแดแดโ", url="https://t.me/DEVILXPRINCE_ROBOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Yes iแด online โ**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ฅรฦSลฆฤชฦS Zแพะฦ๐ฅ", url="https://t.me/BONDOFBESTIZZ")
                ]
            ]
        )
   )
