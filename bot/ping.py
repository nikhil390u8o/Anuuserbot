



from telethon import Button
import time
from session import ping

IMG_URL = "https://files.catbox.moe/1f21lw.jpg"  # replace with your image

def get_ping():
    start = time.time()
    time.sleep(0.05)  # simulate delay
    end = time.time()
    ping_ms = (end - start) * 1000
    return f"{int(ping_ms)}ms"

def get_time(old_timestamp):
    seconds = int(time.time()) - int(old_timestamp)

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

# /ping command
async def ping_handle(client, event):
    # Step 1: send "Pinging..." with image
    buttons = [[Button.url("馃摙 Support", "https://t.me/YourSupportGroup")]]
    msg = await event.respond("鈴� <b>Pinging...</b>", file=IMG_URL, parse_mode="html", buttons=buttons)

    # Step 2: calculate ping & uptime
    ts = ping.get("time")
    since = get_time(ts)
    ms = get_ping()

    final_msg = (
        "<blockquote>Pong! 馃彄</blockquote>\n"
        f"鉃� <b>Ping</b> 鈥� {ms}\n"
        f"鉃� <b>Uptime</b> 鈥� {since}\n"
    )

    # Step 3: edit same message
    await msg.edit(final_msg, parse_mode="html", buttons=buttons)
