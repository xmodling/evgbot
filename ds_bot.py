# Автор скрипта - убийца (vk.com/dxxm3r)
# Скрипт написан в развлекательных целях, поэтому не нужно ничего критиковать, бот полностью готов и вряд ли будет меняться.
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
e = "Неугомонный", "Сумасшедший", "Безбашенный", "Забивной", "Мудрый", "Жирный", "Влюблённый", "Злой", "Убитый", "Бездушный", "Воздушный", "Абсолютный", "Адский", "Бешеный", "Горячий", "Хладнокровный", "Товарищ"
d = "Срун", "Попрыгунчик", "Мошенник", "Тяжеловес", "Змей", "Волк", "Альфасрун", "Носкоман", "Оффник", "Трубочист", "Бандит", "Дебил", "Ублюдок", "Бог", "Школьник", "Козёл", "Орган", "Бот", "Интеллектуал", "Мальчик"
client = commands.Bot(command_prefix = '/')
client.remove_command('help')

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='general')
    await channel.send(f'Привет, {member.mention}. Отправь `/help` для получения списка команд.')


@client.event
async def on_ready():
     while True:
          await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name = "/help."))

@client.command(pass_context = True)
async def quote(ctx):
        print(ctx)
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
                description = "***" + " " + random.choice(e) + " " + random.choice(d) + "***",
                colour = discord.Colour.from_rgb(220,20,60)
                )
        await ctx.send(embed = embed5)
@client.command(pass_context = True)
async def help(ctx):
    embed1 = discord.Embed(
        title = '**Команды от волка:**',
        description = '**/help**' + '\n' + '*Выводит окно с командами.*' + '\n' + '\n' + '**/gen**' + '\n' + '***Рандомная цитата от волка, способная взорвать твой мозг.***' + '\n' + '\n' + '**/gname**' + '\n'  + '***Узнать своё имя на волчьем(Волк сам придумает).***' + '\n' + '\n' + '**/code**' + '\n' + '***Получить исходный код бота.***',
        colour = discord.Colour.from_rgb(128, 0, 255)
    )
    await ctx.send(embed=embed1)


token = os.environ.get('BOT_TOKEN')
client.run(token)
