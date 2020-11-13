import discord
from discord.ext import commands
import random
import
file = open("quotes.txt", 'r')
a = file.readlines()
async def on_ready():
	print('Авторизован!')
async def on_message(self,message):
        print(message)
        print('Получено сообщение')

client = commands.Bot(command_prefix = '/')
@client.command(pass_context = True)
async def gen(ctx):
        await ctx.send(random.choice(a))
        print(ctx.send)
@client.command(pass_context = True)
async def code(ctx):
        await ctx.send("Не дам код")
@client.command(pass_context = True)
async def help(ctx):
        await ctx.send('Волкодав - команды:'
                       '1 ./help - просмотр команд.'
                       '2. /gen - цитата волка.'
                       )
token = os.environ.get('BOT_TOKEN')