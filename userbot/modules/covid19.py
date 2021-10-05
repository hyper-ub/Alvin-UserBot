from covid import Covid
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^;covid (.*)")
async def corona(event):
    await event.edit("_processing Information...._")
    country = event.pattern_match.group(1)
    covid = Covid(source="worldometers")
    country_data = covid.get_status_by_country_name(country)
    if country_data:
        output_text = f"`⚠️Confirmed : {country_data['confirmed']} (+{country_data['new_cases']})`\n"
        output_text += f"`☢️Active         : {country_data['active']}`\n"
        output_text += f"`🤕critical        : {country_data['critical']}`\n"
        output_text += f"`😟new deaths : {country_data['new_deaths']}`\n\n"
        output_text += f"`⚰️deaths     : {country_data['deaths']} (+{country_data['new_deaths']})`\n"
        output_text += f"`😔new cases    : {country_data['new_cases']}`\n"
        output_text += f"`😇recovered        : {country_data['recovered']}`\n"
        output_text += "`📍Total Tes     : N/A`\n\n"
        output_text += f"Data provided by [Worldometer](https://www.worldometers.info/coronavirus/country/{country})"
    else:
        output_text = "*No information found for this Country!*"

    await event.edit(f"Coronavirus info at {country}:\n\n{output_text}")


@register(outgoing=True, pattern="^;covid$")
async def corona(event):
    await event.edit("_processing..._")
    country = "World"
    covid = Covid(source="worldometers")
    country_data = covid.get_status_by_country_name(country)
    if country_data:
        output_text = f"`⚠️confirmed : {country_data['confirmed']} (+{country_data['new_cases']})`\n"
        output_text += f"`☢️active         : {country_data['active']}`\n"
        output_text += f"`🤕critical        : {country_data['critical']}`\n"
        output_text += f"`😟New deaths : {country_data['new_deaths']}`\n\n"
        output_text += f"`⚰️deaths     : {country_data['deaths']} (+{country_data['new_deaths']})`\n"
        output_text += f"`😔new cases    : {country_data['new_cases']}`\n"
        output_text += f"`😇recovered        : {country_data['recovered']}`\n"
        output_text += "`📍Total Tes     : N/A`\n\n"
        output_text += f"Data provided by [Worldometer](https://www.worldometers.info/coronavirus/country/{country})"
    else:
        output_text = "*No information found for this Country!*"

    await event.edit(f"coronavirus info at {country}:\n\n{output_text}")


CMD_HELP.update({"corona": ";covid **<country>**"
                 "\nexplanation: Get information about covid-19 data in a country.\n\n"
                 ";covid"
                 "\nexplanation: Get information about covid-19 data around the world.\n"})
