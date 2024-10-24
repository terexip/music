import asyncio
from pyrogram import filters, Client
from pyrogram.types import Message
from config import BANNED_USERS

app = Client("my_bot")

# متغيرات الاشتراك
required_channel = None  # القناة المطلوبة للاشتراك
subscribed_users_count = 0  # عدد الأعضاء الذين اشتركوا
subscription_limit = 0  # الحد الأقصى لعدد الأعضاء
is_subscription_required = False  # إذا كان الاشتراك الإجباري مفعلًا

@app.on_message(filters.command("اشتراك إجباري") & filters.group)
async def add_subscription(client, message: Message):
    global required_channel, subscribed_users_count, subscription_limit, is_subscription_required
    command_parts = message.command[1:]

    if len(command_parts) < 2:
        await message.reply_text("يرجى إدخال القناة وعدد الأعضاء المطلوبين.")
        return

    required_channel = command_parts[0]
    subscription_limit = int(command_parts[1])  # تحويل العدد إلى عدد صحيح
    is_subscription_required = True
    subscribed_users_count = 0  # إعادة تعيين العدد عند التفعيل

    await message.reply_text(f"تم تفعيل الاشتراك الإجباري في القناة: {required_channel} عدد الأعضاء المطلوبين: {subscription_limit}")

@app.on_message(filters.command("حذف الاشتراك الاجباري") & filters.group)
async def remove_subscription(client, message: Message):
    global required_channel, is_subscription_required, subscribed_users_count
    required_channel = None
    is_subscription_required = False
    subscribed_users_count = 0  # إعادة تعيين العدد عند الحذف
    await message.reply_text("تم حذف الاشتراك الإجباري.")

@app.on_message(filters.command("تعطيل الاشتراك الاجباري") & filters.group)
async def disable_subscription(client, message: Message):
    global is_subscription_required
    if is_subscription_required:
        is_subscription_required = False
        await message.reply_text("تم تعطيل الاشتراك الإجباري.")
    else:
        await message.reply_text("الاشتراك الإجباري غير مفعل.")

@app.on_message(filters.command("تفعيل الاشتراك الاجباري") & filters.group)
async def enable_subscription(client, message: Message):
    global is_subscription_required
    if not is_subscription_required:
        is_subscription_required = True
        await message.reply_text("تم تفعيل الاشتراك الإجباري.")
    else:
        await message.reply_text("الاشتراك الإجباري مفعل بالفعل.")

@app.on_message(filters.text & filters.group)
async def check_subscription(client, message: Message):
    global required_channel, subscribed_users_count, is_subscription_required
    if required_channel and is_subscription_required:
        user_id = message.from_user.id
        try:
            chat_member = await client.get_chat_member(required_channel, user_id)
            if chat_member.status not in ['administrator', 'member']:
                await message.reply_text("يجب أن تكون مشتركًا في القناة قبل إرسال الرسالة.")
                return
            else:
                # زيادة عدد الأعضاء المشتركين إذا كان الاشتراك ناجحًا
                subscribed_users_count += 1
                # تحقق من الحد الأقصى
                if subscribed_users_count >= subscription_limit:
                    await message.reply_text("تم الوصول إلى الحد الأقصى لعدد المشتركين. تم إلغاء الاشتراك الإجباري.")
                    is_subscription_required = False  # إلغاء الاشتراك الإجباري
                    required_channel = None
                    subscribed_users_count = 0
        except Exception as e:
            await message.reply_text("حدث خطأ أثناء التحقق من الاشتراك.")

async def main():
    async with app:
        await app.start()
        print("البوت يعمل الآن...")
        await app.idle()  # ينتظر حتى يتوقف البوت

if __name__ == "__main__":
    asyncio.run(main())
