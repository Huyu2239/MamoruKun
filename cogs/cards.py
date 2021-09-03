from discord.ext import commands


class Card(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def card(self, ctx, person, card, count):
        pass


def setup(bot):
    bot.add_cog(Card(bot))
