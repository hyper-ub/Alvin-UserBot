import random

from telethon.errors import ChatSendInlineForbiddenError, ChatSendStickersForbiddenError

from userbot.events import register
from userbot import CMD_HELP, bot

@register(outgoing=True, pattern=r"^\;frog (.*)")
async def honkasays(event):
    wai = await event.edit("_processing!!!_")
    text = event.pattern_match.group(1)
    if not text:
        return await event.edit("give me some text, example ;prog test")
    try:
        if not text.endswith("."):
            text = text + "."
        if len(text)<=9:
            results = await bot.inline_query("honka_says_bot", text)
            await results[2].click(
                event.chat_id,
                silent=True,
                hide_via=True,
            )
        elif len(text)>=14:
            results = await bot.inline_query("honka_says_bot", text)
            await results[0].click(
                event.chat_id,
                silent=True,
                hide_via=True,
            )
        else:
            results = await bot.inline_query("honka_says_bot", text)
            await results[1].click(
                event.chat_id,
                silent=True,
                hide_via=True,
            )
        await event.delete()
    except ChatSendInlineForbiddenError:
        await event.edit("master! SI can't use inline things here...")
    except ChatSendStickersForbiddenError:
        await event.edit("sorry master,i can't send sticker here !!")


CMD_HELP.update({"frog": "**Modules:** __Frog__\n\n**command:** ;frog <text>\
    \n**explanation:** send a animation like a frog."})
