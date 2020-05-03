import discord
from discord.ext import commands
from mathpix.mathpix import MathPix
from PIL import Image
import requests
import wolframalpha

reader = MathPix(
    app_id="discalculator_gmail_com_f307ad", app_key="684b628a6ac77aeb3d1f"
)


class Farhan(commands.Cog):
    def __init__(self, client):
        self.client = client

    def basecalc(self, query):
        wolfclient = wolframalpha.Client("L766YW-6V34XVRVWG")
        res = wolfclient.query(query)

        if hasattr(res, "results"):
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
    async def convert(self, ctx):
        try:
            msg = ctx.message.content[8:]
            ocr = reader.process_image(image_url=ctx.message.attachments[0].url)
            Farhan.latexToImage(self, ocr.latex)
            await ctx.send(ocr.latex)
            await ctx.send(file=discord.File("pls.jpg"))
            result = await self.client.loop.run_in_executor(
                None, Farhan.basecalc, self, msg + " " + ocr.latex
            )
            Farhan.latexToImage(self, result)
            await ctx.send(result)
            await ctx.send(file=discord.File("pls.jpg"))
        except:
            await ctx.send("Took too long!")


def setup(client):
    client.add_cog(Farhan(client))
