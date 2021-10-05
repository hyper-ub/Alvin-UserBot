""" Userbot module for filter commands """

from asyncio import sleep
from re import search, IGNORECASE, escape
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP
from userbot.events import register


@register(incoming=True, disable_edited=True, disable_errors=True)
async def filter_incoming_handler(handler):
    """ Checks if the incoming message contains handler of a filter """
    try:
        if not (await handler.get_sender()).bot:
            try:
                from userbot.modules.sql_helper.filter_sql import get_filters
            except AttributeError:
                await handler.edit("running in Non-SQL Mode !")
                return
            name = handler.raw_text
            filters = get_filters(handler.chat_id)
            if not filters:
                return
            for trigger in filters:
                pattern = (
                    r"( |^|[^\w])" + escape(trigger.keyword) + r"( |$|[^\w])")
                pro = search(pattern, name, flags=IGNORECASE)
                if pro and trigger.f_mesg_id:
                    msg_o = await handler.client.get_messages(
                        entity=BOTLOG_CHATID, ids=int(trigger.f_mesg_id))
                    await handler.reply(msg_o.message, file=msg_o.media)
                elif pro and trigger.reply:
                    await handler.reply(trigger.reply)
    except AttributeError:
        pass


@register(outgoing=True, pattern=r"^;filter (.*)")
async def add_new_filter(new_handler):
    """ For .filter command, allows adding new filters in a chat """
    try:
        from userbot.modules.sql_helper.filter_sql import add_filter
    except AttributeError:
        await new_handler.edit("running in Non-SQL Mode !`")
        return
    value = new_handler.pattern_match.group(1).split(None, 1)
    """ - The first words after .filter(space) is the keyword - """
    keyword = value[0]
    try:
        string = value[1]
    except IndexError:
        string = None
    msg = await new_handler.get_reply_message()
    msg_id = None
    if msg and msg.media and not string:
        if BOTLOG_CHATID:
            await new_handler.client.send_message(
                BOTLOG_CHATID, f"#FILTER\nID CHAT: {new_handler.chat_id}\nTRIGGER: {keyword}"
                "\n\n_The Following Message Is Saved As Reply Data Filter For Chat Please Don't Delete It master_"
            )
            msg_o = await new_handler.client.forward_messages(
                entity=BOTLOG_CHATID,
                messages=msg,
                from_peer=new_handler.chat_id,
                silent=True)
            msg_id = msg_o.id
        else:
            return await new_handler.edit(
                "_To save media in reply to a filter, BOTLOG_CHATID must be set._"
            )
    elif new_handler.reply_to_msg_id and not string:
        rep_msg = await new_handler.get_reply_message()
        string = rep_msg.text
    success = "*succesfully add a filter* **{}** `{}`."
    if add_filter(str(new_handler.chat_id), keyword, string, msg_id) is True:
        await new_handler.edit(success.format(keyword, 'here'))
    else:
        await new_handler.edit(success.format(keyword, 'here'))


@register(outgoing=True, pattern=r"^;stop (.*)")
async def remove_a_filter(r_handler):
    """ For .stop command, allows you to remove a filter from a chat. """
    try:
        from userbot.modules.sql_helper.filter_sql import remove_filter
    except AttributeError:
        return await r_handler.edit("running in Non-SQL Mode !")
    filt = r_handler.pattern_match.group(1)
    if not remove_filter(r_handler.chat_id, filt):
        await r_handler.edit("_Filter_ **{}** _is not here_.".format(filt))
    else:
        await r_handler.edit(
            "*succesfully delete filter in* **{}** *here*.".format(filt))


@register(outgoing=True, pattern="^;clearbotfilter (.*)")
async def kick_marie_filter(event):
    """ For .bersihkanbotfilter command, allows you to kick all \
        Marie(or her clones) filters from a chat. """
    bot_type = event.pattern_match.group(1).lower()
    if bot_type not in ["marie", "rose"]:
        return await event.edit("The Bot Is Not Supported Yet!")
    await event.edit("*i will delete all filter*")
    await sleep(3)
    resp = await event.get_reply_message()
    filters = resp.text.split("-")[1:]
    for i in filters:
        if bot_type.lower() == "marie":
            await event.reply("/stop %s" % (i.strip()))
        if bot_type.lower() == "rose":
            i = i.replace('`', '')
            await event.reply("/stop %s" % (i.strip()))
        await sleep(0.3)
    await event.respond(
        "*succesfully delete all filter*")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID, "i delete bot filter in " + str(event.chat_id))


@register(outgoing=True, pattern="^;filters$")
async def filters_active(event):
    """ For .filters command, lists all of the active filters in a chat. """
    try:
        from userbot.modules.sql_helper.filter_sql import get_filters
    except AttributeError:
        return await event.edit("`Running on Non-SQL mode!`")
    transact = "`Tidak Ada Filter Apapun Disini.`"
    filters = get_filters(event.chat_id)
    for filt in filters:
        if transact == "*no filter here*":
            transact = "**☠️ master,list of filter is active here:**\n"
            transact += " ➥ `{}`\n".format(filt.keyword)
        else:
            transact += " ➥ `{}`\n".format(filt.keyword)

    await event.edit(transact)

# ALVIN USERBOT
# @Alvin_UserBot_GROUP
CMD_HELP.update({
    "filters":
    ";filters\
    \nexplanation: list filter Alvin userbot is active in chat.\
    \n\nfilter <keyword> <reply> or repely to a message and type ;filter <keyword>\
    \nexplanation: creat filter in chat.\
    \nThe bot will reply if someone mentions the 'keyword' that was created.\
    \ncan be used on media/sticker/vn/file.\
    \n\nstop <keyword>\
    \nexplanation: to disable a filter or stop filter.\
    \n\n;clearbotfilter` <rose>\
    \nexplanation: delete all bot filter in group (Currently supported bots: Rose.) in chat."
})
