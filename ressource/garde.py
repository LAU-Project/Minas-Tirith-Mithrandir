from ressource.time import get_time

WEEK = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
TEAM_AER = ["Ugo PASCALLON", "Alessandro PARIS", "Lucas EECKHOUTTE", "Maya DENTAL", "Celenzo PEUCH", "Close", "Close"] 

SEPARATOR = "\n---------------------------\n"

def guard_list():
    i = 0 
    calandar = """"""
    while i <= 6: 
        calandar = calandar + calandar_guard(TEAM_AER[i], WEEK[i]) + SEPARATOR
        i += 1 
    return calandar


def calandar_guard(Name:str, Day:str) -> str:
    if Name == "Close" : 
        calandar = f"""
            {Day} : {get_time()[1]}
        
        The school is closed

        """
        return calandar
    else :
        calandar =f"""
        {Day} : {get_time()[1]}

    AER : {Name}
        
        Contacter :
            Email -> 
            Discord ->
        """
        return calandar