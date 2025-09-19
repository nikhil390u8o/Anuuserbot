async def sm_handle(client, event):
    # try to delete the command message (force)
    try:
        await client.delete_messages(event.chat_id, [event.message.id])
    except Exception as e:
        print(f"⚠️ Could not delete .sm command: {e}")

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
        (
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
            "ғᴜᴍᴋᴇᴅ ʙʏ :- [ 𝗦𝗠 𝗙𝗨𝗖𝗞𝗘𝗥𝗦 ]\n"
            "𝗢𝗪𝗡𝗘𝗥 @tyson_8076 [𝗦𝗠]\n"
            "𝗕𝗢𝗧 𝗗𝗘𝗩 @ll_PANDA_BBY_ll [𝗦𝗠]"
        )
    ]

    # send the first message using client (guarantees a Message object you can edit)
    try:
        x = await client.send_message(event.chat_id, "Starting...")
    except Exception as e:
        print(f"❌ Failed to send starting message: {e}")
        return

    # recommend 0.7-1.0s between edits to avoid being ignored/rate-limited
    base_delay = 0.8

    for i, msg in enumerate(messages):
        try:
            await x.edit(msg)
        except errors.MessageIdInvalidError:
            # message can't be edited (rare). fallback: send a new message and continue with that
            try:
                x = await client.send_message(event.chat_id, msg)
            except Exception as ex:
                print(f"❌ Fallback send failed at step {i}: {ex}")
                return
        except Exception as e:
            print(f"⚠️ Edit failed at step {i}: {e}")
            # try to resend as fallback so sequence can continue
            try:
                x = await client.send_message(event.chat_id, msg)
            except Exception as ex:
                print(f"❌ Fallback send failed at step {i}: {ex}")
                return

        # longer pause before the final big ASCII art for readability
        if i == len(messages) - 1:
            await asyncio.sleep(0.2)
        else:
            await asyncio.sleep(base_delay)
