from pyrogram import Client, filters
from pyrogram.types import Message

from config import SUDO_USERS   # same as above

# ACTIVE_RRAID list ko share karne ke liye rraid.py se import kar rahe hain
from user.rraid import ACTIVE_RRAID


@Client.on_message(filters.command("drraid", prefixes=".") & (filters.me | filters.user(SUDO_USERS)))
async def drraid_handle(client: Client, message: Message):
    """
    .drraid → kisi user par reply-raid band karo
    """
    target = None

    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user

    elif len(message.command) > 1:
        arg = message.command[1]
        try:
            target = await client.get_users(arg)
        except Exception:
            return await message.reply_text("`User nahi mila.`")

    if not target:
        return await message.reply_text(
            "**Use karne ka tarika:**\n"
            "• `.drraid` (kisi message ka reply karke)\n"
            "• `.drraid @username` ya `.drraid 123456789`"
        )

    if target.id not in ACTIVE_RRAID:
        return await message.reply_text(f"**Raid chal nahi raha** → {target.mention}")

    ACTIVE_RRAID.remove(target.id)

    await message.reply_text(
        f"**Reply-Raid band** → {target.mention}"
    )
