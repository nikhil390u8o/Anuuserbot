import asyncio
import random

links = [
    "https://res.cloudinary.com/dyju9bym4/image/upload/v1754997821/IMG_20250812_163428_070_toituz.jpg",
    "https://res.cloudinary.com/dyju9bym4/image/upload/v1754997821/IMG_20250812_163427_806_u0fqkh.jpg",
    "https://res.cloudinary.com/dyju9bym4/image/upload/v1754997821/IMG_20250812_163427_482_ancj5y.jpg"
]

async def wtf_handle(client, event):
    wtf = (
        "ғᴜᴍᴋᴇᴅ ʙʏ\n"
        ".                       /¯ )\n"
        "                      /¯  /\n"
        "                    /    /\n"
        "              /´¯/'   '/´¯¯•¸\n"
        "          /'/   /    /       /¨¯\\ \n"
        "        ('(   (   (   (  ¯~/'  ')\n"
        "         \\                        /\n"
        "          \\                _.•´\n"
        "            \\              (\n"
        "              \\--------------\n"
        "               ))))))))))))\n"
    )

    # Split into chunks of 3-4 letters for faster editing
    chunk_size = 3
    text = ""
    for i in range(0, len(wtf), chunk_size):
        text += wtf[i:i+chunk_size]
        safe_text = text + "\u2060"  # Invisible char to force update
        await event.edit(safe_text)
        await asyncio.sleep(0.01)  # super fast animation

    # After animation, send clickable image with final text
    random_link = random.choice(links)
    mention = f'<a href="{random_link}">{wtf}</a>'
    await event.edit(mention, parse_mode="html")
