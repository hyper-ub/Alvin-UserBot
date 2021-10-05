from telethon.tl.functions.messages import EditChatDefaultBannedRightsRequest
from telethon.tl.types import ChatBannedRights

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\;lock ?(.*)")
async def locks(event):
    input_str = event.pattern_match.group(1).lower()
    peer_id = event.chat_id
    msg = None
    media = None
    sticker = None
    gif = None
    gamee = None
    ainline = None
    gpoll = None
    adduser = None
    cpin = None
    changeinfo = None
    if input_str == "msg":
        msg = True
        what = "Pesan"
    elif input_str == "media":
        media = True
        what = "Media"
    elif input_str == "sticker":
        sticker = True
        what = "Sticker"
    elif input_str == "gif":
        gif = True
        what = "GIF"
    elif input_str == "game":
        gamee = True
        what = "Game"
    elif input_str == "inline":
        ainline = True
        what = "Inline Bot"
    elif input_str == "poll":
        gpoll = True
        what = "Poll"
    elif input_str == "invite":
        adduser = True
        what = "Invite"
    elif input_str == "pin":
        cpin = True
        what = "Pin"
    elif input_str == "info":
        changeinfo = True
        what = "Info"
    elif input_str == "all":
        msg = True
        media = True
        sticker = True
        gif = True
        gamee = True
        ainline = True
        gpoll = True
        adduser = True
        cpin = True
        changeinfo = True
        what = "everyone"
    else:
        if not input_str:
            await event.edit("_sorry my master,what should i lock??? ヅ_`")
            return
        else:
            await event.edit(f"*master, Type You Want To Lock Is Invalid* `{input_str}`")
            return

    lock_rights = ChatBannedRights(
        until_date=None,
        send_messages=msg,
        send_media=media,
        send_stickers=sticker,
        send_gifs=gif,
        send_games=gamee,
        send_inline=ainline,
        send_polls=gpoll,
        invite_users=adduser,
        pin_messages=cpin,
        change_info=changeinfo,
    )
    try:
        await event.client(
            EditChatDefaultBannedRightsRequest(peer=peer_id,
                                               banned_rights=lock_rights))
        await event.edit(f"*master is lock {what} for this chat ヅ*")
    except BaseException as e:
        await event.edit(
            f"_Does the Lord Have Permission to Do That Here?_\n**error:** {str(e)}")
        return


@register(outgoing=True, pattern=r"^;unlock ?(.*)")
async def rem_locks(event):
    input_str = event.pattern_match.group(1).lower()
    peer_id = event.chat_id
    msg = None
    media = None
    sticker = None
    gif = None
    gamee = None
    ainline = None
    gpoll = None
    adduser = None
    cpin = None
    changeinfo = None
    if input_str == "msg":
        msg = False
        what = "Pesan"
    elif input_str == "media":
        media = False
        what = "Media"
    elif input_str == "sticker":
        sticker = False
        what = "Sticker"
    elif input_str == "gif":
        gif = False
        what = "GIF"
    elif input_str == "game":
        gamee = False
        what = "Game"
    elif input_str == "inline":
        ainline = False
        what = "Inline"
    elif input_str == "poll":
        gpoll = False
        what = "Poll"
    elif input_str == "invite":
        adduser = False
        what = "Invite"
    elif input_str == "pin":
        cpin = False
        what = "Pin"
    elif input_str == "info":
        changeinfo = False
        what = "Info"
    elif input_str == "all":
        msg = False
        media = False
        sticker = False
        gif = False
        gamee = False
        ainline = False
        gpoll = False
        adduser = False
        cpin = False
        changeinfo = False
        what = "everyone"
    else:
        if not input_str:
            await event.edit("_what should i unlock master?? ヅ_")
            return
        else:
            await event.edit(f"*mymaster, Type You Want To unlock Is Invalid* `{input_str}`")
            return

    unlock_rights = ChatBannedRights(
        until_date=None,
        send_messages=msg,
        send_media=media,
        send_stickers=sticker,
        send_gifs=gif,
        send_games=gamee,
        send_inline=ainline,
        send_polls=gpoll,
        invite_users=adduser,
        pin_messages=cpin,
        change_info=changeinfo,
    )
    try:
        await event.client(
            EditChatDefaultBannedRightsRequest(peer=peer_id,
                                               banned_rights=unlock_rights))
        await event.edit(f"master is unlock {what} for this chat ヅ")
    except BaseException as e:
        await event.edit(
            f"*Does the Lord Have Permission to Do That Here?*\n**error:** {str(e)}")
        return


CMD_HELP.update({
    "locks":
    ";lock <all or type> or ;unlock <all atau type>\
\nUsage: Allows you to lock or unlock, several types of messages in chat.\
\n[You must be a group admin to use commands!]\
\n\nThe types of messages that can be locked or unlocked are: \
\n`all, msg, media, sticker, gif, game, inline, poll, invite, pin, info`\n**example:** ;lock msg or ;unlock msg"
})
