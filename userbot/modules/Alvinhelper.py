""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^;mhelp$")
async def usit(e):
    await e.edit(
        f"**Hi master {DEFAULTUSER} If You Don't Know The Command To Order Me Type** `;help` Or you can ask for help to:\n"
        "\n[Telegram](t.me/Alvin_junior)"
        "\n[Repo](https://github.com/fahrial2310/Alvin-Userbot)"
        "\n[Instagram](https://www.instagram.com/mfahrial2310/)"
        "\n[Github](https://github.com/fahrial2310)"
        "\n[Youtube](https://bit.ly/Alvin_JuniorYT)"
    )
    #don't edit or delete this


@register(outgoing=True, pattern="^;vars$")
async def var(m):
    await m.edit(
        f"**Here List of Vars From {DEFAULTUSER}:**\n"
        "\n[LIST VARS](https://github.com/fahrial2310/Alvin-UserBot/blob/Alvin-UserBot/varshelper.txt)")


CMD_HELP.update({
    "helpers":
    ";mhelp\
\nexplanation: Help For Alvin-Userbot.\
\n;vars\
\nexplanation: To View Multiple List of Vars."
})
