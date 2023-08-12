import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

items = {
    'бумага': '2-5 месяцев',
    'банановая кожура': '2-5 недель',
    'пластиковая бутылка': '400 лет'
}    

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def decomposition(ctх, item):
    if item in items:
        time_to_decompose = items[item]
        await ctх.send(f'Предмет {item} разлагается примерно {time_to_decompose}')
    else:
        await ctх.send('Про такой предмет ещё нет информации')

@bot.command()
async def sort(ctх, item):
    if item == 'батарейки':
        await ctх.send('отдать на переработку')
    elif item == 'стекло':
        await ctх.send('отдать на переработку, можно выбросить в специальную урну')
    else:
        await ctх.send('пока не известно, что делать с этим предметом')    

bot.run('MTEzMjI3NzgwMjgxMzY0MDcxNA.GzFjZt.Bj-Jyth6USbVLMQPWzByOuHB10kSZhb7Mk6vO4')
