import discord
from discord.ext import commands


class Shoeb(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def anime(self, ctx):
        await ctx.send("If you don't watch Vinland Saga then you need to reevaluate your life.")


def setup(client):
    client.add_cog(Shoeb(client))
