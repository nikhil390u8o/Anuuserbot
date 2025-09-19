



from telethon import Button
import time
from session import ping  # dictionary storing bot start time

CHANNEL = "BAMBI799U"  # channel username
MSG_ID = 139            # message ID of the video

def get_ping():
    start = time.time()
    time.sleep(0.01)
    end = time.time()
    return f"{int((end - start) * 1000)}ms"

def get_uptime(start_timestamp):
    seconds = int(time.time()) - int(start_timestamp)

    minute = 60
    hour = 60 * minute
    day = 24 * hour
    week = 7 * day
    month = 30 * day
    year = 365 * day

    years = seconds // year; seconds %= year
    months = seconds // month; seconds %= month
    weeks = seconds // week; seconds %= week
    days = seconds // day; seconds %= day
    hours = seconds // hour; seconds %= hour
    minutes = seconds // minute; seconds %= minute

    result = []
    if years: result.append(f"{years}y")
    if months: result.append(f"{months}M")
    if weeks: result.append(f"{weeks}w")
    if days: result.append(f"{days}d")
    if hours: result.append(f"{hours}h")
    if minutes: result.append(f"{minutes}m")
    if seconds or not result: result.append(f"{seconds}s")

    return " ".join(result)

# ───────────── /ping Handler ─────────────
async def ping_handle(client, event):
    buttons = [[Button.url("𝐒𝐔𝐏𝐏𝐎𝐑𝐓", "https://t.me/YourSupportGroup")]]

    # Step 1: Get the video from Telegram channel
    try:
        video_msg = await client.get_messages(CHANNEL, ids=MSG_ID)
        media = video_msg.media
    except Exception as e:
        await event.respond(f"❌ Failed to get video: {e}")
        return

    # Step 2: Send "Pinging..." with video
    msg = await event.respond("<b>ᴘɪɴɢɪɴɢ...</b>", file=media, parse_mode="html", buttons=buttons)

    # Step 3: Calculate ping & uptime
    start_ts = ping.get("time", time.time())
    uptime = get_uptime(start_ts)
    latency = get_ping()

    # Step 4: Edit the same message with stats
    final_text = (
        "<blockquote>ᴘᴏɴɢ!!</blockquote>\n"
        f"<b>ᴘɪɴɢ:</b> {latency}\n"
        f"<b>ᴜᴘᴛɪᴍᴇ:</b> {uptime}\n"
    )
    await msg.edit(final_text, parse_mode="html", buttons=buttons)
