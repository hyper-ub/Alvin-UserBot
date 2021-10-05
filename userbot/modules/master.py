from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^;sadboy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("First of all you are beautiful`")
    sleep(2)
    await typew.edit("`Both of you are cute`")
    sleep(1)
    await typew.edit("`And the last one is you are not my soul mate`")

@register(outgoing=True, pattern='^;excuseme(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**excuse me**")


@register(outgoing=True, pattern='^;monitoring(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**i still monitoring you**")
    
CMD_HELP.update({
    "master":
    ";master\
    \nUsage: alive bot.\
    \n\n;sadboy\
    \nUsage: hiks\
    \n\n;excuseme | ;monitoring\
    \nUsage: try it."
})
