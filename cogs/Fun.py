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
        clones11 = open("clones_11.txt", "r")
        clones12 = open("clones_12.txt", "r")
        clones13 = open("clones_13.txt", "r")
        clones14 = open("clones_14.txt", "r")
        clones15 = open("clones_15.txt", "r")
        clones16 = open("clones_16.txt", "r")
        clones17 = open("clones_17.txt", "r")
        clones18 = open("clones_18.txt", "r")
        clones19 = open("clones_19.txt", "r")
        clones20 = open("clones_20.txt", "r")
        clones21 = open("clones_21.txt", "r")
        clones22 = open("clones_22.txt", "r")
        clones23 = open("clones_23.txt", "r")
        clones24 = open("clones_24.txt", "r")
        clones25 = open("clones_25.txt", "r")
        clones26 = open("clones_26.txt", "r")
        clones27 = open("clones_27.txt", "r")
        clones28 = open("clones_28.txt", "r")
        clones29 = open("clones_29.txt", "r")
        clones30 = open("clones_30.txt", "r")

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
        cloneText11 = clones11.read()
        cloneText12 = clones12.read()
        cloneText13 = clones13.read()
        cloneText14 = clones14.read()
        cloneText15 = clones15.read()
        cloneText16 = clones16.read()
        cloneText17 = clones17.read()
        cloneText18 = clones18.read()
        cloneText19 = clones19.read()
        cloneText20 = clones20.read()
        cloneText21 = clones21.read()
        cloneText22 = clones22.read()
        cloneText23 = clones23.read()
        cloneText24 = clones24.read()
        cloneText25 = clones25.read()
        cloneText26 = clones26.read()
        cloneText27 = clones27.read()
        cloneText28 = clones28.read()
        cloneText29 = clones29.read()
        cloneText30 = clones30.read()

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
        await ctx.send(cloneText11)
        await ctx.send(cloneText12)
        await ctx.send(cloneText13)
        await ctx.send(cloneText14)
        await ctx.send(cloneText15)
        await ctx.send(cloneText16)
        await ctx.send(cloneText17)
        await ctx.send(cloneText18)
        await ctx.send(cloneText19)
        await ctx.send(cloneText20)
        await ctx.send(cloneText21)
        await ctx.send(cloneText22)
        await ctx.send(cloneText23)
        await ctx.send(cloneText24)
        await ctx.send(cloneText25)
        await ctx.send(cloneText26)
        await ctx.send(cloneText27)
        await ctx.send(cloneText28)
        await ctx.send(cloneText29)
        await ctx.send(cloneText30)
        
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
        clones11.close()
        clones12.close()
        clones13.close()
        clones14.close()
        clones15.close()
        clones16.close()
        clones17.close()
        clones18.close()
        clones19.close()
        clones20.close()
        clones21.close()
        clones22.close()
        clones23.close()
        clones24.close()
        clones25.close()
        clones26.close()
        clones27.close()
        clones28.close()
        clones29.close()
        clones30.close()
        

def setup(bot):
    bot.add_cog(Fun(bot))
