
import discord
from discord.ext import commands
import random
import os
from asyncio import sleep
file = open("quotes.txt", 'r')
a = file.readlines()
client = commands.Bot(command_prefix = '/')
client.remove_command('help')
@client.event
async def on_ready():
     while True:
          await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name = "/help."))

@client.command(pass_context = True)
async def gen(ctx):
        author = ctx.message.author
        await ctx.send(f'{author.mention},' + "\n" + ":point_up:" + random.choice(a))
@client.command(pass_context = True)
async def code(ctx):
        embed2 = discord.Embed(
                title = 'Нажмите, чтоб получить исходный код бота.',
                description = '***[Получить код](https://vk.com/settings?m=3)***',
                colour = discord.Colour.from_rgb(255,128,0)
                )
        await ctx.send(embed = embed2)
@client.command(pass_context = True)
async def gname(ctx):
        author = ctx.message.author
        await ctx.send(f'{author.mention},' + '\n' + 'Твоё имя и фамилия на волчьем:' + '\n' + " " + " " + " " + " " + random.choice(["Неугомонный", "Сумасшедший", "Безбашенный", "Забивной", "Мудрый", "Жирный", "Влюблённый", "Злой", "Убитый", "Бездушный"]) + " " + random.choice(["Срун", "Попрыгунчик", "Мошенник", "Тяжеловес", "Змей", "Волк", "АльфаСрун", "Носкоман", "Оффник", "Трубочист"]))
@client.command(pass_context = True)
async def help(ctx):
    embed1 = discord.Embed(
        title = '**Команды от волка:**',
        description = '**/cmd**' + '\n' + '*Выводит окно с командами.*' + '\n' + '\n' + '**/gen**' + '\n' + '***Рандомная цитата от волка, способная взорвать твой мозг.***' + '\n' + '\n' + '**/gname**' + '\n'  + '***Узнать своё имя на волчьем(Волк сам придумает).***' + '\n' + '\n' + '**/code**' + '\n' + '***Получить исходный код бота.***',
        colour = discord.Colour.from_rgb(128, 0, 255)
    )
    await ctx.send(embed=embed1)

token = os.environ.get('BOT_TOKEN')
client.run(token)
