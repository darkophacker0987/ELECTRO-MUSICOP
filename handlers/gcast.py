import asyncio
import os
import subprocess
import time
from pyrogram import Client, filters
from pyrogram.types import Message
from config import  SUDO_USERS


@Client.on_message(
    filters.command("broadcast")
    & filters.group
    & filters.user(SUDO_USERS)
    & ~ filters.edited
)
async def sbroadcast(message):
    data = await get_parsed_note_list(message, split_args=-1)
    dp.register_message_handler(check_message_for_smartbroadcast)

    await db.sbroadcast.drop({})

    chats = mongodb.chat_list.distinct('chat_id')

    data['chats_num'] = len(chats)
    data['recived_chats'] = 0
    data['chats'] = chats

    await db.sbroadcast.insert_one(data)
    await message.reply("Smart broadcast planned for <code>{}</code> chats".format(len(chats)))

