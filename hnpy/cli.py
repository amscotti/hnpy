import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch and display top Hacker News stories."
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=30,
        help="Number of top stories to display (default: 30)",
    )
    parser.add_argument(
        "--hide-url", action="store_true", help="Hide story URLs in output"
    )
    return parser.parse_args()
