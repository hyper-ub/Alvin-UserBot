from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\;doujin(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@nHentaiBot"
    await event.edit("_Processing_")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=424466890))
            await bot.send_message(chat, link)
            response = await response
        except YouBlockedUserError:
            await event.reply("_Please unblock @nHentaiBot and try again_")
            return
        if response.text.startswith("**Sorry I couldn't get manga from**"):
            await event.edit("_I think this is not the right link_")
        else:
            await event.delete()
            await bot.send_message(event.chat_id, response.message)

CMD_HELP.update({
    "hentai":
    ";doujin <link / code> \
\nUsage: view nhentai in telegra.ph XD\n"})
