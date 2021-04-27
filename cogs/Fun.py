import discord
import urllib.parse, urllib.request, re
import time
import asyncio
import praw
import random
import youtube_dl
from discord.ext import commands
from discord.utils import get

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='coolestpersonalive',
        description="Who's the coolest person alive?")
    async def coolestPersonAlive(self, ctx):
        """Find out who the coolest person alive is!"""
        if ctx.message.author.id == 293089328026877952:
            await ctx.send("Who's the coolest person alive?")
            await ctx.send("It's you, Aweseome245!")
        else:
            await ctx.send("Who's the coolest person alive?")
            await ctx.send("Not you for sure.")

    @commands.command(
        name='hellothere',
        description='General Kenobi!')
    async def helloThere(self, ctx):
        """The civilised greeting."""
        await ctx.send(file=discord.File('tenor.gif'))

    @commands.command(
        name='order66',
        description='Execute Order 66.')
    async def order66(self, ctx):
        """Haha lightsaber go swish"""
        if ctx.message.author.id == 293089328026877952:
            await ctx.send('Yes, my lord.')
            await ctx.send(file=discord.File('giphy.gif'))
        else:
            await ctx.send(file=discord.File('giphy.gif'))

    @commands.command(
        name='splash',
        description='Splash someone. Syntax: w!splash [insert text here]')
    async def splash(self, ctx, *, arg):
        """Force hydration."""
        await ctx.send('{} has been splashed!'.format(arg))

    @commands.command(
        name='clones',
        description='Every single clone, in alphabetical order.')
    async def changelog(self, ctx):
        """CLONES"""
        clones1 = open("clones_1.txt", "r")
        clones2 = open("clones_2.txt", "r")
        clones3 = open("clones_3.txt", "r")
        clones4 = open("clones_4.txt", "r")
        clones5 = open("clones_5.txt", "r")
        clones6 = open("clones_6.txt", "r")
        clones7 = open("clones_7.txt", "r")
        clones8 = open("clones_8.txt", "r")
        clones9 = open("clones_9.txt", "r")
        clones10 = open("clones_10.txt", "r")

        cloneText1 = clones1.read()
        cloneText2 = clones2.read()
        cloneText3 = clones3.read()
        cloneText4 = clones4.read()
        cloneText5 = clones5.read()
        cloneText6 = clones6.read()
        cloneText7 = clones7.read()
        cloneText8 = clones8.read()
        cloneText9 = clones9.read()
        cloneText10 = clones10.read()

        await ctx.send(cloneText1)
        await ctx.send(cloneText2)
        await ctx.send(cloneText3)
        await ctx.send(cloneText4)
        await ctx.send(cloneText5)
        await ctx.send(cloneText6)
        await ctx.send(cloneText7)
        await ctx.send(cloneText8)
        await ctx.send(cloneText9)
        await ctx.send(cloneText10)
        
        clones1.close()
        clones2.close()
        clones3.close()
        clones4.close()
        clones5.close()
        clones6.close()
        clones7.close()
        clones8.close()
        clones9.close()
        clones10.close()

def setup(bot):
    bot.add_cog(Fun(bot))
