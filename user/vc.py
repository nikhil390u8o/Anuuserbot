from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import AudioPiped
from pyrogram import Client, filters
import os

app = Client
pytgcalls = PyTgCalls(app)

@pytgcalls.on_stream_end()
async def stream_end(_, update):
    await pytgcalls.leave_group_call(update.chat_id)

@app.on_message(filters.command("join", prefixes=".") & filters.group)
async def join_vc(client, message):
    chat_id = message.chat.id

    try:
        await pytgcalls.join_group_call(
            chat_id,
            AudioPiped(
                "mic",  # mic input
                audio_parameters={
                    "volume": 200  # software gain (100 = normal)
                }
            ),
        )
        await message.reply("🔊 **Joined VC with boosted mic**")
    except Exception as e:
        await message.reply(f"❌ VC join failed:\n`{e}`")
