from sqlalchemy.exc import IntegrityError

from userbot import CMD_HELP, bot
from userbot.events import register


@register(outgoing=True, disable_edited=True, pattern=r"^\;fban(?: |$)(.*)")
async def fban(event):
    """Bans a user from connected federations."""
    try:
        from userbot.modules.sql_helper.fban_sql import get_flist
    except IntegrityError:
        return await event.edit("**running in NON-SQL mode!**")

    if event.is_reply:
        reply_msg = await event.get_reply_message()
        fban_id = reply_msg.from_id
        reason = event.pattern_match.group(1)
        user_link = f"[{fban_id}](tg://user?id={fban_id})"
    else:
        pattern = str(event.pattern_match.group(1)).split()
        fban_id = pattern[0]
        reason = " ".join(pattern[1:])
        user_link = fban_id

    self_user = await event.client.get_me()

    if fban_id == self_user.id or fban_id == "@" + self_user.username:
        return await event.edit(
            "**Error: This action was prevented by the FeRuBoT protocol.**"
        )

    if len((fed_list := get_flist())) == 0:
        return await event.edit("**Anda belum terhubung ke federasi mana pun!**")

    await event.edit(f"**Fbanning** {user_link}...")
    failed = []
    total = int(0)

    for i in fed_list:
        total += 1
        chat = int(i.chat_id)
        try:
            async with bot.conversation(chat) as conv:
                await conv.send_message(f"/fban {user_link} {reason}")
                reply = await conv.get_response()
                await bot.send_read_acknowledge(
                    conv.chat_id, message=reply, clear_mentions=True
                )

                if (
                    ("New FedBan" not in reply.text)
                    and ("Starting a federation ban" not in reply.text)
                    and ("Start a federation ban" not in reply.text)
                    and ("FedBan reason updated" not in reply.text)
                ):
                    failed.append(i.fed_name)
        except BaseException:
            failed.append(i.fed_name)

    reason = reason if reason else "Not specified."

    if failed:
        status = f"Failed to do fban on {len(failed)}/{total} federation.\n"
        for i in failed:
            status += "• " + i + "\n"
    else:
        status = f"succesfully fbanned this user in {total} federation."

    await event.edit(
        f"**Fbanned **{user_link}!\n**reason:** {reason}\n**Status:** {status}"
    )


@register(outgoing=True, disable_edited=True, pattern=r"^\;unfban(?: |$)(.*)")
async def unfban(event):
    """Unbans a user from connected federations."""
    try:
        from userbot.modules.sql_helper.fban_sql import get_flist
    except IntegrityError:
        return await event.edit("**running in Non-SQL mode !**")

    if event.is_reply:
        reply_msg = await event.get_reply_message()
        unfban_id = reply_msg.from_id
        reason = event.pattern_match.group(1)
        user_link = f"[{unfban_id}](tg://user?id={unfban_id})"
    else:
        pattern = str(event.pattern_match.group(1)).split()
        unfban_id = pattern[0]
        reason = " ".join(pattern[1:])
        user_link = unfban_id

    self_user = await event.client.get_me()

    if unfban_id == self_user.id or unfban_id == "@" + self_user.username:
        return await event.edit("**wait,that is ilegal**")

    if len((fed_list := get_flist())) == 0:
        return await event.edit("**You are not connected to any federation yet!**")

    await event.edit(f"**Un-fbanning **{user_link}**...**")
    failed = []
    total = int(0)

    for i in fed_list:
        total += 1
        chat = int(i.chat_id)
        try:
            async with bot.conversation(chat) as conv:
                await conv.send_message(f"/unfban {user_link} {reason}")
                reply = await conv.get_response()
                await bot.send_read_acknowledge(
                    conv.chat_id, message=reply, clear_mentions=True
                )

                if (
                    ("New un-FedBan" not in reply.text)
                    and ("I'll give" not in reply.text)
                    and ("Un-FedBan" not in reply.text)
                ):
                    failed.append(i.fed_name)
        except BaseException:
            failed.append(i.fed_name)

    reason = reason if reason else "Not specified."

    if failed:
        status = f"Filed to cancel fban on {len(failed)}/{total} federation.\n"
        for i in failed:
            status += "• " + i + "\n"
    else:
        status = f"succesfully un-fbanned this user in {total} federation."

    reason = reason if reason else "not found."
    await event.edit(
        f"**Un-fbanned** {user_link}!\n**reason:** {reason}\n**Status:** {status}"
    )


@register(outgoing=True, pattern=r"^\;addfeed *(.*)")
async def addf(event):
    """Adds current chat to connected federations."""
    try:
        from userbot.modules.sql_helper.fban_sql import add_flist
    except IntegrityError:
        return await event.edit("**running in Non-SQL mode !**")

    if not (fed_name := event.pattern_match.group(1)):
        return await event.edit("**Give a name to connect to this group!**")

    try:
        add_flist(event.chat_id, fed_name)
    except IntegrityError:
        return await event.edit(
            "**This group is connected to the federation list.**"
        )

    await event.edit("**Add this group to federation list!**")


@register(outgoing=True, pattern=r"^\;delfeed$")
async def delf(event):
    """Removes current chat from connected federations."""
    try:
        from userbot.modules.sql_helper.fban_sql import del_flist
    except IntegrityError:
        return await event.edit("**running in Non-SQL mode !**")

    del_flist(event.chat_id)
    await event.edit("**delete this group from federation list!**")


@register(outgoing=True, pattern=r"^\;listfeed$")
async def listf(event):
    """List all connected federations."""
    try:
        from userbot.modules.sql_helper.fban_sql import get_flist
    except IntegrityError:
        return await event.edit("**running in Non-SQL mode !**")

    if len((fed_list := get_flist())) == 0:
        return await event.edit("**You are not connected to any federation yet!**")

    msg = "**connect federations:**\n\n"

    for i in fed_list:
        msg += "• " + str(i.fed_name) + "\n"

    await event.edit(msg)


@register(outgoing=True, disable_edited=True, pattern=r"^\;clearfeed$")
async def delf(event):
    """Removes all chats from connected federations."""
    try:
        from userbot.modules.sql_helper.fban_sql import del_flist_all
    except IntegrityError:
        return await event.edit("**running in Non-SQL mode !**")

    del_flist_all()
    await event.edit("**Disconnected from all connected federations!**")


CMD_HELP.update(
    {
        "federation": ";fban <id/username> <reason>"
        "\nexplanation: Ban users from connected federations."
        "\nYou can reply to the user you want to fban or manually enter username/id."
        "\n\n;unfban <id/username> <reason>"
        "\nexplanation: same like fban but unfban user"
        "\n\n;addf <name>"
        "\nexplanation: Add current group and save it as <name> in connected federations."
        "\naddin one group is enough for one federation."
        "\n\n;delf"
        "\nexplanation: delete group from federations list."
        "\n\n;listf"
        "\nexplanation:Lists all connected federations with the specified name."
    }
)
