import asyncio
from logging import Logger, StreamHandler
from os import environ as env
from random import choice

from aiohttp import ClientSession

from novelai_api import NovelAIAPI
from novelai_api.GlobalSettings import GlobalSettings
from novelai_api.story import NovelAI_Story
from novelai_api.utils import get_encryption_key

if "NAI_USERNAME" not in env or "NAI_PASSWORD" not in env:
    raise RuntimeError("Please ensure that NAI_USERNAME and NAI_PASSWORD are set in your environment")

username = env["NAI_USERNAME"]
password = env["NAI_PASSWORD"]

logger = Logger("NovelAI")
logger.addHandler(StreamHandler())


async def story_manipulation(api: NovelAIAPI):
    api.timeout = 30

    await api.high_level.login(username, password)

    key = get_encryption_key(username, password)
    keystore = await api.high_level.get_keystore(key)

    global_settings = GlobalSettings()

    story_handler = NovelAI_Story(api, keystore, global_settings)
    await story_handler.load_from_remote()

    id_list = list(story_handler)
    story_id = choice(id_list)

    story = story_handler[story_id]

    for _ in range(10):
        await story.generate()


#        logger.info(story)
#        logger.info(dumps(story._storycontent["data"]["story"]["fragments"], indent = 4))
#        logger.info("")


async def test_story_manipulation_sync():
    # sync handler
    api = NovelAIAPI()
    await story_manipulation(api)


async def test_story_manipulation_async():
    # async handler
    try:
        async with ClientSession() as session:
            api = NovelAIAPI(session)
            await story_manipulation(api)
    except Exception as e:
        await session.close()
        raise e


if __name__ == "__main__":
    asyncio.run(test_story_manipulation_async())
