from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot import bot, CMD_HELP


@register(outgoing=True, pattern=r"^\;id(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("please reply to message master")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("please reply to message master")
        return
    chat = "@getidsbot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("please reply to message master")
        return
    await event.edit("geting ID.......")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=186675376))
            await bot.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("bot is error")
            return
        if response.text.startswith("Forward"):
            await event.edit("master, This Man's  Has No ID")
        else:
            await event.edit(f"{response.message.message}")


CMD_HELP.update({
    "getid":
    ";id"
    "\nUsage: Reply To User Message To Get His ID."
})
