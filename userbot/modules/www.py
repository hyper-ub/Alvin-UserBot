""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

from datetime import datetime

from speedtest import Speedtest
from userbot import CMD_HELP, StartTime, ALIVE_NAME
from userbot.events import register
import time


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["scnd", "Mnt", "Hour", "Day"]

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


@register(outgoing=True, pattern="^;fping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit(".                       /¯ )")
    await pong.edit(".                       /¯ )\n                      /¯  /")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ ")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (\n              \\  ")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**☠️ PING** "
                    f"\n  ➥ %sms \n"
                    f"**☠️ MASTER** "
                    f"\n  ➥ {ALIVE_NAME} \n" % (duration))


@register(outgoing=True, pattern="^;lping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("☠️")
    await pong.edit("__**MASTER☠️**__")
    await pong.edit("__**MASTE☠️R**__")
    await pong.edit("__**MAST☠️ER**__")
    await pong.edit("__**MAS☠️TER**__")
    await pong.edit("__**MA☠️STER**__")
    await pong.edit("__**M☠️ASTER**__")
    await pong.edit("__**☠️MASTER☠️**__")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**☠️ᴘɪɴɢ☠️**\n"
                    f"☠️ **ᴘɪɴɢ:** "
                    f"%sms \n"
                    f"☠️ **ᴏɴʟɪɴᴇ:** "
                    f"{uptime} \n" % (duration))


@register(outgoing=True, pattern="^;xping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("Ping..............")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**☠️ Pong!**\n"
                    f"➠ __Ping:__ "
                    f"%sms \n"
                    f"➠ __Uptime:__ "
                    f"{uptime} \n" % (duration))


@register(outgoing=True, pattern="^;ping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**𖣘**")
    await pong.edit("**𖣘𖣘**")
    await pong.edit("**𖣘𖣘𖣘**")
    await pong.edit("**✦҈͜͡➳ PONG!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**☠️ Alvin Ping ☠️**\n"
                    f"☠️ **Ping:** "
                    f"%sms \n"
                    f"☠️ **Uptime:** "
                    f"{uptime} \n"
                    f"**✦҈͜͡➳ MY MASTER:** {ALIVE_NAME}" % (duration))


@register(outgoing=True, pattern="^;signal$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("checking signal...")
    await pong.edit("**0% ▒▒▒▒▒▒▒▒▒▒**")
    await pong.edit("**20% ██▒▒▒▒▒▒▒▒**")
    await pong.edit("**40% ████▒▒▒▒▒▒**")
    await pong.edit("**60% ██████▒▒▒▒**")
    await pong.edit("**80% ████████▒▒**")
    await pong.edit("**100% ██████████**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"- **M A S T E R** -\n"
                    f"**• SɪGɴAʟ  :** "
                    f"%sms \n"
                    f"**• ᴏNʟIɴE  :** "
                    f"{uptime} \n"
                    f"**• ᴏᴡɴᴇʀ  :** {ALIVE_NAME}" % (duration))


@register(outgoing=True, pattern="^;speed$")
async def speedtst(spd):
    """ For .speed command, use SpeedTest to check server speeds. """
    await spd.edit("Running High Speed Test...🚀")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit("**Test Results:\n**"
                   "❃ **Started at:** "
                   f"`{result['timestamp']}` \n"
                   f" **━━━━━━━━━━━━━━━━━**\n\n"
                   "❃ **Download:** "
                   f"`{speed_convert(result['download'])}` \n"
                   "❃ **Upload:** "
                   f"`{speed_convert(result['upload'])}` \n"
                   "❃ **Ping:** "
                   f"`{result['ping']}` \n"
                   "❃ **ISP:** "
                   f"`{result['client']['isp']}` \n"
                   "❃ **BOT:** `Alvin Userbot`")


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@register(outgoing=True, pattern="^;pong$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    start = datetime.now()
    await pong.edit("☁️")
    await pong.edit("🌥")
    await pong.edit("⛅️")
    await pong.edit("🌤")
    await pong.edit("☀️")
    await pong.edit("☀️Lets☀️Go☀️")
    await pong.edit("☀️")
    await pong.edit("☀️☀️")
    await pong.edit("☀️G☀️")
    await pong.edit("☀️NG☀️")
    await pong.edit("☀️ONG☀️")
    await pong.edit("☀️PONG☀️")
    await pong.edit("☀️Ping☀️Pong☀️")
    end = datetime.now()
    duration = (end - start).seconds / 3
    await pong.edit("☠️ **Ping!**\n%sms" % (duration))

CMD_HELP.update(
    {"ping": ";ping ; ;lping ; ;xping ; ;fping\
    \nPenjelasan: To show ping bot.\
    \n\n;speed\
    \nExplanation: To show speed.\
    \n\n;pong\
    \nExplanation: same as ping command."
     })
CMD_HELP.update(
    {"signal": "**Modules:** Signal\
    \n\n**• command :** ;signal\
    \n  ➥ **explanation :** __to check bot signal__"})
