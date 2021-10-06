import asyncio
from asyncio import create_subprocess_exec as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from platform import python_version, uname
from shutil import which
from os import remove
from telethon import version
from telethon import __version__, version
import platform
import sys
import time
from datetime import datetime
import psutil

from userbot import ALIVE_LOGO, ALIVE_NAME, BOT_VER, ALVIN_TEKS_CUSTOM, CMD_HELP, StartTime, UPSTREAM_REPO_BRANCH, bot
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


modules = CMD_HELP


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["scnd", "Mnt", "hor", "day"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(outgoing=True, pattern=r"^\;spc")
async def psu(event):
    uname = platform.uname()
    softw = "**System Information**\n"
    softw += f"System   : {uname.system}\n"
    softw += f"Release    : {uname.release}\n"
    softw += f"Version    : {uname.version}\n"
    softw += f"machine    : {uname.machine}\n"
    # Boot Time
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    softw += f"time alive: {bt.day}/{bt.month}/{bt.year}  {bt.hour}:{bt.minute}:{bt.second}\n"
    # CPU Cores
    cpuu = "**CPU Information**\n"
    cpuu += "Physical cores   : " + \
        str(psutil.cpu_count(logical=False)) + "\n"
    cpuu += "Total cores      : " + \
        str(psutil.cpu_count(logical=True)) + "\n"
    # CPU frequencies
    cpufreq = psutil.cpu_freq()
    cpuu += f"Max Frequency    : {cpufreq.max:.2f}Mhz\n"
    cpuu += f"Min Frequency    : {cpufreq.min:.2f}Mhz\n"
    cpuu += f"Current Frequency: {cpufreq.current:.2f}Mhz\n\n"
    # CPU usage
    cpuu += "**CPU Usage Per Core**\n"
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        cpuu += f"Core {i}  : {percentage}%\n"
    cpuu += "**Total CPU Usage**\n"
    cpuu += f"all Core: {psutil.cpu_percent()}%\n"
    # RAM Usage
    svmem = psutil.virtual_memory()
    memm = "**usage memory**\n"
    memm += f"Total     : {get_size(svmem.total)}\n"
    memm += f"Available : {get_size(svmem.available)}\n"
    memm += f"Used      : {get_size(svmem.used)}\n"
    memm += f"Percentage: {svmem.percent}%\n"
    # Bandwidth Usage
    bw = "**Bandwith Digunakan**\n"
    bw += f"upload  : {get_size(psutil.net_io_counters().bytes_sent)}\n"
    bw += f"Download: {get_size(psutil.net_io_counters().bytes_recv)}\n"
    help_string = f"{str(softw)}\n"
    help_string += f"{str(cpuu)}\n"
    help_string += f"{str(memm)}\n"
    help_string += f"{str(bw)}\n"
    help_string += "**machine Information**\n"
    help_string += f"Python {sys.version}\n"
    help_string += f"Telethon {__version__}"
    await event.edit(help_string)


def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


@register(outgoing=True, pattern=r"^\;sysd$")
async def sysdetails(sysd):
    if not sysd.text[0].isalpha() and sysd.text[0] not in ("/", "#", "@", "!"):
        try:
            fetch = await asyncrunapp(
                "neofetch",
                "--stdout",
                stdout=asyncPIPE,
                stderr=asyncPIPE,
            )

            stdout, stderr = await fetch.communicate()
            result = str(stdout.decode().strip()) + \
                str(stderr.decode().strip())

            await sysd.edit("`" + result + "`")
        except FileNotFoundError:
            await sysd.edit("Install neofetch first !!")


@register(outgoing=True, pattern=r"^\;botver$")
async def bot_ver(event):
    if event.text[0].isalpha() or event.text[0] in ("/", "#", "@", "!"):
        return
    if which("git") is not None:
        ver = await asyncrunapp(
            "git",
            "describe",
            "--all",
            "--long",
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )
        stdout, stderr = await ver.communicate()
        verout = str(stdout.decode().strip()) + str(stderr.decode().strip())

        rev = await asyncrunapp(
            "git",
            "rev-list",
            "--all",
            "--count",
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )
        stdout, stderr = await rev.communicate()
        revout = str(stdout.decode().strip()) + str(stderr.decode().strip())

        await event.edit(
            "**☛**Alvin-UserBot version:** \n "
            f"{verout}"
            "\n**☛**Revisi:**\n "
            f"{revout}"
        )
    else:
        await event.edit(
            "Too bad you don't have git, you're Running a Bot - 'v1.beta.4'!"
        )


@register(outgoing=True, pattern=r"^\;pip(?: |$)(.*)")
async def pipcheck(pip):
    if pip.text[0].isalpha() or pip.text[0] in ("/", "#", "@", "!"):
        return
    pipmodule = pip.pattern_match.group(1)
    if pipmodule:
        await pip.edit("finding...")
        pipc = await asyncrunapp(
            "pip3",
            "search",
            pipmodule,
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )

        stdout, stderr = await pipc.communicate()
        pipout = str(stdout.decode().strip()) + str(stderr.decode().strip())

        if pipout:
            if len(pipout) > 4096:
                await pip.edit("Output Too Large, Sent As File")
                file = open("output.txt", "w+")
                file.write(pipout)
                file.close()
                await pip.client.send_file(
                    pip.chat_id,
                    "output.txt",
                    reply_to=pip.id,
                )
                remove("output.txt")
                return
            await pip.edit(
                "**Query: **\n`"
                f"pip3 search {pipmodule}"
                "`\n**Result: **\n`"
                f"{pipout}"
                "`"
            )
        else:
            await pip.edit(
                "**Query: **\n"
                f"pip3 search {pipmodule}"
                "\n**Result: **\nNo Result Returned/False"
            )
    else:
        await pip.edit("Use ;help pip To See Examples")


@register(outgoing=True, pattern=r"^\;(?:master|alvin|skull)\s?(.)?")
async def amireallyalive(alive):
    user = await bot.get_me()
    await get_readable_time((time.time() - StartTime))
    await alive.edit("I'M ALIVE!")
    await alive.edit("☠️")
    output = (
        f" **┗┓ALVIN USERBOT┏┛** \n"
        f"\n__**{ALVIN_TEKS_CUSTOM}**__\n"
        f"**━━━━━━━━━━━━━━━━**\n"
        f"**☠️ Master** \n"
        f"  {DEFAULTUSER} \n"
        f"**☠️ Username** \n"
        f"  @{user.username} \n"
        f"┏━━━━━━━━━━━━━━━━\n"
        f"┣[• Telethon :Ver {version.__version__} \n"
        f"┣[• Python   :Ver {python_version()} \n"
        f"┣[• Bot Ver  :{BOT_VER} \n"
        f"┣[• Modules  :{len(modules)} Modules \n"
        f"┗━━━━━━━━━━━━━━━━")
    if ALIVE_LOGO:
        try:
            logo = ALIVE_LOGO
            await alive.delete()
            msg = await bot.send_file(alive.chat_id, logo, caption=output)
            await asyncio.sleep(200)
            await msg.delete()
        except BaseException:
            await alive.edit(
                output + "\n\n *The provided logo is invalid."
                "\nMake sure the link is directed to the logo picture"
            )
            await asyncio.sleep(100)
            await alive.delete()
    else:
        await alive.edit(output)
        await asyncio.sleep(100)
        await alive.delete()


@register(outgoing=True, pattern=r"^\;(?:xalive|xon)\s?(.)?")
async def amireallyalive(alive):
    user = await bot.get_me()
    await get_readable_time((time.time() - StartTime))
    output = (
        f"**╔═════❙۩☠️۩❙═════╗**\n"
        f" **☠️ ALVIN USERBOT ☠️** \n\n"
        f"☠️ **Master**     \n    {DEFAULTUSER} \n"
        f"☠️ **Username** \n    @{user.username} \n"
        f"☠️ **Telethon** \n    Version {version.__version__} \n"
        f"☠️ **Python**   \n    Version {python_version()} \n"
        f"☠️ **Bot Version**\n    {BOT_VER}\n"
        f"☠️ **Module**    \n    {len(modules)} \n\n"
        f"☠️ **Repo Userbot:** [Alvin-Userbot](https://github.com/fahrial2310/Alvin-Userbot)\n☠️ **Group Userbot: **[press](t.me/Alvin_Userbot_Group)\n☠️ **Owner:** [Alvin Junior](t.me/Alvin_junior)\n"
        f"**╚═════❙۩☠️۩❙═════╝**")
    if ALIVE_LOGO:
        try:
            logo = ALIVE_LOGO
            await alive.delete()
            msg = await bot.send_file(alive.chat_id, logo, caption=output)
            await asyncio.sleep(200)
            await msg.delete()
        except BaseException:
            await alive.edit(
                output + "\n\n *`The provided logo is invalid."
                "\nMake sure the link is directed to the logo picture`"
            )
            await asyncio.sleep(100)
            await alive.delete()
    else:
        await alive.edit(output)
        await asyncio.sleep(100)
        await alive.delete()


@register(outgoing=True, pattern=r"^\;(?:alive|on)\s?(.)?")
async def amireallyalive(alive):
    user = await bot.get_me()
    await get_readable_time((time.time() - StartTime))
    await alive.edit("I'M ALIVE!")
    await alive.edit("☠️")
    output = (
        f"**☠️ Alvin UserBot ☠️** \n\n"
        f"┏━━━━━━━━━━━━━━━━\n"
        f"┣|☠️ Master     :{DEFAULTUSER} \n"
        f"┣|☠️ Username :@{user.username} \n"
        f"┣|☠️ Telethon :Ver {version.__version__} \n"
        f"┣|☠️ Python   :Ver {python_version()} \n"
        f"┣|☠️ Branch   :{UPSTREAM_REPO_BRANCH} \n"
        f"┣|☠️ Bot Ver  :{BOT_VER} \n"
        f"┣|☠️ Modules  :{len(modules)} Modules \n"
        f"┗━━━━━━━━━━━━━━━━\n\n"
        f"☠️[Repo](https://github.com/fahrial2310/Alvin-Userbot) | [Group Support](t.me/Alvin_Userbot_Group) | [Owner](t.me/Alvin_junior)☠️")
    if ALIVE_LOGO:
        try:
            logo = ALIVE_LOGO
            await alive.delete()
            msg = await bot.send_file(alive.chat_id, logo, caption=output)
            await asyncio.sleep(500)
            await msg.delete()
        except BaseException:
            await alive.edit(
                output + "\n\n *Invalid Logo Provided."
                "\nMake sure the link you are using is valid"
            )
            await asyncio.sleep(100)
            await alive.delete()
    else:
        await alive.edit(output)
        await asyncio.sleep(100)
        await alive.delete()


@register(outgoing=True, pattern="^;aliveu")
async def amireallyaliveuser(username):
    """ For .aliveu command, change the username in the .alive command. """
    message = username.text
    output = ";aliveu [username] cannot empty"
    if not (message == ".aliveu" or message[7:8] != " "):
        newuser = message[8:]
        global DEFAULTUSER
        DEFAULTUSER = newuser
        output = "Successfully changed user on ;alive to " + newuser + "!"
    await username.edit("`" f"{output}" "`")


@register(outgoing=True, pattern=r"^\;resetalive$")
async def amireallyalivereset(ureset):
    global DEFAULTUSER
    DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
    await ureset.edit("`" "Successfully reset Alive user!" "`")


CMD_HELP.update({"sysd": ";sysd\
    \nDescription: Displaying system information using neofetch.\
     \n\n;spc\
     \nExplanation: Display system specifications.\
     \n\n;db\
     \nExplanation: Displays database info."})
CMD_HELP.update({"botver": ";botver\
     \nExplanation: Displays the userbot version."})

CMD_HELP.update({"pip": ";pip <module(s)>\
     \nExplanation: Perform a pip module search."})

CMD_HELP.update({"alive": ";alive | ;on\
     \nExplanation: Type ;alive/;on to see if your bot is working or not.\
     \n\n;alive <text>\
     \nExplanation: Change 'user' to any text you want.\
     \n\n;resetalive\
     \nExplanation: Reset user to default.\
     \n\n;master | ;alvin | ;skull.\
     \nexplanation: alive"})
