import random
import asyncio



h = ["❤️", "💖", "💗", "💓", "💞", "💕", "💘", "💝", "💟"]






def numbers():
    a = random.randint(0, 8)
    b = random.randint(0, 8)
    while b == a:
        b = random.randint(0, 8)
    return a, b


def gen_heart(bg, heart):
    pattern = [
        "0000000",
        "0110110",
        "1111111",
        "1111111",
        "0111110",
        "0011100",
        "0001000"
    ]
    
    h_msg = ""
    for row in pattern:
        for char in row:
            if char == "1":
                h_msg += heart
            else:
                h_msg += bg
        h_msg += "\n"  
    return h_msg




async def love_handle(client, event):
  for i in range(0, 16):
    a, b = numbers()
    bg = h[a]
    heart = h[b]
    h_msg = gen_heart(bg, heart)
    await event.edit(f"{h_msg}")
    
  love = "I Love You <3"
  for i in range(0,len(love)+1):
    ms = love[:i]
    try:
      await event.edit(ms)
    except:
      pass
  

async def loveyou_handle(client, event):
  art1 = random.choice(art)
  await event.edit(art1)
  
  


art = [
    """❤️ .LOVE:
  💖💖   💖💖
 💖💖💖 💖💖💖
 💖💖💖💖💖💖💖
  💖💖💖💖💖
   💖💖💖
    💖YOU💖""",

    """💕💕💕💕💕
💞      💞
 💖    💖
   💝💝💝
     💓
      💘""",

    """❤️❤️
💖 (´｡• ᵕ •｡`)  
💗   (づ￣ ³￣)づ
💘       💘
💝 LOVE 💝""",

    """💓💓💓💓💓
💞        💞
 💕      💕
  💖    💖
   💘  💘
    💝💝
     💟""",

    """❤️ LOVE ❤️
💞 FOREVER 💞
  (•‿•)  
 <)   )╯
  /   \\ """,

    """💖💖💖💖
💘      💘
 💝    💝
  💕  💕
   💞💞
    💓
     ❤️""",

    """💕💕💕💕💕
💖   YOU   💖
 💗       💗
  💘     💘
   💝   💝
    💞 💞
     ❤️"""
]
