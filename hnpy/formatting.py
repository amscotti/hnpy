from rich.console import Console

from typing import Any

HACKERNEWS_URL = "https://news.ycombinator.com/item?id="


def format_story(story: dict[str, Any], hide_url: bool = False) -> str:
    output = f"[bold]{story['title']}[/bold]\n"
    output += f"[green]score: {story['score']}[/green]\t[blue]comments: {story.get('descendants', 0)}[/blue]\t[yellow]user: {story['by']}[/yellow]\n"
    if not hide_url:
        output += f"url: [link={HACKERNEWS_URL}{story['id']}]{HACKERNEWS_URL}{story['id']}[/link]\n"
    return output


def print_stories(stories: list[Any], hide_url: bool) -> None:
    console = Console()
    for story in stories:
        console.print(format_story(story, hide_url), markup=True)
