
import discord
from discord.ext import commands
import random
import os
from asyncio import sleep
file = open("quotes.txt", 'r')
a = file.readlines()
client = commands.Bot(command_prefix = '/')
@client.event
async def on_ready():
     while True:
          await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name = "/cmd."))
@client.command(pass_context = True)
async def gen(ctx):
        author = ctx.message.author
        await ctx.send(f'{author.mention},' + "\n" + ":point_up:" + random.choice(a))
@client.command(pass_context = True)
async def code(ctx):
        author = ctx.message.author
        await ctx.send(f'{author.mention},' + "\n" + "Не дам код")
@client.command(pass_context = True)
async def gname(ctx):
        author = ctx.message.author
        await ctx.send(f'{author.mention},' + '\n' + 'Твоё имя и фамилия на волчьем:' + '\n' + " " + " " + " " + " " + random.choice(["Неугомонный", "Сумасшедший", "Безбашенный", "Забивной", "Мудрый", "Жирный", "Влюблённый", "Злой", "Убитый", "Бездушный"]) + " " + random.choice(["Срун", "Попрыгунчик", "Мошенник", "Тяжеловес", "Змей", "Волк", "АльфаСрун", "Носкоман", "Оффник", "Трубочист"]))
@client.command(pass_context = True)
async def displayembed(ctx):
    embed1 = discord.Embed(
        title = '***Команды бота-бандита:***',
        description = '**/gen**' + '\n' + '*Рандомная цитата от волка.*' + '\n' + '\n' + '**/gname**' + '\n' + '\n' + '*Узнать своё имя на волчьем.*' + '\n' + '\n' + '**/code**' + '\n' + '\n' + '*Получить исходнык код бота.*',
        colour = discord.Colour.from_rgb(128, 0, 255)
    )
    await ctx.send(embed=embed1)
@client.command(pass_context = True)
async def cmd(ctx):
        author = ctx.message.author
        await ctx.send(f'{author.mention},' + "\n" + " " + "Команды бандита:" + "\n" + "\n" + " " + " " + "/gen - Рандомная цитата от волка, способная взорвать твой мозг, будь осторожен, я предупредил." + "\n" + "\n" + " " + " " + "/code - Получить код бота." + "\n" + "\n" + " " + " " + "/gname - Получить имя от волка(он сам придумал)" + "\n" + "\n" + " " + " " + "/cmd - Список команд.")
token = os.environ.get('BOT_TOKEN')
client.run(token)
