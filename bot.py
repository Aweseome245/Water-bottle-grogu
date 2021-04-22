import discord
import urllib.parse, urllib.request, re
import time
import asyncio
import praw
import random
import youtube_dl
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command_prefix=['w!', "W!"],
                      description="VC, Reddit, randomness, you want it? It's yours my friend.\n As long as you have this bot on your server.")

client.load_extension("cogs.BotCommands")

client.help_command.cog = client.cogs["BotCommands"]

client.load_extension("cogs.Music")

client.load_extension("cogs.Fun")

client.load_extension("cogs.Reddit")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('w!help for commands'))
    print('Bot ready.')

client.run('Nzk1OTk0MjY2NDYzMzcxMjk2.X_RdbQ.in0sHR6Md9eWQF47jWIvGZJrt4A')
