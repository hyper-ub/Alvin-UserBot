from userbot.events import register
from userbot import CMD_HELP, bot

@register(outgoing=True, pattern="^;gcast (.*)")
async def gcast(event):
    xx = event.pattern_match.group(1)
    if not xx:
        return await event.edit("_master,please give some message_")
    tt = event.text
    msg = tt[6:]
    kk = await event.edit("*send message globally...*")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(f"**succesfully send message to** `{done}` **Group, failed send message to** `{er}` **Group**")

# Alvin Ganteng
CMD_HELP.update(
    {
        "gcast": ";gcast <messages>\
    \nexplanation: Global Broadcast send a message to the Entire Group you Entered."
    })
