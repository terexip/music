import asyncio
import os
import requests
import pyrogram
from pyrogram import Client, filters, emoji
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from ZeMusic import app
from config import OWNER_ID, LOGGER_ID, START_IMG_URL, CHANNEL_NAME, CHANNEL_LINK
import config

@app.on_message(command(["اوامر", "التشغيل "]))
async def zdatsr(client: Client, message: Message):
    usr = await client.get_users(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username

    if not START_IMG_URL:  # تحقق من وجود رابط الصورة
        await message.reply("لا يوجد رابط للصورة!")
        return

    await message.reply_photo(
        photo=START_IMG_URL,
        caption=f"""<b>-› مرحبا بك</b> {message.from_user.mention} .\n\n<b>-› جميع اوامر البوت موجودة بالقائمة هذي ، اضغط الازرار الي تحت واستكشف ياوحش\n</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(" اوامــر التشغيــل ", callback_data="zzzll"),
                ],
                [
                    InlineKeyboardButton(" اوامـر القنـاة ", callback_data="zzzch"),
                    InlineKeyboardButton(" اوامـر الادمـن ", callback_data="zzzad"),
                ],
                [
                    InlineKeyboardButton(text=CHANNEL_NAME, url=CHANNEL_LINK),
                ],
            ]
        ),
    )
