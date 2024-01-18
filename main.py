import discord, random, requests, os
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            file_name = file.filename
            file_url = file.url
            await file.save(f'{file_name}')
            await ctx.send(f'file disimpan atas nama {file_name}')
            hasil = get_class('keras_model.h5','labels.txt', file_name)

            if hasil[0] == 'merpati\n' and hasil[1] >= 0.6:
                await ctx.send("ini adalah buwung merpati")
            elif hasil[0] == 'pipit\n' and hasil[1] >= 0.6:
                await ctx.send("ini adalah buwung pipit")
            else:
                await ctx.send("ini burung apa")
    else:
        await ctx.send('ANDA TIDAK MENGIRIM APAPUN :((')

bot.run("MTEzNDEwNDYyMDU4MzYyNDgyNw.GOj6IB.Gg1gcdMArd0bfCcr4M9ta0kYzNbBoV3lj9eawk")

