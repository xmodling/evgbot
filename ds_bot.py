
import discord
from discord.ext import commands
import random
import os

file = open("quotes.txt", 'r')
a = file.readlines()
client = commands.Bot(command_prefix = '/')
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
async def cmd(ctx):
        author = ctx.message.author
        await ctx.send(f'{author.mention},' + "\n" + " " + "Команды бандита:" + "\n" + "\n" + " " + " " + "/gen - Рандомная цитата, способная взорвать твой мозг." + "\n" + "\n" + " " + " " + "/code - Получить код бота." + "\n" + "\n" + " " + " " + "/gname - Получить имя от волка(он сам придумал)" + "\n" + "\n" + " " + " " + "/cmd - Список команд.")
token = os.environ.get('BOT_TOKEN')
client.run(token)
