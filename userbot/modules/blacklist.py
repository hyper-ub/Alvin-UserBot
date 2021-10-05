import io
import re

import userbot.modules.sql_helper.blacklist_sql as sql
from userbot import CMD_HELP
from userbot.events import register


@register(incoming=True, disable_edited=True, disable_errors=True)
async def on_new_message(event):
    # TODO: exempt admins from locks
    name = event.raw_text
    snips = sql.get_chat_blacklist(event.chat_id)
    for snip in snips:
        pattern = r"( |^|[^\w])" + re.escape(snip) + r"( |$|[^\w])"
        if re.search(pattern, name, flags=re.IGNORECASE):
            try:
                await event.delete()
            except Exception:
                await event.reply("*master, you don't have permission to delete message here*")
                await sleep(1)
                await reply.delete()
                sql.rm_from_blacklist(event.chat_id, snip.lower())
            break


@register(outgoing=True, pattern=r"^\;addblacklist(?: |$)(.*)")
async def on_add_black_list(addbl):
    text = addbl.pattern_match.group(1)
    to_blacklist = list(
        {trigger.strip() for trigger in text.split("\n") if trigger.strip()}
    )

    for trigger in to_blacklist:
        sql.add_to_blacklist(addbl.chat_id, trigger.lower())
    await addbl.edit(
        "add text **{}** to Blacklist for this chat".format(text)
    )


@register(outgoing=True, pattern=r"^\;blacklist(?: |$)(.*)")
async def on_view_blacklist(listbl):
    all_blacklisted = sql.get_chat_blacklist(listbl.chat_id)
    OUT_STR = "Blacklists in the Current Chat:\n"
    if len(all_blacklisted) > 0:
        for trigger in all_blacklisted:
            OUT_STR += f"`{trigger}`\n"
    else:
        OUT_STR = "*no blacklist in this chat`"
    if len(OUT_STR) > 4096:
        with io.BytesIO(str.encode(OUT_STR)) as out_file:
            out_file.name = "blacklist.text"
            await listbl.client.send_file(
                listbl.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption="Blacklist in this chat",
                reply_to=listbl,
            )
            await listbl.delete()
    else:
        await listbl.edit(OUT_STR)


@register(outgoing=True, pattern=r"^\.rmblacklist(?: |$)(.*)")
async def on_delete_blacklist(rmbl):
    text = rmbl.pattern_match.group(1)
    to_unblacklist = list(
        {trigger.strip() for trigger in text.split("\n") if trigger.strip()}
    )

    successful = 0
    for trigger in to_unblacklist:
        if sql.rm_from_blacklist(rmbl.chat_id, trigger.lower()):
            successful += 1
    if not successful:
        await rmbl.edit("master, **{}** not in the blacklist".format(text))
    else:
        await rmbl.edit("_succesfully delete_ **{}** _in blacklist_".format(text))


CMD_HELP.update({"blacklist": ">;blacklist"
                 "\nUsage: list of blacklist are active in this chat."
                 "\n\n>;addblacklist <text>"
                 "\nUsage: add message to blacklist."
                 "\nmaster,bot will automatically remove 'word blacklist'."
                 "\n\n>;rmblacklist <text>"
                 "\nUsage: delete blacklist text."})
