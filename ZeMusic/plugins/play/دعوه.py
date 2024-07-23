from config import OWNER_ID
import asyncio
from pyrogram import Client, filters
from ZeMusic.utils.database import get_assistant
from pyrogram.types import Message
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic.core.call import Mody

@app.on_message(filters.video_chat_started)
async def brah(_, msg):
       await msg.reply("<b> تم بدء المكالمه الي وده يسمعنا صوته حياه</b>")



@app.on_message(filters.video_chat_members_invited)
async def brah3(app :app, message:Message):
           text = f"↞ هالحلو يبيك {message.from_user.mention} \n↞ تعال ياحلو للمكالمه :"
           x = 0
           for user in message.video_chat_members_invited.users:
             try:
               text += f"<a href='tg://user?id={user.id}'>{user.first_name}</a>"
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text}")
           except:
             pass

@app.on_message(filters.video_chat_ended)
async def brah2(client, message):
    da = message.video_chat_ended.duration
    ma = divmod(da, 60)
    ho = divmod(ma[0], 60)
    day = divmod(ho[0], 24)
    if da < 60:
       await message.reply(f"<b>واضح اصواتكم حلوه المكالمه تقفلت مدتها {da} ثانيه </b> ")        
    elif 60 < da < 3600:
        if 1 <= ma[0] < 2:
            await message.reply(f" <b>واضح اصواتكم حلوه المكالمه تقفلت مدتها دقيقه</b>")
        elif 2 <= ma[0] < 3:
            await message.reply(f" <b>واضح اصواتكم حلوه المكالمه تقفلت مدتها دقيقتين</b> ")
        elif 3 <= ma[0] < 11:
            await message.reply(f"<b>واضح اصواتكم حلوه المكالمه تقفلت مدتها {ma[0]} دقايق</b> ")  
        else:
            await message.reply(f"<b>واضح اصواتكم حلوه المكالمه تقفلت مدتها {ma[0]} دقيقه</b>")
    elif 3600 < da < 86400:
        if 1 <= ho[0] < 2:
            await message.reply(f"<b>واضح اصواتكم حلوه المكالمه تقفلت مدتها ساعه</b> ")
        elif 2 <= ho[0] < 3:
            await message.reply(f"<b>واضح اصواتكم حلوه المكالمه تقفلت مدتها ساعتين</b> ")
        elif 3 <= ho[0] < 11:
            await message.reply(f"<b>واضح اصواتكم حلوه المكالمه تقفلت مدتها {ho[0]} ساعات</b> ")  
        else:
            await message.reply(f"<b>واضح اصواتكم حلوه المكالمه تقفلت مدتها {ho[0]} ساعة</b> ")
    else:
        if 1 <= day[0] < 2:
            await message.reply(f"<b>واضح اصواتكم حلوه المكالمه تقفلت مدتها يوم</b> ")
        elif 2 <= day[0] < 3:
            await message.reply(f" <b>واضح اصواتكم حلوه المكالمه تقفلت مدتها يومين</b> ")
        elif 3 <= day[0] < 11:
            await message.reply(f" <b>واضح اصواتكم حلوه المكالمه تقفلت مدتها {day[0]} ايام</b> ")  
        else:
            await message.reply(f" <b>واضح اصواتكم حلوه المكالمه تقفلت مدتها {day[0]} يوم</b>")
