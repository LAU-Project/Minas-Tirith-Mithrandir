import discord
from os import getenv
from dotenv import load_dotenv

load_dotenv()

UGO_ID = getenv("ID_UGO")
ALESSANDRO_ID = getenv("ID_ALESSANDRO")
LUCAS_ID = getenv("ID_LUCAS")
MAYA_ID = getenv("ID_MAYA")
CZ_ID = getenv("ID_CZ")

UGO = ["PASCALLON Ugo", UGO_ID, "ugo.pascallon@epitech.eu"]
ALESSANDRO = ["PARIS Alessandro", ALESSANDRO_ID, "alessandro1.paris@epitech.eu"]
LUCAS = ["EECKHOUTTE Lucas", LUCAS_ID, "lucas1.eeckhoutte@epitech.eu"]
MAYA = ["DENTAL Maya", MAYA_ID, "maya1.dental@epitech.eu"]
CZ = ["PEUCH Celenzo", CZ_ID, "celenzo.peuch@epitech.eu"]


def aer(AER:list) -> str:
    return f"""
    {AER[0]}
        
        Contacter :
            Email -> {AER[2]}
            Discord -> {AER[1]}
"""

SEPARATOR = "\n---------------------------\n"

async def _format_discord_user(client: discord.Bot, user_id: str | None) -> str:
    if not user_id:
        return "Inconnu"

    try:
        user = await client.fetch_user(int(user_id))
    except (discord.NotFound, discord.Forbidden, discord.HTTPException, ValueError):
        return f"<@{user_id}>"

    return f"{user.name} ({user.display_name})"


async def get_aer_team(client: discord.Bot) -> str:
    team = [UGO, LUCAS, ALESSANDRO, MAYA, CZ]
    lines = []

    for member in team:
        discord_name = await _format_discord_user(client, member[1])
        lines.append(
            f"""
    {member[0]}
        
        Contacter :
            Email -> {member[2]}
            Discord -> {discord_name}
""".strip()
        )

    return SEPARATOR.join(lines)

