from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot import bot, CMD_HELP

@register(outgoing=True, pattern="^;ig ?(.*)")
async def insta(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("_master,please replt to instagram link_")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("Sorry master, I Need Instagram Media Link To Download")
        return
    chat = "@SaveAsBot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("_processing....._")
        return
    await event.edit("_processing....._")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=523131145)
            )
            await event.client.send_message(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.edit("master, please unblock @SaveAsbot and try again")
            return
        if response.text.startswith("Forward"):
            await event.edit(
                "Uhmm Private maybe."
            )
        else:
            await event.delete()
            await event.client.send_file(
                event.chat_id,
                response.message.media,
                caption=f"**Download By @Alvin_userbot_Group**",
            )
            await event.client.send_read_acknowledge(conv.chat_id)
            await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
            await event.delete()

CMD_HELP.update({"instagram": "**Modules:** __Instagram__\n\n**command:** ;i`"
                 "\n**explanation:** Download Media on Instagram Posts, Reply to the Instagram link, type ;ig"})
