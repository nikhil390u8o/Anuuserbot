import asyncio
import random

links = [
    "https://res.cloudinary.com/dyju9bym4/image/upload/v1754997821/IMG_20250812_163428_070_toituz.jpg",
    "https://res.cloudinary.com/dyju9bym4/image/upload/v1754997821/IMG_20250812_163427_806_u0fqkh.jpg",
    "https://res.cloudinary.com/dyju9bym4/image/upload/v1754997821/IMG_20250812_163427_482_ancj5y.jpg"
]

async def wtf_handle(client, event):
    # Use triple quotes for ASCII art
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

    # Animate letter by letter
    text = ""
    for letter in wtf:
        text += letter
        safe_text = text + "\u2060"  # Invisible char to force update
        await event.edit(safe_text)
        await asyncio.sleep(0.2)  # animation speed

    # After animation, send clickable image with final text
    random_link = random.choice(links)
    mention = f'<a href="{random_link}">{wtf}</a>'
    await event.edit(mention, parse_mode="html")
