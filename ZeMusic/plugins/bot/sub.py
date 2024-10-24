from pyrogram import filters
from pyrogram.types import Message
from config import BANNED_USERS
from ZeMusic import app  # تأكد من استيراد التطبيق الخاص بك

# متغيرات الاشتراك
required_channel = None
subscribed_users_count = 0
subscription_limit = 0
is_subscription_required = False

@app.on_message(filters.command("اشتراك إجباري") & filters.group)
async def add_subscription(client, message: Message):
    global required_channel, subscribed_users_count, subscription_limit, is_subscription_required
    command_parts = message.command[1:]

    if len(command_parts) < 2:
        await message.reply_text("يرجى إدخال القناة وعدد الأعضاء المطلوبين.")
        return

    required_channel = command_parts[0]
    subscription_limit = int(command_parts[1])
    is_subscription_required = True
    subscribed_users_count = 0

    await message.reply_text(f"تم تفعيل الاشتراك الإجباري في القناة: {required_channel} عدد الأعضاء المطلوبين: {subscription_limit}")

@app.on_message(filters.command("حذف الاشتراك الاجباري") & filters.group)
async def remove_subscription(client, message: Message):
    global required_channel, is_subscription_required, subscribed_users_count
    required_channel = None
    is_subscription_required = False
    subscribed_users_count = 0
    await message.reply_text("تم حذف الاشتراك الإجباري.")

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
                subscribed_users_count += 1
                if subscribed_users_count >= subscription_limit:
                    await message.reply_text("تم الوصول إلى الحد الأقصى لعدد المشتركين. تم إلغاء الاشتراك الإجباري.")
                    is_subscription_required = False
                    required_channel = None
                    subscribed_users_count = 0
        except Exception as e:
            await message.reply_text("حدث خطأ أثناء التحقق من الاشتراك.")
