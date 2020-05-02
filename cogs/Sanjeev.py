import discord
from discord.ext import commands


class Sanjeev(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def henlo(self, ctx):
        await ctx.send("bread")


def setup(client):
    client.add_cog(Sanjeev(client))
