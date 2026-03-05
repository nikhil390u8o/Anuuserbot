# user/rraid.py

import asyncio
import random
from pyrogram import Client, filters
from pyrogram.types import Message

from config import SUDO_USERS   # agar config mein SUDO_USERS hai toh yeh use karo
# ya agar SUDO_USER (singular) hai toh change kar dena: from config import SUDO_USER

from PANDA.data import RAID     # tumhara RAID list

# Global list (in-memory) – bot restart hone par clear ho jayega
ACTIVE_RRAID = []

@Client.on_message(filters.command("rraid", prefixes=".") & (filters.me | filters.user(SUDO_USERS)))
async def rraid_handle(client: Client, message: Message):
    """
    .rraid → kisi user par reply-raid start karo
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
            "• `.rraid` (kisi message ka reply karke)\n"
            "• `.rraid @username` ya `.rraid 123456789`"
        )

    if target.is_self:
        return await message.reply_text("`Apne par raid nahi kar sakta.`")
    if target.id in SUDO_USERS:
        return await message.reply_text("`Sudo user par raid nahi kar sakta.`")

    if target.id in ACTIVE_RRAID:
        return await message.reply_text(f"**Already raiding** → {target.mention}")

    ACTIVE_RRAID.append(target.id)

    await message.reply_text(
        f"**Reply-Raid shuru** → {target.mention}\n"
        "Ab iske har message ka jawab raid list se milega."
    )


@Client.on_message(~filters.me & filters.incoming, group=10)
async def rraid_auto_reply(client: Client, message: Message):
    """
    Jo user ACTIVE_RRAID mein hai, uske har message par auto-reply
    """
    if not message.from_user:
        return

    if message.from_user.id in ACTIVE_RRAID:
        try:
            abuse = random.choice(RAID)
            await asyncio.sleep(random.uniform(1.3, 4.2))  # natural delay
            await message.reply(abuse)
        except Exception:
            pass  # flood ya error aaye to ignore
