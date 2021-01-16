import discord
import os
import requests
import json
import random
import time
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')



@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, diceNum: int, sides: int):
    dice = []

    for _ in range(diceNum):
        dice.append(str(random.randint(1, sides)))

    await ctx.send(', '.join(dice))



@bot.command(name='start_countdown',  help='Simulates a countdown timer')
async def countDown(ctx, seconds: int, finalMessage):
    msg = await ctx.send("Time left: "+ (str)(seconds) + " seconds.")

    for x in range(1, seconds+1):
        time.sleep(1)
        await msg.edit(content = "Time left: "+ str(seconds-x) + " seconds.")

    time.sleep(1)
    await msg.edit(content = finalMessage)


    
# To run the bot
bot.run(TOKEN)