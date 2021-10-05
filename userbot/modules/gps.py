from geopy.geocoders import Nominatim
from telethon.tl import types
from userbot.events import register
from userbot import CMD_HELP


@register(outgoing=True, pattern="^;gps(?: |$)(.*)")
async def gps(event):
    if event.fwd_from:
        return
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    input_str = event.pattern_match.group(1)

    if not input_str:
        return await event.edit("_Master please give me the place you are looking for_")

    await event.edit("_finding this location in server map...._")

    geolocator = Nominatim(user_agent="Alvin")
    geoloc = geolocator.geocode(input_str)

    if geoloc:
        lon = geoloc.longitude
        lat = geoloc.latitude
        await reply_to_id.reply(
            input_str,
            file=types.InputMediaGeoPoint(
                types.InputGeoPoint(
                    lat, lon
                )
            )
        )
        await event.delete()
    else:
        await event.edit("_Sorry master,i can't found it_")

CMD_HELP.update({
    "gps":
    ">;gps"
    "\nUsage: to get location map"
})
