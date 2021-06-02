import discord
import urllib.parse, urllib.request, re
import time
import asyncio
import random
import youtube_dl
from discord.ext import commands
from discord.utils import get

FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

VCleave = 0

VCautoleave = 0

def convert(arg):
    min, sec = divmod(arg, 60)
    hour, min = divmod(min, 60)
    return "%d:%02d:%02d" % (hour, min, sec)

VCqueue = []
VCtitles = []
VCmembers = []
nowPlayTitle = []
nowPlayDuration = []
nowPlayRequester = []
nowPlayThumbnail = []

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='play',
        description='Streams audio from Youtube. Syntax: w!play [keyword(s)].',
        aliases=['p'])
    async def play(self, ctx, *, search):
        """Plays audio from Youtube"""
        voiceChannel=ctx.message.author.voice.channel
        voiceChannelStr = str(voiceChannel)
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice == None:
            await ctx.send("Joining VC " + voiceChannelStr + ".")
            await voiceChannel.connect()
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        query_string = urllib.parse.urlencode({
            'search_query': search
        })
        htm_content = urllib.request.urlopen(
            'http://www.youtube.com/results?' + query_string
        )
        search_results = re.findall(r"watch\?v=(\S{11})", htm_content.read().decode())
        url = 'http://www.youtube.com/watch?v=' + search_results[0]
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            song_info = ydl.extract_info(url, download=False)
            video_title = song_info.get('title', None)
            video_length = song_info.get('duration', None)
            video_thumbnail = song_info.get('thumbnail', None)
        requester = ctx.message.author.mention
        new_video_length = convert(video_length)
        if voice.is_playing() == False:
            embed = (discord.Embed(title='Now Playing',
                                description=video_title,
                                color=discord.Color.dark_blue())
                 .add_field(name='Duration', value=new_video_length)
                 .add_field(name='Requested by', value=requester))
            embed.set_thumbnail(url=video_thumbnail)
        else:
            embed = (discord.Embed(title='Added to queue',
                                description=video_title,
                                color=discord.Color.dark_blue())
                 .add_field(name='Duration', value=new_video_length)
                 .add_field(name='Requested by', value=requester))
            embed.set_thumbnail(url=video_thumbnail)
        nowPlayTitle.append(video_title)
        nowPlayDuration.append(new_video_length)
        nowPlayRequester.append(requester)
        nowPlayThumbnail.append(video_thumbnail)
        npVar = -1
        await ctx.send(embed=embed)
        VCqueue.append(song_info["formats"][0]["url"])
        new_vctitle = (video_title + ", Duration: " + new_video_length + ", Requested by " + requester)
        VCtitles.append(new_vctitle)
        while voice != None:
            global VCleave
            if VCleave == 69420:
                global VCautoleave
                VCautoleave = 0
                VCleave = 0
                break
            if voice.is_playing():
                VCautoleave = 0
                await asyncio.sleep(1)
            else:
                if voice.is_paused():
                    VCautoleave = 0
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(3)
                    VCautoleave += 3
                    if VCautoleave == 900:
                        await voice.disconnect()
                        VCleave = 69420
                        voiceChannel=ctx.message.author.voice.channel
                        voiceChannelStr = str(voiceChannel)
                        VCqueue.clear()
                        VCtitles.clear()
                        nowPlayTitle.clear()
                        nowPlayDuration.clear()
                        nowPlayRequester.clear()
                        nowPlayThumbnail.clear()
                        await ctx.send("Left channel " + voiceChannelStr + ".")
                    VClength = len(VCqueue)
                    if VClength > 0:
                        VCautoleave = 0
                        voice.play(discord.FFmpegPCMAudio(VCqueue[0], **FFMPEG_OPTIONS))
                        VCqueue.pop(0)
                        VCtitles.pop(0)
                        npVar +=1
                        if npVar >= 1:
                            nowPlayTitle.pop(0)
                            nowPlayDuration.pop(0)
                            nowPlayRequester.pop(0)
                            nowPlayThumbnail.pop(0)
        else:
            return

    @commands.command(
        name='clear',
        description='Clears the queue.')
    async def clear(self, ctx):
        """Clears the queue"""
        global VCautoleave
        VCautoleave = 0
        VCqueue.clear()
        VCtitles.clear()
        nowPlayTitle.clear()
        nowPlayDuration.clear()
        nowPlayRequester.clear()
        nowPlayThumbnail.clear()
        await ctx.send("Queue successfully cleared.")
    
    @commands.command(
        name='pause',
        description='Pauses the music player.')
    async def pause(self, ctx):
        """Pauses the music player"""
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
            await ctx.send("Paused the music player.")
            global VCautoleave
            VCautoleave = 0
        else:
            await ctx.send("Currently no audio is playing.")
            VCautoleave = 0

    @commands.command(
        name='resume',
        description='Resumes the music player.')
    async def resume(self, ctx):
        """Resumes a paused music player."""
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_paused():
            voice.resume()
            await ctx.send("Resumed the music player.")
            global VCautoleave
            VCautoleave = 0
        else:
            await ctx.send("The audio is not paused.")
            global VCautoleave
            VCautoleave = 0

    @commands.command(
        name='skip',
        description='Skips the current song.')
    async def stop(self, ctx):
        """Annoy your friends by skipping their favourite songs!"""
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        global VCautoleave
        VCautoleave = 0
        voice.stop()
        await ctx.send("Skipped the current track.")

    @commands.command(
        name='queue',
        description='Shows contents of queue (excluding currently playing).')
    async def queue(self, ctx):
        """Shows the queue (minus the currently playing. That's another command.)"""
        global VCautoleave
        VCautoleave = 0
        user = ctx.message.author
        pfp = user.avatar_url
        list_length = len(VCtitles)
        voiceChannel=ctx.message.author.voice.channel
        embed = discord.Embed(title='Queue for {}'.format(voiceChannel),color=discord.Color.dark_blue())
        embed.add_field(name="Up Next:", value="-", inline=False)
        for i in range(list_length):
            embed.add_field(name=i+1, value=VCtitles[i])
        embed.set_author(name=user, icon_url=pfp)
        await ctx.send(embed=embed)

    @commands.command(
        name='nowplaying',
        description='Shows the currently playing song.')
    async def nowplaying(self, ctx):
        """Shows the currently playing song. Even though you should know what it is already."""
        global VCautoleave
        VCautoleave = 0
        title = nowPlayTitle[0]
        length = nowPlayDuration[0]
        requester = nowPlayRequester[0]
        thumbnail = nowPlayThumbnail[0]
        embed = discord.Embed(title='Now Playing', description=title, color=discord.Color.dark_blue())
        embed.add_field(name='Duration', value=length)
        embed.add_field(name='Requested by', value=requester)
        embed.set_thumbnail(url=thumbnail)
        await ctx.send(embed=embed)

    @commands.command(
        name='leave',
        description='Leaves the current voice chat.',
        aliases=['byebye'])
    async def leave(self, ctx):
        """Goodbye, old friend. And may the force be with you, always."""
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_connected():
            await voice.disconnect()
            global VCautoleave
            VCautoleave = 0
            global VCleave
            VCleave = 69420
            voiceChannel=ctx.message.author.voice.channel
            voiceChannelStr = str(voiceChannel)
            VCqueue.clear()
            VCtitles.clear()
            nowPlayTitle.clear()
            nowPlayDuration.clear()
            nowPlayRequester.clear()
            nowPlayThumbnail.clear()
            await ctx.send("Left channel " + voiceChannelStr + ".")
        else:
            await ctx.send("The bot is not connected to a voice channel.")

    @commands.command(
        name='palpcrack',
        description='In OrDeR tO eNsUrE tHe SeCuRiTy, AnD cOnTiNuInG sTaBiLiTy,')
    async def palpcrack(self, ctx):
        """Darth Sidious.exe is not responding"""
        global VCautoleave
        VCautoleave = 0
        voiceChannel=ctx.message.author.voice.channel
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice == None:
            await voiceChannel.connect()
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_playing() == True:
            VCqueue.append("palpcrack.mp3")
            await ctx.send("Added this song to the queue.")
        else:
            voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
            voice.play(discord.FFmpegPCMAudio("palpcrack.mp3"))

    @commands.command(
        name='bluegletranslate',
        description="I'm blue, da ba dee da ba die")
    async def bluegletranslate(self, ctx):
        """Google Translate sings the hit 90s song I'm Blue by Eiffel 65."""
        global VCautoleave
        VCautoleave = 0
        voiceChannel=ctx.message.author.voice.channel
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice == None:
            await voiceChannel.connect()
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_playing() == True:
            VCqueue.append("bluetranslate.mp3")
            await ctx.send("Added this song to the queue.")
        else:
            voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
            voice.play(discord.FFmpegPCMAudio("bluetranslate.mp3"))

    @commands.command(
        name='rickroll',
        description='You know the rules, and so do I...')
    async def rickRoll(self, ctx):
        """You know the rules, and so do I..."""
        global VCautoleave
        VCautoleave = 0
        voiceChannel=ctx.message.author.voice.channel
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice == None:
            await voiceChannel.connect()
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_playing() == True:
            VCqueue.append("rickroll.mp3")
            await ctx.send("Added this song to the queue.")
        else:
            voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
            voice.play(discord.FFmpegPCMAudio("rickroll.mp3"))

    @commands.command(
        name='revengetranslate',
        description='So we back in the mine...')
    async def revengetranslate(self, ctx):
        """Google Translate becomes an epic Minecraft Gamer and kills Technoblade"""
        global VCautoleave
        VCautoleave = 0
        voiceChannel=ctx.message.author.voice.channel
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice == None:
            await voiceChannel.connect()
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_playing() == True:
            VCqueue.append("revengeTranslate.mp3")
            await ctx.send("Added this song to the queue.")
        else:
            voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
            voice.play(discord.FFmpegPCMAudio("revengeTranslate.mp3"))

    @commands.command(
        name='itsnouse',
        description='TAKE THIS!')
    async def itsnouse(self, ctx):
        """Silver is my favourite Sonic character, and deserves to be here."""
        global VCautoleave
        VCautoleave = 0
        voiceChannel=ctx.message.author.voice.channel
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice == None:
            await voiceChannel.connect()
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_playing() == True:
            VCqueue.append("itisofnovalue.mp3")
            await ctx.send("Added this song to the queue.")
        else:
            voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
            voice.play(discord.FFmpegPCMAudio("itisofnovalue.mp3"))
            await asyncio.sleep(3)
            await voice.disconnect()
    
def setup(bot):
    bot.add_cog(Music(bot))
