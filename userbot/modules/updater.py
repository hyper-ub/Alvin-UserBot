"""
This module updates the userbot based on upstream revision
"""

from os import remove, execle, path, environ
import asyncio
import sys

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError

from userbot import (
    BOTLOG,
    BOTLOG_CHATID,
    CMD_HELP,
    HEROKU_API_KEY,
    HEROKU_APP_NAME,
    UPSTREAM_REPO_URL,
    UPSTREAM_REPO_BRANCH)
from userbot.events import register

requirements_path = path.join(
    path.dirname(path.dirname(path.dirname(__file__))), 'requirements.txt')


async def gen_chlog(repo, diff):
    ch_log = ''
    d_form = "%d/%m/%y"
    for c in repo.iter_commits(diff):
        ch_log += f'•[{c.committed_datetime.strftime(d_form)}]: {c.summary} <{c.author}>\n'
    return ch_log


async def update_requirements():
    reqs = str(requirements_path)
    try:
        process = await asyncio.create_subprocess_shell(
            ' '.join([sys.executable, "-m", "pip", "install", "-r", reqs]),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE)
        await process.communicate()
        return process.returncode
    except Exception as e:
        return repr(e)


async def deploy(event, repo, ups_rem, ac_br, txt):
    if HEROKU_API_KEY is not None:
        import heroku3
        heroku = heroku3.from_key(HEROKU_API_KEY)
        heroku_app = None
        heroku_applications = heroku.apps()
        if HEROKU_APP_NAME is None:
            await event.edit(
                '[HEROKU]: Please Set Up Variable **HEROKU_APP_NAME** '
                ' to be able to deploy the latest changes from Alvin Userbot.'
            )
            repo.__del__()
            return
        for app in heroku_applications:
            if app.name == HEROKU_APP_NAME:
                heroku_app = app
                break
        if heroku_app is None:
            await event.edit(
                f'{txt}\nInvalid Heroku credentials for deploying Alvin Userbot dyno.'
            )
            return repo.__del__()
        await event.edit('[HEROKU]:'
                         '\nDyno Alvin-Userbot is in progress, please wait 7-8 minutes'
                         )
        ups_rem.fetch(ac_br)
        repo.git.reset("--hard", "FETCH_HEAD")
        heroku_git_url = heroku_app.git_url.replace(
            "https://", "https://api:" + HEROKU_API_KEY + "@")
        if "heroku" in repo.remotes:
            remote = repo.remote("heroku")
            remote.set_url(heroku_git_url)
        else:
            remote = repo.create_remote("heroku", heroku_git_url)
        try:
            remote.push(refspec="HEAD:refs/heads/master", force=True)
        except GitCommandError as error:
            await event.edit(f'{txt}\nAn Error Occurred In The Log:\n{error}')
            return repo.__del__()
        build = app.builds(order_by="created_at", sort="desc")[0]
        if build.status == "failed":
            await event.edit(
                "Build Failed!\n" "Cancelled or there is some error..."
            )
            await asyncio.sleep(5)
            return await event.delete()
        else:
            await event.edit("Lord-Userbot Successfully Deployed!\n" "Restarting, Please Wait Master.....")
            await asyncio.sleep(15)
            await event.delete()

        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID, "#BOT \n"
                "Alvin-Userbot Has Been Updated")

    else:
        await event.edit('[HEROKU]:'
                         '\nPlease Prepare Variable **HEROKU_API_KEY** .'
                         )
        await asyncio.sleep(10)
        await event.delete()
    return


async def update(event, repo, ups_rem, ac_br):
    try:
        ups_rem.pull(ac_br)
    except GitCommandError:
        repo.git.reset("--hard", "FETCH_HEAD")
    await update_requirements()
    await event.edit('**☠️ Alvin-Userbot ☠️** Has Been Updated!')
    await asyncio.sleep(1)
    await event.edit('**☠️ Alvin-Userbot ☠️** Restarted....')
    await asyncio.sleep(1)
    await event.edit('Please Wait A Few Seconds Lord ツ')
    await asyncio.sleep(10)
    await event.delete()

    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID, "#BOT \n"
            "**Alvin-Userbot Has Been Updated ツ**")
        await asyncio.sleep(100)
        await event.delete()

    # Spin a new instance of bot
    args = [sys.executable, "-m", "userbot"]
    execle(sys.executable, *args, environ)
    return


@ register(outgoing=True, pattern=r"^;update(?: |$)(now|deploy)?")
async def upstream(event):
    "For .update command, check if the bot is up to date, update if specified"
    await event.edit("Checking Update, Please Wait....")
    conf = event.pattern_match.group(1)
    off_repo = UPSTREAM_REPO_URL
    force_update = False
    try:
        txt = "Sorry Master, the update can't be continued because "
        txt += "Some Problem Happened\n\n**LOGTRACE:**\n"
        repo = Repo()
    except NoSuchPathError as error:
        await event.edit(f'{txt}\nDirectory {error} cannot found')
        return repo.__del__()
    except GitCommandError as error:
        await event.edit(f'{txt}\nEarly Fail! {error}')
        return repo.__del__()
    except InvalidGitRepositoryError as error:
        if conf is None:
            return await event.edit(
                f"Unfortunately, Directory {error} Doesn't Appear From Repo."
                 "\nBut We Can Force Update Userbot Using .update now."
            )
        repo = Repo.init()
        origin = repo.create_remote("upstream", off_repo)
        origin.fetch()
        force_update = True
        repo.create_head("master", origin.refs.master)
        repo.heads.master.set_tracking_branch(origin.refs.master)
        repo.heads.master.checkout(True)

    ac_br = repo.active_branch.name
    if ac_br != UPSTREAM_REPO_BRANCH:
        await event.edit(
            '**[UPDATER]:**\n'
            f'Looks like you are using your own custom branch ({ac_br}). '
            'in that case, Updater is unable to identify '
            'which branch is to be merged. '
            'please checkout to any official branch')
        return repo.__del__()
    try:
        repo.create_remote('upstream', off_repo)
    except BaseException:
        pass

    ups_rem = repo.remote('upstream')
    ups_rem.fetch(ac_br)

    changelog = await gen_chlog(repo, f'HEAD..upstream/{ac_br}')

    if changelog == '' and force_update is False:
        await event.edit(
            f'\n**☠️ Alvin-Userbot is the latest version**\n')
        await asyncio.sleep(15)
        await event.delete()
        return repo.__del__()

    if conf is None and force_update is False:
        changelog_str = f'**☠️ Update For Alvin-Userbot [{ac_br}]:\n\n☠️ updates:**\n{changelog}'
        if len(changelog_str) > 4096:
            await event.edit("Changelog Too Big, View File To See It.")
            file = open("output.txt", "w+")
            file.write(changelog_str)
            file.close()
            await event.client.send_file(
                event.chat_id,
                "output.txt",
                reply_to=event.id,
            )
            remove("output.txt")
        else:
            await event.edit(changelog_str)
        return await event.respond('**Command To Update Alvin Userbot**\n >;update now\n >;update deploy\n\n__To Update Latest Features From Alvin Userbot.__')

    if force_update:
        await event.edit(
            'Force Sync To Latest Stable Userbot Code Please Wait .....')
    else:
        await event.edit('☠️ Alvin-Userbot Update Process, Loading....1%')
        await event.edit('☠️ Alvin-Userbot Update Process, Loading....20%')
        await event.edit('☠️ Alvin-Userbot Update Process, Loading....35%')
        await event.edit('☠️ Alvin-Userbot Update Process, Loading....77%')
        await event.edit('☠️ Alvin-Userbot Update Process, Updating...90%')
        await event.edit('☠️ Alvin-Userbot Update Process, please wait master....100%')
    if conf == "now":
        await update(event, repo, ups_rem, ac_br)
        await asyncio.sleep(10)
        await event.delete()
    elif conf == "deploy":
        await deploy(event, repo, ups_rem, ac_br, txt)
        await asyncio.sleep(10)
        await event.delete()
    return


CMD_HELP.update({
    'updater':
    ";update"
    "\nUsage: To View Latest Alvin-Userbot Updates."
    "\n\n;update now"
    "\nUsage: Updating Alvin-Userbot."
    "\n\n;update deploy"
    "\nUsage: Updating Alvin-Userbot By Re-Deploy."
})
