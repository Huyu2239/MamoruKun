import os

import git
from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.repo = git.Repo()
        self.bot.load_extension("cogs.management.eval")
        self._load_cogs()
        print('loaded')

    def _load_cogs(self):
        for cog in os.listdir("./cogs"):
            if cog.endswith(".py"):
                try:
                    self.bot.load_extension(f"cogs.{cog[:-3]}")
                except commands.ExtensionAlreadyLoaded:
                    self.bot.reload_extension(f"cogs.{cog[:-3]}")

    async def cog_check(self, ctx):
        return await self.bot.is_owner(ctx.author)

    @commands.command()
    async def git_pull(self, ctx):
        msg = await ctx.send("実行中・・・")
        self.repo.remotes.origin.pull()
        print("pulled")
        await msg.edit(content="完了")

    @commands.command()
    async def reload(self, ctx):
        msg = await ctx.send("更新中")
        for cog in os.listdir("./cogs"):
            if cog.endswith(".py"):
                try:
                    self.bot.unload_extension(f"cogs.{cog[:-3]}")
                except commands.ExtensionNotLoaded:
                    pass
                self._load_cogs()
        await msg.edit(content="更新しました")
        print("--------------------------------------------------")


def setup(bot):
    bot.add_cog(Admin(bot))