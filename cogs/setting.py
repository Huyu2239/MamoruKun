from discord.ext import commands


class Setting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setting(self, ctx):
        pass


def setup(bot):
    bot.add_cog(Setting(bot))