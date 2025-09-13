from telethon import Button, events
from config import OWNER_NAME, OWNER_USERNAME
from firebase import add_new_user

IMG_URL = "https://files.catbox.moe/1f21lw.jpg"

# /start command
async def start_handle(event):
    user = await event.get_sender()
    mention = f'<a href="tg://user?id={user.id}">{user.first_name}</a>'
    owner = f'<a href="https://t.me/{OWNER_USERNAME}">{OWNER_NAME}</a>'

    msg = (
        f"┌────── ˹ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ˼ ⏤‌‌‌‌‌‌‌‌★
┆◍ ʜᴇʏ, ɪ ᴀᴍ :[ᴀɴᴀɴʏᴀ-x-ᴜsᴇʀʙᴏᴛ](https://t.me/USERBOT_577Y_BOT)
┆◍ ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ ᴅᴇᴀʀ !! 
└────────────────────•
❖ ɪ ᴀᴍ ᴀ ᴘᴏᴡᴇʀғᴜʟ & ᴜsᴇғᴜʟʟ ᴜsᴇʀʙᴏᴛ.
❖ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ғᴏʀ ғᴜɴ ʀᴀɪᴅ sᴘᴀᴍ.
❖ ɪ ᴄᴀɴ ʙᴏᴏsᴛ ʏᴏᴜʀ ɪᴅ ᴡɪᴛʜ ᴀɴɪᴍᴀᴛɪᴏɴ
❖ ᴛᴀᴘ ᴛᴏ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ғᴏʀ ᴅᴇᴛᴀɪʟs.
•────────────────────•
❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :- [ʀᴀᴅʜɪᴋᴀ-x-ɴᴇᴛᴡᴏʀᴋ 🚩](https://t.me/RADHIKA_YIIOO)
•────────────────────•
☆ ᴏᴡɴᴇʀ: [ᴘᴀɴᴅᴀ-ʙᴀʙʏ](https://t.me/ll_PANDA_BBY_ll)"
    )

    buttons = [
        [Button.url("Channel", "https://t.me/YourSupportChannel"),
         Button.url("Group", "https://t.me/YourSupportGroup")],
        [Button.url("Owner", f"https://t.me/{OWNER_USERNAME}"),
         Button.inline("Help", data=b"help_menu")]
    ]

    await event.reply(msg, file=IMG_URL, parse_mode="html", buttons=buttons)

    # Save user in Firebase
    data = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "username": user.username,
        "user_id": user.id,
    }
    add_new_user(data)

# Help menu callback
async def help_menu(event):
    buttons = [[Button.inline("Back", data=b"back_start")]]
    await event.edit(
        """✦ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ

➻ /start - ꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ
➻ /gen - ʜᴏsᴛ ʏᴏᴜʀ ᴄʟɪᴇɴᴛ
➻ /clone - ᴄʟᴏɴᴇ ᴠɪᴀ sᴛʀɪɴɢ sᴇssɪᴏɴ
➻ /ping - ᴄʜᴇᴄᴋ ᴛʜᴇ ʙᴏᴛ ɪs ᴀʟɪᴠᴇ 

✦ ᴀʙᴏᴜᴛ ᴛʜɪꜱ ʙᴏᴛ

◍ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴛᴏ ʙᴏᴏsᴛ ʏᴏᴜʀ ɪᴅ ᴡɪᴛʜ ʙᴇᴀᴜᴛɪғᴜʟ ᴀɴɪᴍᴀᴛɪᴏɴ.


◌ ʟᴀɴɢᴜᴀɢᴇ : [ᴘʏᴛʜᴏɴ](python.org)
◌ ᴘᴏᴡᴇʀᴇᴅ ʙʏ : [ʀᴀᴅʜɪᴋᴀ-x-ɴᴇᴛᴡᴏʀᴋ](https://t.me/RADHIKA_YIIOO)
◌ ᴅᴇᴠᴇʟᴏᴘᴇʀ : [ᴘᴀɴᴅᴀ-ʙᴀʙʏ](https://t.me/ll_PANDA_BBY_ll)""",
        parse_mode="html",
        buttons=buttons
    )

# Back button callback
# Back button callback
async def back_start(event):
    user = await event.get_sender()
    mention = f'<a href="tg://user?id={user.id}">{user.first_name}</a>'
    owner = f'<a href="https://t.me/{OWNER_USERNAME}">{OWNER_NAME}</a>'

    buttons = [
    [
        Button.url("Channel", "https://t.me/YourSupportChannel"),
        Button.url("Group", "https://t.me/YourSupportGroup"),
        Button.url("Owner", f"https://t.me/{OWNER_USERNAME}")
    ],
    [Button.inline("Help", data=b"help_menu")]  # This will be big
]

    await event.edit(
        f"┌────── ˹ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ˼ ⏤‌‌‌‌‌‌‌‌★
┆◍ ʜᴇʏ, ɪ ᴀᴍ :[ᴀɴᴀɴʏᴀ-x-ᴜsᴇʀʙᴏᴛ](https://t.me/USERBOT_577Y_BOT)
┆◍ ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ ᴅᴇᴀʀ !! 
└────────────────────•
❖ ɪ ᴀᴍ ᴀ ᴘᴏᴡᴇʀғᴜʟ & ᴜsᴇғᴜʟʟ ᴜsᴇʀʙᴏᴛ.
❖ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ғᴏʀ ғᴜɴ ʀᴀɪᴅ sᴘᴀᴍ.
❖ ɪ ᴄᴀɴ ʙᴏᴏsᴛ ʏᴏᴜʀ ɪᴅ ᴡɪᴛʜ ᴀɴɪᴍᴀᴛɪᴏɴ
❖ ᴛᴀᴘ ᴛᴏ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ғᴏʀ ᴅᴇᴛᴀɪʟs.
•────────────────────•
❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :- [ʀᴀᴅʜɪᴋᴀ-x-ɴᴇᴛᴡᴏʀᴋ 🚩](https://t.me/RADHIKA_YIIOO)
•────────────────────•
☆ ᴏᴡɴᴇʀ: [ᴘᴀɴᴅᴀ-ʙᴀʙʏ](https://t.me/ll_PANDA_BBY_ll)",
        parse_mode="html",
        buttons=buttons
    )
