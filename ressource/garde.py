import discord

from ressource.AER_team import ALESSANDRO, CZ, LUCAS, MAYA, UGO, _format_discord_user
from ressource.time import get_time

WEEK = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
TEAM_AER = [UGO, ALESSANDRO, LUCAS, MAYA, CZ, "Close", "Close"] 

SEPARATOR = "\n---------------------------\n"


async def guard_list(client: discord.Bot):
    i = 0 
    calandar = """"""
    while i <= 6: 
        calandar = calandar + await calandar_guard(client, TEAM_AER[i], WEEK[i]) + SEPARATOR
        i += 1 
    return calandar


async def calandar_guard(client: discord.Bot, Name, Day:str) -> str:
    if Name == "Close" : 
        calandar = f"""
            {Day} : {get_time()[1]}
        
        The school is closed

        """
        return calandar
    else :
        discord_name = await _format_discord_user(client, Name[1])
        calandar =f"""
        {Day} : {get_time()[1]}

    AER : {Name[0]}
        
        Contacter :
            Email -> {Name[2]}
            Discord -> {discord_name}
        """
        return calandar