
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.types import Message

from config import SUDO_USER
from PANDA.data import RAID           # Your existing RAID list with Hindi abuses

# In-memory storage for users with active reply-raid (resets on bot restart)
RAIDS = []

@Client.on_message(filters.command("rraid", prefixes=".") & (filters.me | filters.user(SUDO_USER)))
async def start_rraid(client: Client, message: Message):
    """
    .rraid → start auto-reply raid on replied user or mentioned user
    """
    target = None

    # Priority: replied message
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user

    # Fallback: .rraid @username or .rraid 123456789
    elif len(message.command) > 1:
        arg = message.command[1]
        try:
            target = await client.get_users(arg)
        except Exception:
            return await message.reply_text("`Invalid user / not found`")

    if not target:
        return await message.reply_text(
            "**Usage:**\n"
            "• `.rraid` (reply to user)\n"
            "• `.rraid @username` or `.rraid 123456789`"
        )

    if target.id in RAIDS:
        return await message.reply_text(
            f"**Already raiding** [{target.first_name}](tg://user?id={target.id})"
        )

    # Optional: protect yourself / devs / sudo users
    if target.is_self or target.id in SUDO_USER:
        return await message.reply_text("`Cannot raid myself or sudo users`")

    RAIDS.append(target.id)
    await message.reply_text(
        f"**Reply-Raid started** → [{target.first_name}](tg://user?id={target.id})\n"
        f"They will now receive random messages from the RAID list on every reply."
    )


@Client.on_message(~filters.me & filters.incoming, group=5)  # group=5 to run after other handlers
async def rraid_trigger(client: Client, message: Message):
    """
    Auto-reply when someone in RAIDS list messages anywhere
    """
    if not message.from_user:
        return

    if message.from_user.id in RAIDS:
        try:
            text = random.choice(RAID)
            # Random human-like delay
            await asyncio.sleep(random.uniform(1.2, 4.0))
            await message.reply(text)
        except Exception:
            # Silent fail on floodwait, deleted messages, etc.
            pass


@Client.on_message(filters.command("drraid", prefixes=".") & (filters.me | filters.user(SUDO_USER)))
async def stop_rraid(client: Client, message: Message):
    """
    .drraid → stop reply-raid on user
    """
    target = None

    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user

    elif len(message.command) > 1:
        arg = message.command[1]
        try:
            target = await client.get_users(arg)
        except Exception:
            return await message.reply_text("`Invalid user / not found`")

    if not target:
        return await message.reply_text(
            "**Usage:**\n"
            "• `.drraid` (reply to user)\n"
            "• `.drraid @username`"
        )

    if target.id not in RAIDS:
        return await message.reply_text(
            f"**No active reply-raid** on [{target.first_name}](tg://user?id={target.id})"
        )

    RAIDS.remove(target.id)
    await message.reply_text(
        f"**Reply-Raid stopped** on [{target.first_name}](tg://user?id={target.id})"
    )


# Optional: add to help menu
try:
    from user.help import add_command_help
    add_command_help(
        "rraid",
        [
            [".rraid", "Start auto-reply raid (reply or @username)"],
            [".drraid", "Stop auto-reply raid (reply or @username)"],
        ],
    )
except ImportError:
    pass
