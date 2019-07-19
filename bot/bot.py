import os
import praw

USER_AGENT = "Reddit-StarsMod by /u/ChaoticWeg"


def __check_environment():
    """ Checks that all required environment variables are set """
    required_values = ["REDDIT_USERNAME", "REDDIT_PASSWORD", "REDDIT_CLIENT_ID", "REDDIT_CLIENT_SECRET"]
    for value in required_values:
        assert os.getenv(value, None) is not None, f"{value} missing from .env"


def create_bot():
    """ Inner wrapped function to create bot and stuff """
    __check_environment()
    bot = praw.Reddit(
        username=os.getenv("REDDIT_USERNAME"),
        password=os.getenv("REDDIT_PASSWORD"),
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=USER_AGENT
    )
    assert str(bot.user.me()) == os.getenv("REDDIT_USERNAME"), "Unable to authenticate! Check credentials in .env"
    return bot
