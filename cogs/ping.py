from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        msg = await ctx.send("pong!")
        await msg.edit(content=f"pong!\n`{self.bot.ws.latency * 1000:.0f}ms`")


def setup(bot):
    bot.add_cog(Ping(bot))