from telethon import Button, events
from config import OWNER_NAME, OWNER_USERNAME
from firebase import add_new_user

VIDEO_URL = "https://files.catbox.moe/slfo3g.jpg"

# /start command
async def start_handle(event):
    user = await event.get_sender()
    mention = f'<a href="tg://user?id={user.id}">{user.first_name}</a>'
    owner = f'<a href="https://t.me/{OWNER_USERNAME}">{OWNER_NAME}</a>'

    msg = (
        f"┌────── ˹ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ˼ ⏤‌‌‌‌‌‌‌‌★\n"
        f"┆◍ ʜᴇʏ {mention}, ɪ ᴀᴍ : <a href='http://t.me/MANIAC_USR_BOT'>ᴍᴀɴɪᴀᴄ-x-ᴜsᴇʀʙᴏᴛ</a>\n"
        "┆◍ ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ ᴅᴇᴀʀ !! \n"
        "└────────────────────•\n"
        "❖ ɪ ᴀᴍ ᴀ ᴘᴏᴡᴇʀғᴜʟ & ᴜsᴇғᴜʟʟ ᴜsᴇʀʙᴏᴛ.\n"
        "❖ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ғᴏʀ ғᴜɴ ʀᴀɪᴅ sᴘᴀᴍ.\n"
        "❖ ɪ ᴄᴀɴ ʙᴏᴏsᴛ ʏᴏᴜʀ ɪᴅ ᴡɪᴛʜ ᴀɴɪᴍᴀᴛɪᴏɴ\n"
        "❖ ᴛᴀᴘ ᴛᴏ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ғᴏʀ ᴅᴇᴛᴀɪʟs.\n"
        "•────────────────────•\n"
        "❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :- <a href='https://t.me/suruchisupport'>sᴜʀᴜᴄʜɪ-x-ɴᴇᴛᴡᴏʀᴋ 🚩</a>\n"
        "•────────────────────•\n"
        f"☆ ᴏᴡɴᴇʀ: {owner}"
    )

    buttons = [
        [
            Button.url("•𝐂𝐇𝐀𝐍𝐍𝐄𝐋•", "https://t.me/suruchisupport"),
            Button.url("•𝐆𝐑𝐎𝐔𝐏•", "https://t.me/+fYnrOJSQP9I4ODlh")
        ],
        [Button.url("•𝐎𝐖𝐍𝐄𝐑•", f"https://t.me/{OWNER_USERNAME}")],
        [Button.inline("•𝐇𝐄𝐋𝐏", data=b"help_menu")]
    ]

    await event.reply(msg, file=VIDEO_URL, parse_mode="html", buttons=buttons)

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
    buttons = [[Button.inline("•𝐁𝐀𝐂𝐊•", data=b"back_start")]]
    await event.edit(
        """✦ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ

➻ /start - ꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ
➻ /gen - ʜᴏsᴛ ʏᴏᴜʀ ᴄʟɪᴇɴᴛ
➻ /clone - ᴄʟᴏɴᴇ ᴠɪᴀ sᴛʀɪɴɢ sᴇssɪᴏɴ
➻ /ping - ᴄʜᴇᴄᴋ ᴛʜᴇ ʙᴏᴛ ɪs ᴀʟɪᴠᴇ 

✦ ᴀʙᴏᴜᴛ ᴛʜɪꜱ ʙᴏᴛ

◍ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴛᴏ ʙᴏᴏsᴛ ʏᴏᴜʀ ɪᴅ ᴡɪᴛʜ ʙᴇᴀᴜᴛɪғᴜʟ ᴀɴɪᴍᴀᴛɪᴏɴ.


◌ ʟᴀɴɢᴜᴀɢᴇ : <a href='python.org'>'ᴘʏᴛʜᴏɴ'</a>
◌ ᴘᴏᴡᴇʀᴇᴅ ʙʏ : <a href='https://t.me/suruchisupport'>'ʀᴀᴅʜɪᴋᴀ-x-ɴᴇᴛᴡᴏᴇᴋ'</a>
◌ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/ll_Sexcy_Samar_ll'>'ᴅᴇᴠᴇʟᴏᴘᴇʀ'</a>""",
        parse_mode="html",
        buttons=buttons
    )

# Back button callback
async def back_start(event):
    user = await event.get_sender()
    mention = f'<a href="tg://user?id={user.id}">{user.first_name}</a>'
    owner = f'<a href="https://t.me/{OWNER_USERNAME}">{OWNER_NAME}</a>'

    buttons = [
        [
            Button.url("•𝐂𝐇𝐀𝐍𝐍𝐄𝐋•", "https://t.me/suruchisupport"),
            Button.url("•𝐆𝐑𝐎𝐔𝐏•", "https://t.me/+fYnrOJSQP9I4ODlh")
        ],
        [Button.url("•𝐎𝐖𝐍𝐄𝐑•", f"https://t.me/{OWNER_USERNAME}")],
        [Button.inline("•𝐇𝐄𝐋𝐏", data=b"help_menu")]
    ]

    await event.edit(
        f"┌────── ˹ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ˼ ⏤‌‌‌‌‌‌‌‌★\n"
        f"┆◍ ʜᴇʏ {mention}, ɪ ᴀᴍ : <a href='https://t.me/Suruchi_XUserbot'>sᴜʀᴜᴄʜɪ-x-ᴜsᴇʀʙᴏᴛ</a>\n"
        "┆◍ ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ ᴅᴇᴀʀ !! \n"
        "└────────────────────•\n"
        "❖ ɪ ᴀᴍ ᴀ ᴘᴏᴡᴇʀғᴜʟ & ᴜsᴇғᴜʟʟ ᴜsᴇʀʙᴏᴛ.\n"
        "❖ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ғᴏʀ ғᴜɴ ʀᴀɪᴅ sᴘᴀᴍ.\n"
        "❖ ɪ ᴄᴀɴ ʙᴏᴏsᴛ ʏᴏᴜʀ ɪᴅ ᴡɪᴛʜ ᴀɴɪᴍᴀᴛɪᴏɴ\n"
        "❖ ᴛᴀᴘ ᴛᴏ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ғᴏʀ ᴅᴇᴛᴀɪʟs.\n"
        "•────────────────────•\n"
        "❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :- <a href='https://t.me/suruchisupport'>sᴜʀᴜᴄʜɪ-x-ɴᴇᴛᴡᴏʀᴋ 🚩</a>\n"
        "•────────────────────•\n"
        f"☆ ᴏᴡɴᴇʀ: {owner}",
        parse_mode="html",
        buttons=buttons
    )
