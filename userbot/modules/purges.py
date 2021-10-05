from asyncio import sleep

from telethon.errors import rpcbaseerrors

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\;purge$")
async def fastpurger(purg):
    chat = await purg.get_input_chat()
    msgs = []
    itermsg = purg.client.iter_messages(chat, min_id=purg.reply_to_msg_id)
    count = 0

    if purg.reply_to_msg_id is not None:
        async for msg in itermsg:
            msgs.append(msg)
            count += 1
            msgs.append(purg.reply_to_msg_id)
            if len(msgs) == 100:
                await purg.client.delete_messages(chat, msgs)
                msgs = []
    else:
        return await purg.edit("please reply to message master ツ ")

    if msgs:
        await purg.client.delete_messages(chat, msgs)
    done = await purg.client.send_message(
        purg.chat_id, f"succesfully delete message master\
        \n*Number of Deleted Messages {str(count)} message*")
    """
    if BOTLOG:
        await purg.client.send_message(
            BOTLOG_CHATID,
            "*succesfully delete message master *" + str(count) + "* Message Cleared Successfully.*")
    """
    await sleep(2)
    await done.delete()


@register(outgoing=True, pattern=r"^\;purgeme")
async def purgeme(delme):
    message = delme.text
    count = int(message[9:])
    i = 1

    async for message in delme.client.iter_messages(delme.chat_id, from_user="me"):
        if i > count + 1:
            break
        i += 1
        await message.delete()

    smsg = await delme.client.send_message(
        delme.chat_id,
        "*succesfully delete message master *" + str(count) + "* Message Cleared Successfully ツ*",
    )
    """
    if BOTLOG:
        await delme.client.send_message(
            BOTLOG_CHATID,
            "*succesfully delete message master *" + str(count) + "* Message Cleared Successfully ツ*")
    """
    await sleep(2)
    i = 1
    await smsg.delete()


@register(outgoing=True, pattern=r"^\;del$")
async def delete_it(delme):
    msg_src = await delme.get_reply_message()
    if delme.reply_to_msg_id:
        try:
            await msg_src.delete()
            await delme.delete()
            """
            if BOTLOG:
                await delme.client.send_message(
                    BOTLOG_CHATID, "_master, succesfully delete message ツ_")
            """
        except rpcbaseerrors.BadRequestError:
            await delme.edit("cannot delete message")
            """
            if BOTLOG:
                await delme.client.send_message(
                    BOTLOG_CHATID, "cannot delete message")
            """


@register(outgoing=True, pattern=r"^\;edit")
async def editer(edit):
    message = edit.text
    chat = await edit.get_input_chat()
    self_id = await edit.client.get_peer_id("me")
    string = str(message[6:])
    i = 1
    async for message in edit.client.iter_messages(chat, self_id):
        if i == 2:
            await message.edit(string)
            await edit.delete()
            break
        i += 1
    """
    if BOTLOG:
        await edit.client.send_message(BOTLOG_CHATID,
                                       "succesfully edit message")
   """


@register(outgoing=True, pattern=r"^\;sd")
async def selfdestruct(destroy):
    message = destroy.text
    counter = int(message[4:6])
    text = str(destroy.text[6:])
    await destroy.delete()
    smsg = await destroy.client.send_message(destroy.chat_id, text)
    await sleep(counter)
    await smsg.delete()
    """
    if BOTLOG:
        await destroy.client.send_message(BOTLOG_CHATID,
                                          "SD Done Successfully ")
    """


CMD_HELP.update({"purge": ">;purge"
                  "\nUsage: Clears all messages starting from the reply message.",
                  "purgeme": ">;purgeme <number>"
                  "\nUsage: Delete the number of your messages, which you want to delete.",
                  "del": ">;del"
                  "\nUsage: Delete message, reply to message.",
                  "edit": ">;edit <new message>"
                  "\nUsage: Replace your last message with <new message>.",
                  "sd": ">;sd <x> <message>"
                  "\nUsage: Creates a self-destruct message in x seconds."
                  "\nKeep seconds below 100 because your bot will sleep.",
                 })
