import discord
from discord.ext import commands
from mathpix.mathpix import MathPix
from PIL import Image
import requests


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

        formula = ocr.latex.replace("\n", " ")
        r = requests.get(
            "http://latex.codecogs.com/png.latex?\dpi{{300}} {formula}".format(
                formula=formula
            )
        )
        f = open("example.png", "wb")
        f.write(r.content)
        f.close()

        im = Image.open("example.png")
        rgb_im = im.convert("RGB")
        rgb_im.save("pls.jpg")
        await ctx.send(file=discord.File("pls.jpg"))


def setup(client):
    client.add_cog(Farhan(client))
