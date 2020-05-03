import discord
from discord.ext import commands
from mathpix.mathpix import MathPix
from PIL import Image
import requests
import wolfram

reader = MathPix(
    app_id="discalculator_gmail_com_f307ad", app_key="684b628a6ac77aeb3d1f"
)

class Shoeb(commands.Cog):
    def __init__(self, client):
        self.client = client

    def basemath(self,query):
        res = wolfram.wolfclient.query(query)

        if hasattr(res, 'results'):
            return next(res.results).text
        else:
            return None

    def latexToImage(self, somethingelse):
        # url = ctx.message.attachments[0].url

        formula = somethingelse.replace("\n", " ")
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

    @commands.command()
    async def math(self, ctx):
        msg = ctx.message.content[5:]
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
        await ctx.trigger_typing()
        result = await self.client.loop.run_in_executor(None, Shoeb.basemath, self, msg + " " + ocr.latex)
        await ctx.send(result)

        try:
            await ctx.send(file=discord.File("pls.jpg"))
            await ctx.trigger_typing()
            result = await self.client.loop.run_in_executor(None, Shoeb.basemath, self, msg + " " + ocr.latex)
            await ctx.send(result)
            await Shoeb.latexToImage(self,result)
        except:
            await ctx.send("Took too long! Or an unexpected error occurred.")


def setup(client):
    client.add_cog(Shoeb(client))
