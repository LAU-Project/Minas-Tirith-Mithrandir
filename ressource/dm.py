import asyncio
import datetime
from typing import Any


async def wait_until_next_42_minute() -> float:
    """Retourne le nombre de secondes avant le prochain :42."""
    now = datetime.datetime.now()
    target = now.replace(minute=42, second=0, microsecond=0)

    if now >= target:
        target += datetime.timedelta(hours=1)

    return (target - now).total_seconds()


async def send_dm_every_hour_at_42(client: Any, user_id: int, message: str) -> None:
    """
    Envoie un message privé à un utilisateur tous les jours à XX:42.

    Exemples:
        asyncio.create_task(send_dm_every_hour_at_42(bot, 123456789012345678, "Test"))
    """
    user = await client.fetch_user(user_id)

    while True:
        delay = await wait_until_next_42_minute()
        await asyncio.sleep(delay)

        try:
            await user.send(message)
            print(f"MP envoyé à {user_id} à {datetime.datetime.now().strftime('%H:%M:%S')}")
        except Exception as exc:
            print(f"Impossible d'envoyer le MP à {user_id}: {exc}")
            # On continue quand même, pour ne pas arrêter la boucle.
            continue