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
        f"<blockquote>Hey there! {mention}</blockquote>\n"
        "➠ I'm a Userbot Creator Bot\n"
        "➠ Use me to create your own userbot\n"
        "<blockquote>Steps to create a userbot:</blockquote>\n"
        "➠ /gen – Generate a string session\n"
        "➠ /clone <your string session> – Clone the userbot\n"
        "➠ /ping – Check bot is alive or not\n\n"
        f"➠ Owner : {owner}\n"
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
        "📖 <b>Help Menu</b>\n\n"
        "➠ /gen – Generate a string session\n"
        "➠ /clone <session> – Clone userbot\n"
        "➠ /ping – Alive check",
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
        [Button.url("Channel", "https://t.me/YourSupportChannel"),
         Button.url("Group", "https://t.me/YourSupportGroup")],
        [Button.url("Owner", f"https://t.me/{OWNER_USERNAME}"),
         Button.inline("Help", data=b"help_menu")]
    ]

    await event.edit(
        f"<blockquote>Hey there! {mention}</blockquote>\n"
        "➠ I'm a Userbot Creator Bot\n"
        "➠ Use me to create your own userbot\n"
        "<blockquote>Steps to create a userbot:</blockquote>\n"
        "➠ /gen – Generate a string session\n"
        "➠ /clone <your string session> – Clone the userbot\n"
        "➠ /ping – Check bot is alive or not\n\n"
        f"➠ Owner : {owner}\n",
        parse_mode="html",
        buttons=buttons
    )
