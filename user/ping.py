import time
import datetime
import asyncio

BOT_START_TIME = time.time()

async def ping_handle(client, event):
    """
    .ping command with ALPHA-style animation and final output
    """
    start = time.monotonic()
    await event.delete()

    # Initial loading message
    loading = await event.respond("0% ▒▒▒▒▒▒▒▒▒▒")

    # An𝗔𝗟𝗣ages (similar to your ALPHA example)
    stages = [
        ("20% ███ ᴀʀᴜ ᴏᴘ▒▒▒▒▒", 0.08),
        ("40% ████ ᴀʀᴜ ɪs▒▒▒▒", 0.08),
        ("60% ██████ ᴀʀᴜ ᴄᴏᴍᴇ▒▒", 0.09),
        ("80% ████████ ᴀʀᴜ▒▒▒▒", 0.09),
        ("100%██████████ ᴄᴏᴍɪɴɢ", 0.10),
    ]

    for text, delay in stages:
        await asyncio.sleep(delay)
        await loading.edit(text)

    # Calculate real ping time and uptime
    end = time.monotonic()
    ping_ms = round((end - start) * 1000, 1)  # 1 decimal is usually enough
    uptime_sec = int(time.time() - BOT_START_TIME)
    uptime = str(datetime.timedelta(seconds=uptime_sec)).split('.')[0]  # remove microseconds

    me = await client.get_me()
    fullname = f"{me.first_name or ''} {me.last_name or ''}".strip() or me.username or "User"

    # Final output in similar style
    output = (
        "❏ ╰☞ 😈ᴀʀᴜ😈\n"
        f"├• ╰☞ 𝐒ᴘᴇᴇᴅ {ping_ms} ms\n"
        f"├• ╰☞ 𝐔ᴘᴛɪᴍᴇ {uptime}\n"
        f"└• ╰☞ 𝐍ᴀᴍᴇ: {fullname}"
    )

    await loading.edit(output)
