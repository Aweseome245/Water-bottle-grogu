import discord
from discord.ext import commands

class BotCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='changelog',
        description='Posts the current version of Grogu and all changes')
    async def changelog(self, ctx):
        """Grogu version and changes"""
        await ctx.send("Water Bottle Grogu version 1.8.5 Full Release")
        await ctx.send("Changes made in Reddit:")
        await ctx.send("Asynchronous checking no longer happens, which should speed up posting.")
        await ctx.send("Changes made in voice:")
        await ctx.send("Added a now playing command.")
        await ctx.send("Changes made overall:")
        await ctx.send("Code is now in cogs. This should help me code the bot a bit easier")
        await ctx.send("Tune in next time for the next update from Aweseome245!")

    @commands.command(
        name='changelog',
        description='Posts the current version of Grogu and all changes')
    async def changelog(self, ctx):
        """Grogu version and changes"""
        changelog = open("changelog.txt", "r")
        newLog = changelog.read()
        changelog.close()
        await ctx.send(newLog)

    @commands.command(
        name='devon',
        description='Use this command to see whether Aweseome245 is available or not!')
    async def changelog(self, ctx):
        """Checks whether the developer of the bot is available."""
        devOn = open("devon.txt", "r")
        aweseome245on = devOn.read()
        devOn.close()
        if aweseome245on == "0":
            await ctx.send("My developer is currently not online, but has left me running.")
        elif aweseome245on == "1":
            await ctx.send("My developer is online, and is available to speak to!")
        else:
            await ctx.send("My developer is online, but is currently doing schoolwork.")

def setup(bot):
    bot.add_cog(BotCommands(bot))
