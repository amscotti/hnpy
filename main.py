import asyncio
from hnpy.api import HackerNewsAPI
from hnpy.formatting import print_stories
from hnpy.cli import parse_args


async def main(limit: int = 30, hide_url: bool = False) -> None:
    async with HackerNewsAPI() as api:
        stories_id = await api.fetch_top_stories(limit)
        stories = await asyncio.gather(
            *[api.fetch_story(story_id) for story_id in stories_id]
        )

    print_stories(stories, hide_url)


if __name__ == "__main__":
    args = parse_args()
    limit = args.limit
    hide_url = args.hide_url

    asyncio.run(main(limit, hide_url))
