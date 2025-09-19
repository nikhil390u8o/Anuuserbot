from telethon import events
import asyncio


# New handler function
async def sm_handle(client, event):
    messages = [
        "ʙᴀʙᴜ",
        "ʙᴀʙᴜ ᴅʜᴇʀ",
        "ʙᴀʙᴜ ᴅʜᴇʀ ᴍᴀᴛ",
        "ʙᴀʙᴜ ᴅʜᴇʀ ᴍᴀᴛ ʙᴏʟɴᴀ",
        "ʙᴀʙᴜ ᴅʜᴇʀ ᴍᴀᴛ ʙᴏʟɴᴀ ɴᴀʜɪ",
        "ʙᴀʙᴜ ᴅʜᴇʀ ᴍᴀᴛ ʙᴏʟɴᴀ ɴᴀʜɪ ᴛᴏ",
        "ʙᴀʙᴜ ᴅʜᴇʀ ᴍᴀᴛ ʙᴏʟɴᴀ ɴᴀʜɪ ᴛᴏ ʏᴀʜɪ",
        "ʙᴀʙᴜ ᴅʜᴇʀ ᴍᴀᴛ ʙᴏʟɴᴀ ɴᴀʜɪ ᴛᴏ ʏᴀʜɪ ᴘᴇ",
        "ʙᴀʙᴜ ᴅʜᴇʀ ᴍᴀᴛ ʙᴏʟɴᴀ ɴᴀʜɪ ᴛᴏ ʏᴀʜɪ ᴘᴇ ᴘᴀʟᴇ ᴅᴇɴɢᴇ 💀",
        """ғᴜᴍᴋᴇᴅ ʙʏ 
.                       /¯ )
                      /¯  /
                    /    /
              /´¯/'   '/´¯¯•¸
          /'/   /    /       /¨¯\\ 
        ('(   (   (   (  ¯~/'  ')
         \\                        /
          \\                _.•´
            \\              (
              \\--------------
               ))))))))))))
ғᴜᴍᴋᴇᴅ ʙʏ :- [ 𝗦𝗠 𝗙𝗨𝗖𝗞𝗘𝗥𝗦 ]
𝗢𝗪𝗡𝗘𝗥 @tyson_8076 [𝗦𝗠]
𝗕𝗢𝗧 𝗗𝗘𝗩 @ll_PANDA_BBY_ll [𝗦𝗠]"""
    ]

    x = await event.respond("ᴄᴏᴍɪɴɢ ʙᴇᴛᴀ ᴊɪ 😈...")
    for msg in messages:
        await x.edit(msg)
        await asyncio.sleep(0.1)  # Change timing for animation speed
