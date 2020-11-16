
import discord
from discord.ext import commands
import random
import os
from asyncio import sleep
file = open("quotes.txt", 'r')
from discord.ext import commands, tasks
from discord.voice_client import VoiceClient
import youtube_dl
a = file.readlines()
e = "Неугомонный", "Сумасшедший", "Безбашенный", "Забивной", "Мудрый", "Жирный", "Влюблённый", "Злой", "Убитый", "Бездушный", "Воздушный"
d = "Срун", "Попрыгунчик", "Мошенник", "Тяжеловес", "Змей", "Волк", "АльфаСрун", "Носкоман", "Оффник", "Трубочист", "Бандит", "Дебил"
client = commands.Bot(command_prefix = '/')
client.remove_command('help')
mschelp = 'join, /leave, /pause, /play, /queue, /remove,  /resume,  /stop, /view'

from random import choice

@client.command(pass_context = True)
async def help(ctx):
    embed1 = discord.Embed(
        title = '**Команды от волка:**',
        description = '**/help**' + '\n' + '*Выводит окно с командами.*' + '\n' + '\n' + '**/gen**' + '\n' + '***Рандомная цитата от волка, способная взорвать твой мозг.***' + '\n' + '\n' + '**/gname**' + '\n'  + '***Узнать своё имя на волчьем(Волк сам придумает).***' + '\n' + '\n' + '**/code**' + '\n' + '***Получить исходный код бота.***' + mschelp,
        colour = discord.Colour.from_rgb(128, 0, 255)
    )
    await ctx.send(embed=embed1)

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


client = commands.Bot(command_prefix='/')

queue = []

@client.event
async def on_ready():
    change_status.start()
    print('Bot is online!')

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='general')
    await channel.send(f'Привет, {member.mention}. Отправь `/help` для получения списка команд.')

@client.command(name='join')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("Вы должны быть подключены к голосовому каналу!")
        return
    
    else:
        channel = ctx.message.author.voice.channel

    await channel.connect()

@client.command(name='queue')
async def queue_(ctx, url):
    global queue

    queue.append(url)
    await ctx.send(f'`{url}` в очереди.')

@client.command(name='remove')
async def rem(ctx, number):
    global queue

    try:
        del(queue[int(number)])
        await ctx.send(f'В очереди `{queue}!`')
    
    except:
        await ctx.send('В очереди ничего нет или произошла ошибка.')
        
@client.command(name='play')
async def play(ctx):
    global queue

    server = ctx.message.guild
    voice_channel = server.voice_client

    async with ctx.typing():
        player = await YTDLSource.from_url(queue[0], loop=client.loop)
        voice_channel.play(player, after=lambda e: print('Произошла ошибка: %s' % e) if e else None)

    await ctx.send('**Воспроизведение** {}'.format(player.title))
    del(queue[0])

@client.command(name='pause')
async def pause(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.pause()

@client.command(name='resume')
async def resume(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.resume()

@client.command(name='view')
async def view(ctx):
    await ctx.send(f'В очереди `{queue}!`')

@client.command(name='leave')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()

@client.command(name='stop')
async def stop(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.stop()

@client.event
async def on_ready():
     while True:
          await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name = "/help."))

@client.command(pass_context = True)
async def gen(ctx):
        embed3 = discord.Embed(
                title = 'Волк произнёс великую цитату для тебя:',
                description = '_' +  random.choice(a) + '_',
                colour = discord.Colour.from_rgb(255,175,0)
                )
        await ctx.send(embed = embed3)
         
@client.command(pass_context = True)
async def code(ctx):
        embed2 = discord.Embed(
                title = 'Нажмите, чтоб получить исходный код бота.',
                description = '***[Получить код](https://youtu.be/dQw4w9WgXcQ?t=41)***',
                colour = discord.Colour.from_rgb(255,128,0)
                )
        await ctx.send(embed = embed2)
@client.command(pass_context = True)
async def gname(ctx):
        embed5 = discord.Embed(
                title = 'Волк придумал для тебя имя:',
                description = ":point_up:" + " " + random.choice(e) + " " + random.choice(d),
                colour = discord.Colour.from_rgb(220,20,60)
                )
        await ctx.send(embed = embed5)


token = os.environ.get('BOT_TOKEN')
client.run(token)
