from discord.ext import commands

class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def killShuana(self, ctx):
        return await ctx.send("I killed Shuana :)")
def setup(bot):
    bot.add_cog(FunCog(bot))
