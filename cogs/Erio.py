import discord
from discord.ext import commands


class Erio(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def calc(self,ctx):
        url = ctx.message.attachments[0].url
        await ctx.send('is this your url? {}'.format(url))


def setup(client):
    client.add_cog(Erio(client))
