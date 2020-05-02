import discord
from discord.ext import commands
from mathpix.mathpix import MathPix


reader = MathPix(
    app_id="discalculator_gmail_com_f307ad", app_key="684b628a6ac77aeb3d1f"
)


class Farhan(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def convert(self, ctx):
        url = ctx.message.attachments[0].url
        ocr = reader.process_image(image_url=url)
        await ctx.send(ocr.latex)


def setup(client):
    client.add_cog(Farhan(client))
