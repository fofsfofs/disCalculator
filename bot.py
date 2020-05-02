import discord
import os
import datetime

from discord.ext import commands

client = commands.Bot(command_prefix=".")
time = datetime.datetime.now()


@client.event
async def on_ready():
    print(f"Bot is ready! {time.hour}:{time.minute}")


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")
    await ctx.send(extension + " has been loaded ✅")


@client.command()
async def test(ctx):
    await ctx.send("bn")


@client.command()
async def stop(ctx):
    await client.logout()


for filename in os.listdir("D:/Google Drive/disCalculator/cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run("NzA0Nzk3ODg4MTM1NTYxMzA3.XqyIZQ.9fwMHY6YpI3w_BYgtiA342txXGY")
