from telethon.sync import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest
import time

# بياناتك
api_id = 24728979
api_hash = '87d1503b0831dbf93c0f1bad3783ff6d'
phone_number = '+218930763907'

# الجروب والقناة بدون @
source_group = 'drkhomci2005'
target_channel = 'dont_share_the_focking_channel'

# إنشاء الجلسة
client = TelegramClient('session', api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone_number)
    code = input('📥 أدخل كود التحقق اللي وصلك على Telegram: ')
    client.sign_in(phone_number, code)

# جلب الأعضاء من الجروب
users = client.get_participants(source_group)

# إضافتهم للقناة
for user in users:
    try:
        client(InviteToChannelRequest(target_channel, [user]))
        print(f'✅ تمت إضافة: {user.id}')
        time.sleep(10)  # مهم عشان ما تاخذ سبام أو حظر
    except Exception as e:
        print(f'❌ فشل في {user.id}: {e}')
        time.sleep(5)

client.disconnect()
