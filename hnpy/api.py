import httpx

from typing import Any, cast, Optional, Type, Self
from types import TracebackType


class HackerNewsAPI:
    STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
    ITEM_URL_BASE = "https://hacker-news.firebaseio.com/v0/item"

    def __init__(self) -> None:
        self.client = httpx.AsyncClient()

    async def fetch_top_stories(self, limit: int = 30) -> list[int]:
        response = await self.client.get(self.STORIES_URL)
        response.raise_for_status()
        all_ids = response.json()
        return cast(list[int], all_ids[:limit])

    async def fetch_story(self, story_id: int) -> dict[str, Any]:
        response = await self.client.get(f"{self.ITEM_URL_BASE}/{story_id}.json")
        response.raise_for_status()
        return cast(dict[str, Any], response.json())

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        await self.client.aclose()
