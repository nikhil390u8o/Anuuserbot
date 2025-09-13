# user/info.py

async def info_handle(client, event):
    """
    Handle the .info command: fetch and show user information.
    Works with reply, username/ID, or by default your own account.
    """
    replied = await event.get_reply_message()
    input_str = event.pattern_match.group(1)

    # Decide which user to fetch
    if replied:
        user_identifier = replied.sender_id
    elif input_str:
        user_identifier = input_str
    else:
        user_identifier = event.sender_id

    try:
        user = await client.get_entity(user_identifier)

        info = f"""
**👤 User Info**
🆔 ID: `{user.id}`
👤 First Name: {user.first_name or 'N/A'}
👥 Last Name: {user.last_name or 'N/A'}
🔗 Username: @{user.username if user.username else 'N/A'}
🤖 Bot: {user.bot}
✔️ Verified: {user.verified}
⛔ Restricted: {user.restricted}
"""
        await event.reply(info.strip())

    except Exception as e:
        await event.reply(f"❌ Error while fetching info: {str(e)}")
