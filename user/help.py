import asyncio

async def help_handle(client, event):
    # ✅ Delete the .help command message
    try:
        await event.delete()
    except:
        pass

    # 🍼 First short animation before showing help
    x = await event.respond("**ᴄᴏᴍɪɴɢ ʙᴀʙʏ....**")  # ✅ Fixed missing **
    await asyncio.sleep(0.2)  # wait a bit longer before editing

    # 📜 Full Help Menu (Quoted Commands)
    help_text = (
        "**🤖 𝗔𝗡𝗨 𝗨𝗦𝗘𝗥𝗕𝗢𝗧 𝗛𝗘𝗟𝗣 𝗠𝗘𝗡𝗨**\n\n"
        "**Available Commands:**\n"
        "> `.afk`\n"
        "> `.ban`\n"
        "> `.ba`\n"
        "> `.brain`\n"
        "> `.info`\n"
        "> `.clone`\n"
        "> `.dono`\n"
        "> `.help`\n"
        "> `.love`\n"
        "> `.lover`\n"
        "> `.mute`\n"
        "> `.nah`\n"
        "> `.ping`\n"
        "> `.raid`\n"
        "> `.marco`\n"
        "> `.spam`\n"
        "> `.type`\n"
        "> `.wtf`\n\n"
        "**Support**\n"
        "📢 **Support Channel:** @YourSupportChannel\n"
        "👑 **Owner:** @YourOwnerUsername"
    )

    await x.edit(help_text)

