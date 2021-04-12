import discord
import urllib.parse, urllib.request, re
import time
import asyncio
import praw
import random
import youtube_dl
from discord.ext import commands
from discord.utils import get

reddit = praw.Reddit(client_id='p03M1i1KZqfabA',
                     client_secret='EQex0eQntJu-bFOKTQMy809J2tx9Kg',
                     user_agent='windows:MyExampleApp:v1 (by u/YaBoi245)',
                     check_for_async=False)

class Reddit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='meme',
        description='Pulls a meme from r/memes.')
    async def meme(self, ctx):
        """Spicy memes from Reddit."""
        memes_submissions = reddit.subreddit('memes').hot()
        post_to_pick = random.randint(1, 50)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)

        await ctx.send(submission.url)

    @commands.command(
        name='cake',
        description='Posts a random picture of cake')
    async def cake(self, ctx):
        """GLaDOS' favourite subreddit."""
        memes_submissions = reddit.subreddit('cake').hot()
        post_to_pick = random.randint(1, 50)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)

        await ctx.send(submission.url)

    @commands.command(
        name='minecraftbuild',
        description='Pulls a build from r/MinecraftBuilds.')
    async def minecraftbuild(self, ctx):
        """Pro gamers being cool."""
        prequelMemes_submissions = reddit.subreddit('MinecraftBuilds').hot()
        post_to_pick = random.randint(1, 50)
        for i in range(0, post_to_pick):
            submission = next(x for x in prequelMemes_submissions if not x.stickied)

        await ctx.send(submission.url)

    @commands.command(
        name='prequelmeme',
        description='Pulls a meme from r/PrequelMemes.')
    async def prequelMeme(self, ctx):
        """One of, if not the most civilised subreddit on the platform."""
        prequelMemes_submissions = reddit.subreddit('PrequelMemes').hot()
        post_to_pick = random.randint(1, 50)
        for i in range(0, post_to_pick):
            submission = next(x for x in prequelMemes_submissions if not x.stickied)

        await ctx.send(submission.url)

    @commands.command(
        name='terrariameme',
        description='Pulls a meme from r/TerrariaMemes.')
    async def terrariameme(self, ctx):
        """Memes based on my suffering! How lovely."""
        prequelMemes_submissions = reddit.subreddit('TerrariaMemes').hot()
        post_to_pick = random.randint(1, 50)
        for i in range(0, post_to_pick):
            submission = next(x for x in prequelMemes_submissions if not x.stickied)

        await ctx.send(submission.url)
    
def setup(bot):
    bot.add_cog(Reddit(bot))
