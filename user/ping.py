import time
import datetime
import asyncio

BOT_START_TIME = time.time()

async def ping_handle(client, event):
    """
    .ping command with smooth 10%-100% loading animation
    and a fancy final output.
    """
    start = time.monotonic()
    await event.delete()

    # Send initial message
    loading = await event.respond("ᴘɪɴɢɪɴɢ...")

    # Show progress from 20 to 100
    for percent in range(20, 101, 10):
        await asyncio.sleep(0.10)
        await loading.edit(f"ᴘɪɴɢɪɴɢ... {percent}%**")

    # Calculate latency & uptime
    end = time.monotonic()
    ping_ms = round((end - start) * 1000, 2)
    uptime_sec = int(time.time() - BOT_START_TIME)
    uptime = str(datetime.timedelta(seconds=uptime_sec))

    me = await client.get_me()
    fullname = f"{me.first_name or ''} {me.last_name or ''}".strip()

    # Final styled message
    output = (
         "❏   ❖ [ʀᴀᴅʜɪᴋᴀ-x-ɴᴇᴛᴡᴏʀᴋ](https://t.me/RADHIKA_YIIOO) ™ ╮\n"
        f"├•  ❖ 𝐒ᴘᴇᴇᴅ - `{ping_ms} ms`\n"
        f"├•  ❖ 𝐔ᴘᴛɪᴍᴇ - `{uptime}`\n"
        f"└•  ❖ 𝐍ᴀᴍᴇ: ⏤‌‌‌‌‌‌‌‌ `{fullname}`"
    )

    await loading.edit(output)
