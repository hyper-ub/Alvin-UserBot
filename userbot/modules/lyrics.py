import os
import lyricsgenius

from userbot.events import register
from userbot import CMD_HELP, GENIUS, lastfm, LASTFM_USERNAME
from pylast import User

if GENIUS is not None:
    genius = lyricsgenius.Genius(GENIUS)


@register(outgoing=True, pattern="^;lyrics (?:(now)|(.*) - (.*))")
async def lyrics(lyric):
    await lyric.edit("_Getting information..._")
    if GENIUS is None:
        await lyric.edit(
            "_Provide genius access token to Heroku ConfigVars..._")
        return False
    if lyric.pattern_match.group(1) == "now":
        playing = User(LASTFM_USERNAME, lastfm).get_now_playing()
        if playing is None:
            await lyric.edit(
                "_No information current lastfm scrobbling..._"
            )
            return False
        artist = playing.get_artist()
        song = playing.get_title()
    else:
        artist = lyric.pattern_match.group(2)
        song = lyric.pattern_match.group(3)
    await lyric.edit(f"_Searching lyrics for {artist} - {song}..._")
    songs = genius.search_song(song, artist)
    if songs is None:
        await lyric.edit(f"_Song_  **{artist} - {song}**  _not found..._")
        return False
    if len(songs.lyrics) > 4096:
        await lyric.edit("_Lyrics is too big, view the file to see it._")
        with open("lyrics.txt", "w+") as f:
            f.write(f"Search query: \n{artist} - {song}\n\n{songs.lyrics}")
        await lyric.client.send_file(
            lyric.chat_id,
            "lyrics.txt",
            reply_to=lyric.id,
        )
        os.remove("lyrics.txt")
        return True
    else:
        await lyric.edit(
            f"**Search query**:\n`{artist}` - `{song}`"
            f"\n\n```{songs.lyrics}```"
        )
        return True


CMD_HELP.update({
    "lyrics":
    ";lyrics **<artist name> - <song name>**"
    "\nUsage: Get lyrics matched artist and song."
    "\n\n;lyrics now"
    "\nUsage: Get lyrics artist and song from current lastfm scrobbling."
})
