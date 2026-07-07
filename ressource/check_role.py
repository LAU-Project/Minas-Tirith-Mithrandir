import discord


def get_user_role_names(user_roles: list[discord.Role]) -> list[str]:
    return [role.name for role in user_roles]


def check_role(roles_authorized: list[str], user_roles: list[discord.Role]) -> bool:
    user_role_names = get_user_role_names(user_roles)
    return any(role_name in roles_authorized for role_name in user_role_names)