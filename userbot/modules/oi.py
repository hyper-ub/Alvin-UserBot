from time import sleep
from userbot.events import register


@register(outgoing=True, pattern='^;alvin(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("Hi my name is..._unknown identity_")
    sleep(3)
    await typew.edit("_unknown years old_")
    sleep(1)
    await typew.edit("_unknown place_,error, master identity not found:)")
    #dont edit or remove


@register(outgoing=True, pattern='^;sayang(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("i'm wanna say")
    sleep(3)
    await typew.edit("I Love You")
    sleep(1)
    await typew.edit("I LOVE YOU 💞")


@register(outgoing=True, pattern='^;semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("Whatever Happens")
    sleep(3)
    await typew.edit("Keep Breathing")
    sleep(1)
    await typew.edit("And Always Grateful")
