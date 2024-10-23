import asyncio
import os
import requests
import pyrogram
from pyrogram import Client, filters, emoji
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified
from ZeMusic import app
from config import OWNER_ID, LOGGER_ID, START_IMG_URL
import config

@app.on_message(command(["اوامر", "التشغيل "]))
async def zdatsr(client: Client, message: Message):
    # الحصول على معلومات المستخدم
    try:
        usr = await client.get_users(OWNER_ID)
        name = usr.first_name
        usrnam = usr.username
    except Exception as e:
        await message.reply(f"حدث خطأ في جلب معلومات المستخدم: {str(e)}")
        return

    # التحقق من الرابط قبل إرسال الصورة
    if not START_IMG_URL:
        await message.reply("الصورة غير متاحة حالياً.")
        return

    try:
        # إرسال رسالة الرد بالصورة والقائمة
        await message.reply_photo(
            photo=START_IMG_URL,
            caption=f"""<b>-› مرحبا بك</b> {message.from_user.mention} .\n\n<b>-› جميع اوامر البوت موجودة بالقائمة هذي، اضغط الأزرار تحت واستكشف ياوحش\n</b>""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            " اوامــر التشغيــل ", callback_data="zzzll"),
                    ],
                    [
                        InlineKeyboardButton(
                            " اوامـر القنـاة ", callback_data="zzzch"),
                        InlineKeyboardButton(
                            " اوامـر الادمـن ", callback_data="zzzad"),
                    ],
                    [
                        InlineKeyboardButton(
                            text=config.CHANNEL_NAME, url=config.CHANNEL_LINK),
                    ],
                ]
            ),
        )
    except Exception as e:
        await message.reply(f"حدث خطأ أثناء إرسال الرسالة: {str(e)}")
