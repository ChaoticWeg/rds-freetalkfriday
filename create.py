from bot import create_bot, get_title, get_body
from dotenv import load_dotenv
load_dotenv()

SUBREDDIT = "TestStars"


def make_post(bot):
    """ Creates a Free Talk Friday post. """
    assert bot is not None, "Bot cannot be None!"
    return bot.subreddit(SUBREDDIT).submit(
        selftext=get_body(),
        title=get_title(),
        send_replies=False
    )


def sticky_post(post):
    """ Stickies the post """
    post.mod.distinguish()
    post.mod.sticky()


def run():
    bot = create_bot()
    post = make_post(bot)
    sticky_post(post)


if __name__ == "__main__":
    run()
