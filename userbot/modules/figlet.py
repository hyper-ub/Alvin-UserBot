import pyfiglet
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\;fg(?: |$)(.*)")
async def figlet(e):
    if e.fwd_from:
        return
    CMD_FIG = {
        "slant": "slant",
        "3D": "3-d",
        "5line": "5lineoblique",
        "alpha": "alphabet",
        "banner": "banner3-D",
        "doh": "doh",
        "iso": "isometric1",
        "letter": "letters",
        "allig": "alligator",
        "dotm": "dotmatrix",
        "bubble": "bubble",
        "bulb": "bulbhead",
        "digi": "digital"}
    input_str = e.pattern_match.group(1)
    if "." in input_str:
        text, cmd = input_str.split(".", maxsplit=1)
    elif input_str is not None:
        cmd = None
        text = input_str
    else:
        await e.edit("`Please add some text to figlet`")
        return
    if cmd is not None:
        try:
            font = CMD_FIG[cmd]
        except KeyError:
            await e.edit("_Invalid selected font._")
            return
        result = pyfiglet.figlet_format(text, font=font)
    else:
        result = pyfiglet.figlet_format(text)
    await e.respond("‌‌‎`{}`".format(result))
    await e.delete()

CMD_HELP.update({
    "figlet":
        ">;fg"
    "\nUsage: Enhance ur text to strip line with anvil."
    "\n\nExample: ;figlet TEXT.STYLE"
    "\nSTYLE LIST: slant, 3D, 5line, alph`, banner, doh, iso, letter, allig, dotm, bubble, bulb, digi"
})
