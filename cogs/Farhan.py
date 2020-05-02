import discord
from discord.ext import commands

class Farhan(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("ur mom")
        

def setup(client):
    client.add_cog(Farhan(client))