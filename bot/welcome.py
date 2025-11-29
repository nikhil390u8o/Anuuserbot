import random
import asyncio
from telethon import events, Button

WELCOME_IMAGES = [
    "https://files.catbox.moe/d8mnv9.jpg",
    "https://files.catbox.moe/4d7s4u.jpg",
    "https://files.catbox.moe/orqaah.jpg"
]

WELCOME_TEXT = """🌸✨ ──────────────────── ✨🌸  
🎊 <b>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴏᴜʀ ɢʀᴏᴜᴘ</b> 🎊  
  
🌹 <b>ɴᴀᴍᴇ</b> ➤ {name}  
🆔 <b>ᴜsᴇʀ ɪᴅ</b> ➤ <code>{user_id}</code>  
🏠 <b>ɢʀᴏᴜᴘ</b> ➤ {chat_title}  
  
💕 <b>ᴡᴇ'ʀᴇ sᴏ ʜᴀᴘᴘʏ ᴛᴏ ʜᴀᴠᴇ ʏᴏᴜ ʜᴇʀᴇ!</b>  
✨ <b>ғᴇᴇʟ ғʀᴇᴇ ᴛᴏ sʜᴀʀᴇ ᴀɴᴅ ᴇɴᴊᴏʏ!</b>  
⚡ <b>ᴇɴᴊᴏʏ ʏᴏᴜʀ ᴇxᴘᴇʀɪᴇɴᴄᴇ ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ</b>  
  
💝 <b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➤</b> <a href="https://t.me/XTREAME_BOTS">[𝗔𝗟𝗧𝗥𝗢𝗡 ✘ 𝗕𝗢𝗧𝗦]</a>  
🌸✨ ──────────────────── ✨🌸  
"""

WELCOME_BUTTONS = [
    [
        Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/ALTR0N_BOTS"),
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/PURANI_HVELI")
    ]
]


async def welcome_user(event):

    # ❌ FIX: STOP DOUBLE WELCOME
    if not (event.user_joined or event.user_added):
        return

    # Extra double-filter safety  
    if event.user_joined and event.user_added:
        return

    try:
        user = await event.get_user()
        chat = await event.get_chat()
        name = user.first_name or "User"
        uid = user.id
        image = random.choice(WELCOME_IMAGES)
        caption = WELCOME_TEXT.format(
            name=name,
            user_id=uid,
            chat_title=chat.title
        )

        msg = await event.client.send_file(
            chat.id,
            image,
            caption=caption,
            buttons=WELCOME_BUTTONS,
            parse_mode="html"
        )

        await asyncio.sleep(60)
        await msg.delete()

    except Exception as e:
        print(f"[WELCOME ERROR] {e}")