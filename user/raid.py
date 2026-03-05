import asyncio
from PANDA.data import RAID

async def raid_handle(client, event):
  """
  Usage (reply to a user's message with):
    .raid 10        -> send 10 abusive messages as a reply
    .raid           -> default 5 messages
  Only works when used as a reply to a user's message.
  """
  text = event.raw_text
  parts = text.split(maxsplit=1)
  times = 5
  if len(parts) > 1 and parts[1].strip():
    try:
      times = int(parts[1].strip())
    except:
      await event.edit("`The argument must be an integer. Example: .raid 10`")
      return

  # Ensure the command is a reply
  if not event.is_reply:
    await event.edit("`Reply to a user's message to raid them.`")
    return

  # Get the replied message so responses are threaded to that user
  replied = await event.get_reply_message()

  await event.delete()

  for i in range(times):
    # choose message in a round-robin way to avoid heavy randomness
    msg = RAID[i % len(RAID)]
    # respond to the replied message (keeps the target visible)
    await event.respond(msg, reply_to=replied.id)
    await asyncio.sleep(0.0)
