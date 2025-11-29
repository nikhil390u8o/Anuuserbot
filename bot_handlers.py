from telethon import events
from bot.clone import clone_handle
from bot.gen import gen_handle
from bot.start import start_handle, help_menu, back_start
from bot.ping import ping_handle
from bot.send import send_handle
from bot.log import log_msg
from bot.addhelp import addhelp_handle
from bot.welcome import welcome_user   # <-- ADD THIS


def register(client):
    # log all messages
    @client.on(events.NewMessage())
    async def handle_user_messages(event):
        if event.out:
            return
        await log_msg(client, event)

    # /addhelp
    @client.on(events.NewMessage(pattern=r"^/addhelp(\s.*)?$"))
    async def addhelp_cmd(event):
        await addhelp_handle(client, event)

    # /start
    @client.on(events.NewMessage(pattern=r"^/start$"))
    async def start_cmd(event):
        await start_handle(event)
    
    @client.on(events.NewMessage(pattern=r"welcome(\s.*)?$"))
    async def welcome_cmd(event):
        await welcome_handle(event)
     
    # /gen
    @client.on(events.NewMessage(pattern=r"^/gen(\s.*)?$"))
    async def gen_cmd(event):
        await gen_handle(client, event)

    # /ping
    @client.on(events.NewMessage(pattern=r"^/ping(\s.*)?$"))
    async def ping_cmd(event):
        await ping_handle(client, event)

    # /send
    @client.on(events.NewMessage(pattern=r"^/send(\s.*)?$"))
    async def send_cmd(event):
        await send_handle(client, event)

    # /clone
    @client.on(events.NewMessage(pattern=r'^/clone(?:\s+(.+))?$'))
    async def clone_handler(event):
        await clone_handle(client, event)

    # Inline button: Help
    @client.on(events.CallbackQuery(data=b"help_menu"))
    async def callback_help(event):
        await help_menu(event)

    # Inline button: Back
    @client.on(events.CallbackQuery(data=b"back_start"))
    async def callback_back(event):
        await back_start(event)

    # Auto Welcome Handler
    @client.on(events.ChatAction())
    async def welcome_event(event):
        await welcome_user (event)