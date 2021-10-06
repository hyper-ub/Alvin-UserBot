""" Alvin Userbot help command """
import asyncio
from userbot import CMD_HELP
from userbot.events import register

modules = CMD_HELP

@register(outgoing=True, pattern="^;help(?: |$)(.*)")
async def help(Alvin):
    """ For .help command,"""
    args = Alvin.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await Alvin.edit(str(CMD_HELP[args]))
        else:
            await Alvin.edit("**sorry master,i don't have that command,type ;help ツ**")
            await asyncio.sleep(200)
            await Alvin.delete()
    else:
        await Alvin.edit("☠️")
        await Alvin.edit("**☠️MODULES☠️:**\n"
                        "`admin` | `adzan` | `afk` | `bored` | `vip` | `animation`|  `android` | `anime` | `anti_spambot` | `aria` | `ascii`\n\n"
                        "`blacklist` | `carbon`  | `chat` | `mutechat` | `corona` | `creating` | `deepfry` | `emogames`\n\n"
                        "`eval` | `exec` | `term` | `fgban` | `federation` | `figlet` | `tags` | `filters` | `gban` | `gcast` | `googledrive` | `gcommit` | `github`\n\n"
                        "`glitch` | `gps` | `hash` | `base64` | `hentai` | `heroku` | `id` | `memeimage` | `power`\n\n"
                        "`lastfm` | `locks` | `master` | `aeshtetic` | `detect` | `mastergame` | `helpers` | `hazmat`\n\n"
                        "`instagram` | `impostor` | `memes` | `misc` | `app` | `undelete` | `grab` | `clone`\n\n"
                        "`randomprofil` | `song` | `tiny` | `tempmail` | `tiktok` | `wordcloud`\n\n" 
                        "`lyrics` | `mega` | `justforfun` | `memify` | `mentions` | `purge` | `purgeme` | `del` | `edit`\n\n"
                        "`sd` | `random` | `sleep` | `shutdown` | `repo`  |`readme` | `repeat` | `restart`\n\n"
                        "`raw` | `nekobot` | `notes` | `off` | `phreaker` | `pm` | `profil` | `quotly`|  `rastick` | `resi` | `reverse` | `salam` | `sangmata`\n\n"
                        "`santet` | `image_search` | `currency` | `google` | `wiki`| `ud` | `tts` | `translate`| `youtube` | `rip`\n\n"
                        "`removebg` | `ocr` | `qrcode` | `barcode` | `paste` | `getpaste` | `nekobin` | `direct` | `screenshot` | `sed` | `snips` | `spammer` | `spotifynow` | `ssvideo`\n\n"
                        "`stickers` | `stickers2` | `sysd` | `botver` | `pip` | `alive` | `tag_all` | `telegraph` | `timedate` | `torrent`\n\n" 
                        "`transform` | `updater` |`downloader` | `getid` | `waifu` | `wallpaper` | `weather`\n\n"
                        "`webupload` | `welcome`|  `info` | `ping` | `signal` | `xiaomi` | `zipfile`")
        await Alvin.reply("\n**HOW TO USE????,** **EXAMPLE:**\n**TYPE** `;help afk` **FOR INFORMATION MODULES**GO TO**GROUP SUPPORT:** [CLICK HERE TO GO](t.me/Alvin_Userbot_Group)")
        await asyncio.sleep(1000)
        await Alvin.delete()
