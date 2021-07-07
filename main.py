import os

import discord
from discord.ext import commands
from dotenv import load_dotenv


class MyBot(commands.Bot):
    def __init__(self, command_prefix):
        super().__init__(
            command_prefix=commands.when_mentioned_or(command_prefix),
            intents=discord.Intents.all(),
            allowed_mentions=discord.AllowedMentions(
                everyone=False, roles=False, users=True
            ),
        )
        self.load_extension("cogs.management.admin")


if __name__ == "__main__":
    load_dotenv()
    bot = MyBot(command_prefix=os.environ["PREFIX"])
    bot.run(os.environ["TOKEN"])
