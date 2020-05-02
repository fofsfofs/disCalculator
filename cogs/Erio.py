import discord
from discord.ext import commands


class Erio(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def testicles(self, ctx):
        await ctx.send("HONK")


def setup(client):
    client.add_cog(Erio(client))
