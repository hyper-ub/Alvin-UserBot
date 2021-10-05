from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import CMD_HELP, bot
from userbot.events import register


@register(outgoing=True, pattern=r"^\;detect(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    reply_message = await event.get_reply_message()
    if not event.reply_to_msg_id:
        await event.edit("_master, Please Reply To User Message or type .detect (ID/Username) which you want to detect_")
        return
    if input_str:
        try:
            uid = int(input_str)
        except ValueError:
            try:
                u = await event.client.get_entity(input_str)
            except ValueError:
                await edit.event("_master, Please Provide ID/Username to find History_"
                                 )
            uid = u.id
    else:
        uid = reply_message.sender_id
    chat = "@tgscanrobot"
    event = await event.edit("_detected..._")
    async with bot.conversation(chat) as conv:
        try:
            await conv.send_message(f"{uid}")
        except YouBlockedUserError:
            await steal.reply(
                "*master please Unblock @tgscanrobot and try again*"
            )
        response = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.edit(response.text)


def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"[{full_name}](tg://user?id={user.id})"


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    return " ".join(names)


# Alvin Ganteng
CMD_HELP.update({
    "detect":
        ":detect\
          \nexplanation: view the History of Groups Ever/Currently Entered."
})
