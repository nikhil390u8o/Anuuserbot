import asyncio
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import AudioPiped
import config

app = Client(
    "vc_user",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    session_string=config.USER_SESSION
)

pytgcalls = PyTgCalls(app)

@app.on_message(filters.command("join", prefixes=".") & filters.group)
async def join_vc(_, message):
    try:
        await pytgcalls.join_group_call(
            message.chat.id,
            AudioPiped(
                "mic",
                audio_parameters={"volume": 200}
            ),
        )
        await message.reply("🔊 Joined VC with boosted mic")
    except Exception as e:
        await message.reply(f"❌ VC error:\n`{e}`")

async def start_vc():
    await app.start()
    await pytgcalls.start()
    await asyncio.Event().wait()

