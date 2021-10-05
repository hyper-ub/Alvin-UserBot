# ALVIN USERBOT
from asyncio import sleep

from requests import get
from telethon.events import ChatAction
from telethon.tl.types import ChannelParticipantsAdmins, Message

from userbot import (
    ANTI_SPAMBOT,
    ANTI_SPAMBOT_SHOUT,
    BOTLOG,
    BOTLOG_CHATID,
    CMD_HELP,
    bot,
)

# ALVIN USERBOT

@bot.on(ChatAction)
async def ANTI_SPAMBOTS(welcm):
    """block newly joined users if they match the spammer checking algorithm."""
    try:
        if not ANTI_SPAMBOT:
            return
        if welcm.user_joined or welcm.user_added:
            adder = None
            ignore = False
            users = None

            if welcm.user_added:
                ignore = False
                try:
                    adder = welcm.action_message.from_id
                except AttributeError:
                    return

            async for admin in bot.iter_participants(
                welcm.chat_id, filter=ChannelParticipantsAdmins
            ):
                if admin.id == adder:
                    ignore = True
                    break

            if ignore:
                return

            elif welcm.user_joined:
                users_list = hasattr(welcm.action_message.action, "users")
                if users_list:
                    users = welcm.action_message.action.users
                else:
                    users = [welcm.action_message.from_id]

            await sleep(5)
            spambot = False

            if not users:
                return

            for user_id in users:
                async for message in bot.iter_messages(
                    welcm.chat_id, from_user=user_id
                ):

                    correct_type = isinstance(message, Message)
                    if not message or not correct_type:
                        break

                    join_time = welcm.action_message.date
                    message_date = message.date

                    if message_date < join_time:
                        continue  # The message was sent before the user joined, thus ignore it

                    check_user = await welcm.client.get_entity(user_id)

                    # DEBUGGING. LEAVING IT HERE FOR SOME TIME ###
                    print(f"user joining: {check_user.first_name} [ID: {check_user.id}]")
                    print(f"Chat: {welcm.chat.title}")
                    print(f"time: {join_time}")
                    print(f"message send: {message.text}\n\n[time: {message_date}]")
                    ##############################################

                    try:
                        # https://t.me/combotnews/283
                        cas_url = f"https://api.cas.chat/check?user_id={check_user.id}"
                        r = get(cas_url, timeout=3)
                        data = r.json()
                    except BaseException:
                        print(
                            "CAS check failed, revert to legacy anti_spambot behavior."
                        )
                        data = None

                    if data and data["ok"]:
                        reason = f"[Banned by Combot Anti Spam](https://cas.chat/query?u={check_user.id})"
                        spambot = True
                    elif "t.cn/" in message.text:
                        reason = "Match on `t.cn` URLs"
                        spambot = True
                    elif "t.me/joinchat" in message.text:
                        reason = "Potential Promotion Message"
                        spambot = True
                    elif message.fwd_from:
                        reason = "Forwarded Message"
                        spambot = True
                    elif "?start=" in message.text:
                        reason = "Telegram bot `start` link"
                        spambot = True
                    elif "bit.ly/" in message.text:
                        reason = "Match on `bit.ly` URLs"
                        spambot = True
                    else:
                        if check_user.first_name in (
                            "Bitmex",
                            "Promotion",
                            "Information",
                            "Dex",
                            "Announcements",
                            "Info",
                        ):
                            if users.last_name == "Bot":
                                reason = "Known spambot"
                                spambot = True

                    if spambot:
                        print(f"Potensi Pesan Spam: {message.text}")
                        await message.delete()
                        break

                    continue  # Check the next messsage

            if spambot:
                chat = await welcm.get_chat()
                admin = chat.admin_rights
                creator = chat.creator
                if not admin and not creator:
                    if ANTI_SPAMBOT_SHOUT:
                        await welcm.reply(
                            "@admins\n"
                            "*ANTI SPAMBOT DETECTOR!\n"
                            "THIS USER MATCHES MY ALGORITHM AS SPAMBOT!*"
                            f"ALASAN: {reason}"
                        )
                        kicked = False
                        reported = True
                else:
                    try:

                        await welcm.reply(
                            "*Potential spambots detected.!!*\n"
                            f"*REASON   :* {reason}\n"
                            "Get him out for now.\n"
                            f"*USERS :* [{check_user.first_name}](tg://user?id={check_user.id})"
                        )

                        await welcm.client.kick_participant(
                            welcm.chat_id, check_user.id
                        )
                        kicked = True
                        reported = False

                    except BaseException:
                        if ANTI_SPAMBOT_SHOUT:
                            await welcm.reply(
                                "@admins\n"
                                "*ANTI SPAMBOT DETECTOR!\n"
                                "THIS USER MATCHES MY ALGORITHM AS SPAMBOT!*"
                                f"ALASAN: {reason}"
                            )
                            kicked = False
                            reported = True

                if BOTLOG:
                    if kicked or reported:
                        await welcm.client.send_message(
                            BOTLOG_CHATID,
                            "#ANTI_SPAMBOT REPORT\n"
                            f"user   : [{users.first_name}](tg://user?id={check_user.id})\n"
                            f"ID user : `{check_user.id}`\n"
                            f"user    : {welcm.chat.title}\n"
                            f"ID Messages    : `{welcm.chat_id}`\n"
                            f"REASON      : {reason}\n"
                            f"MESSAGE       :\n\n{message.text}",
                        )
    except ValueError:
        pass

# ALVIN USERBOT
# ALVIN GANTENG

CMD_HELP.update(
    {
        "anti_spambot": "If enabled in config.env or env var,\
         \nthis module will disallow (or notify group admins about)\
         \nspam if it matches the user's bot anti-spam algorithm."
    }
)
