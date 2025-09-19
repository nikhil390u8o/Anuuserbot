from telethon import Button, events
from telethon.tl.functions.messages import GetMessagesRequest
from config import OWNER_NAME, OWNER_USERNAME
from firebase import add_new_user

# Telegram post for media
VIDEO_CHANNEL = "BAMBI799U"
VIDEO_ID = 139  # ID of the post in the channel

# ───────────── /start Command ─────────────
async def start_handle(client, event):
    user = await event.get_sender()
    mention = f'<a href="tg://user?id={user.id}">{user.first_name}</a>'
    owner = f'<a href="https://t.me/{OWNER_USERNAME}">{OWNER_NAME}</a>'

    msg_text = (
        f"┌────── ˹ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ˼ ⏤‌‌‌‌‌‌‌‌★\n"
        f"┆◍ ʜᴇʏ {mention}, ɪ ᴀᴍ : <a href='https://t.me/MANIAC_USR_BOT'>ᴍᴀɴɪᴀᴄ-x-ᴜsᴇʀʙᴏᴛ</a>\n"
        "┆◍ ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ ᴅᴇᴀʀ !! \n"
        "└────────────────────•\n"
        "❖ ɪ ᴀᴍ ᴀ ᴘᴏᴡᴇʀғᴜʟ & ᴜsᴇғᴜʟʟ ᴜsᴇʀʙᴏᴛ.\n"
        "❖ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ғᴏʀ ғᴜɴ ʀᴀɪᴅ sᴘᴀᴍ.\n"
        "❖ ɪ ᴄᴀɴ ʙᴏᴏsᴛ ʏᴏᴜʀ ɪᴅ ᴡɪᴛʜ ᴀɴɪᴍᴀᴛɪᴏɴ\n"
        "❖ ᴛᴀᴘ ᴛᴏ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ғᴏʀ ᴅᴇᴛᴀɪʟs.\n"
        "•────────────────────•\n"
        "❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :- <a href='https://t.me/RADHIKA_YIIOO'>ʀᴀᴅʜɪᴋᴀ-x-ɴᴇᴛᴡᴏʀᴋ 🚩</a>\n"
        "•────────────────────•\n"
        f"☆ ᴏᴡɴᴇʀ: {owner}"
    )

    buttons = [
        [Button.url("•𝐂𝐇𝐀𝐍𝐍𝐄𝐋•", "https://t.me/YourSupportChannel"),
         Button.url("•𝐆𝐑𝐎𝐔𝐏•", "https://t.me/YourSupportGroup")],
        [Button.url("•𝐎𝐖𝐍𝐄𝐑•", f"https://t.me/{OWNER_USERNAME}")],
        [Button.inline("•𝐇𝐄𝐋𝐏", data=b"help_menu")]
    ]

    # Fetch media from channel post
    channel_entity = await client.get_entity(VIDEO_CHANNEL)
    message = await client.get_messages(channel_entity, ids=VIDEO_ID)

    await event.reply(
        msg_text,
        file=message.media if message and message.media else None,
        parse_mode="html",
        buttons=buttons
    )

    # Save user in Firebase
    data = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "username": user.username,
        "user_id": user.id,
    }
    add_new_user(data)

# ───────────── Help Menu Callback ─────────────
async def help_menu(event):
    buttons = [[Button.inline("•𝐁𝐀𝐂𝐊•", data=b"back_start")]]
    help_text = (
        "✦ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ\n\n"
        "➻ /start - ꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n"
        "➻ /gen - ʜᴏsᴛ ʏᴏᴜʀ ᴄʟɪᴇɴᴛ\n"
        "➻ /clone - ᴄʟᴏɴᴇ ᴠɪᴀ sᴛʀɪɴɢ sᴇssɪᴏɴ\n"
        "➻ /ping - ᴄʜᴇᴄᴋ ᴛʜᴇ ʙᴏᴛ ɪs ᴀʟɪᴠᴇ\n\n"
        "✦ ᴀʙᴏᴜᴛ ᴛʜɪꜱ ʙᴏᴛ\n\n"
        "◍ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴛᴏ ʙᴏᴏsᴛ ʏᴏᴜʀ ɪᴅ ᴡɪᴛʜ ʙᴇᴀᴜᴛɪғᴜʟ ᴀɴɪᴍᴀᴛɪᴏɴ.\n\n"
        "◌ ʟᴀɴɢᴜᴀɢᴇ : <a href='https://python.org'>Python</a>\n"
        "◌ ᴘᴏᴡᴇʀᴇᴅ ʙʏ : <a href='https://t.me/RADHIKA_YIIOO'>ʀᴀᴅʜɪᴋᴀ-x-ɴᴇᴛᴡᴏʀᴋ</a>\n"
        "◌ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/ll_PANDA_BBY_ll'>Developer</a>"
    )
    await event.edit(help_text, parse_mode="html", buttons=buttons)

# ───────────── Back Button Callback ─────────────
async def back_start(event):
    user = await event.get_sender()
    mention = f'<a href="tg://user?id={user.id}">{user.first_name}</a>'
    owner = f'<a href="https://t.me/{OWNER_USERNAME}">{OWNER_NAME}</a>'

    msg_text = (
        f"┌────── ˹ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ˼ ⏤‌‌‌‌‌‌‌‌★\n"
        f"┆◍ ʜᴇʏ {mention}, ɪ ᴀᴍ : <a href='https://t.me/USERBOT_577Y_BOT'>ᴀɴᴀɴʏᴀ-x-ᴜsᴇʀʙᴏᴛ</a>\n"
        "┆◍ ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ ᴅᴇᴀʀ !! \n"
        "└────────────────────•\n"
        "❖ ɪ ᴀᴍ ᴀ ᴘᴏᴡᴇʀғᴜʟ & ᴜsᴇғᴜʟʟ ᴜsᴇʀʙᴏᴛ.\n"
        "❖ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ғᴏʀ ғᴜɴ ʀᴀɪᴅ sᴘᴀᴍ.\n"
        "❖ ɪ ᴄᴀɴ ʙᴏᴏsᴛ ʏᴏᴜʀ ɪᴅ ᴡɪᴛʜ ᴀɴɪᴍᴀᴛɪᴏɴ\n"
        "❖ ᴛᴀᴘ ᴛᴏ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ғᴏʀ ᴅᴇᴛᴀɪʟs.\n"
        "•────────────────────•\n"
        "❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :- <a href='https://t.me/RADHIKA_YIIOO'>ʀᴀᴅʜɪᴋᴀ-x-ɴᴇᴛᴡᴏʀᴋ 🚩</a>\n"
        "•────────────────────•\n"
        f"☆ ᴏᴡɴᴇʀ: {owner}"
    )

    buttons = [
        [Button.url("•𝐂𝐇𝐀𝐍𝐍𝐄𝐋•", "https://t.me/YourSupportChannel"),
         Button.url("•𝐆𝐑𝐎𝐔𝐏•", "https://t.me/YourSupportGroup")],
        [Button.url("•𝐎𝐖𝐍𝐄𝐑•", f"https://t.me/{OWNER_USERNAME}")],
        [Button.inline("•𝐇𝐄𝐋𝐏", data=b"help_menu")]
    ]

    await event.edit(msg_text, parse_mode="html", buttons=buttons)
