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

def setup(bot):
    bot.add_cog(Fun(bot))
