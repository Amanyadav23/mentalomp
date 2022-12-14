import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

from AdityaHalder.utilities import config
from AdityaHalder.utilities.config.config import BANNED_USERS
from AdityaHalder import app, bot, LOGGER
from AdityaHalder.modules.core.call import aditya
from AdityaHalder.plugins import ALL_MODULES
from AdityaHalder.modules.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("â¦âÍâ¬ð¾ ðâ¬ð¥ð¦  ViÍ¥ruÍ£sÍ« ð¦  ð¥").error(
            "ð¥ ðð¨ ðð¬ð¬ð¢ð¬ð­ðð§ð­ ðð¥ð¢ðð§ð­ð¬ [ððð«ð¬] ðð¨ð®ð§ðâ"
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("â¦âÍâ¬ð¾ ðâ¬ð¥ð¦  ViÍ¥ruÍ£sÍ« ð¦  ð¥").warning(
            "ð¥ ðð¨ ðð©ð¨ð­ð¢ðð² ððð«ð¬ ðððð¢ð§ððâ...\nð· ðð¨ð®ð« ðð¨ð­ ðð¨ð§'ð­ ðð ððð¥ð ðð¨ ðð¥ðð² ðð©ð¨ð­ð¢ðð² ðð®ðð«ð¢ðð¬â..."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await bot.start()
    for all_module in ALL_MODULES:
        importlib.import_module("AdityaHalder.plugins" + all_module)
    LOGGER("AdityaHalder.modules.plugins").info(
        "ð¥ ðð®ððð¬ð¬ðð®ð¥ð¥ð² ðð¦ð©ð¨ð«ð­ðð ðð¥ð¥ ðð¨ðð®ð¥ðð¬ ð¿ "
    )
    await app.start()
    await aditya.start()
    try:
        await aditya.stream_call(
            "http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("â¦âÍâ¬ð¾ ðâ¬ð¥ð¦  ViÍ¥ruÍ£sÍ« ð¦  ð¥").error(
            "[ðð«ð«ð¨ð«] - \n\nð¥ ðð¥ððð¬ð ðð®ð«ð§ ðð§ ðð¨ð¢ðð ðð¡ðð­ ðð ðð¨ð®ð« ðð¨ð ð ðð« ðð«ð¨ð®ð©â..."
        )
        sys.exit()
    except:
        pass
    await aditya.decorators()
    LOGGER("â¦âÍâ¬ð¾ ðâ¬ð¥ð¦  ViÍ¥ruÍ£sÍ« ð¦  ð¥").info("ð¥³ ðð¨ð§ð ð«ðð­ð®ð¥ðð­ð¢ð¨ð§ð¬, ðð¨ð®ð« ðð¨ð­ ðð®ðððð¬ð¬ðð®ð¥ð¥ð² ððð©ð¥ð¨ð²ðð â¨...")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("Aman Yadav").info("ð ðð²ð¬ð­ðð¦ ðð­ð¨ð©ð©ðð, ðð¨ð¨ððð²ðâ...")
