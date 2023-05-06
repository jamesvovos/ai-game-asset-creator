import requests
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# get Discord Token from .env file
load_dotenv()
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
DISCORD_CHANNEL_ID = os.getenv("DISCORD_CHANNEL_ID")

# file path
file = "././data/prompts.txt"

# create discord bot
bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())   

@bot.event
async def on_ready():
    channel = bot.get_channel(int(DISCORD_CHANNEL_ID))
    await channel.send("Midjourney Prompts Ready! Use /prompts to retrieve them")

# commands
# needs error checking for empty file (will cause error atm if prompts file is empty)

@bot.command()
async def prompts(ctx):
    with open(file, 'r') as f:
        prompt = f.readline()
        while prompt:
            await ctx.send(prompt)
            prompt = f.readline()
        channel = bot.get_channel(int(DISCORD_CHANNEL_ID))
        await channel.send("Copy the prompt -> Type in /imagine -> press tab -> paste prompt -> press enter to get game asset")


# run the command
bot.run(DISCORD_BOT_TOKEN)