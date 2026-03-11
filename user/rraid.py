import asyncio
import random
from pyrogram import Client, filters
from pyrogram.types import Message

from config import SUDO_USERS
from Samar.data import RAID  # Your RAID messages list

# Global list of user IDs currently under reply-raid (in-memory only)
ACTIVE_RRAID = []

@Client.on_message(filters.command("rraid", prefixes=".") & (filters.me | filters.user(SUDO_USERS)))
async def rraid_handle(client: Client, message: Message):
    """
    .rraid  →  Start reply-raid on a user (they get auto-replied with random abuses)
    Usage:
      • Reply to user → .rraid
      • Mention user  → .rraid @username
    """
    target = None

    # Case 1: Replied to a message
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user

    # Case 2: Provided username or ID
    elif len(message.command) > 1:
        arg = message.command[1]
        try:
            target = await client.get_users(arg)
        except Exception:
            return await message.reply_text("`Couldn't find that user.`")

    if not target:
        return await message.reply_text(
            "**Usage:**\n"
            "• `.rraid` (reply to someone)\n"
            "• `.rraid @username` or `.rraid 123456789`"
        )

    # Basic protection
    if target.is_self:
        return await message.reply_text("`I won't raid myself.`")
    if target.id in SUDO_USERS:
        return await message.reply_text("`Can't raid a sudo user.`")

    if target.id in ACTIVE_RRAID:
        return await message.reply_text(
            f"**Already raiding** → [{target.first_name}](tg://user?id={target.id})"
        )

    ACTIVE_RRAID.append(target.id)

    await message.reply_text(
        f"**Reply-Raid activated** on [{target.first_name}](tg://user?id={target.id})\n"
        "Every message they send will now get a random reply from the raid list."
    )


@Client.on_message(~filters.me & filters.incoming, group=10)
async def rraid_auto_reply(client: Client, message: Message):
    """
    Automatically replies to messages from users in ACTIVE_RRAID list
    group=10 → runs after most other handlers
    """
    if not message.from_user:
        return

    if message.from_user.id in ACTIVE_RRAID:
        try:
            abuse = random.choice(RAID)
            # Random delay to look more natural / avoid flood detection
            await asyncio.sleep(random.uniform(1.3, 4.2))
            await message.reply(abuse)
        except Exception:
            # Silent fail (floodwait, permissions, deleted msg, etc.)
            pass
