import discord
from discord.ext import commands
from tools import anilist_req
import json
from dotenv import load_dotenv
import os 
import random 


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!nota ", intents=intents)

def load_data():
    try:
        with open('favorites.json', 'r') as f:
            data = json.load(f)


    except FileNotFoundError:
        data = {}
    return data

def save_data(data):
    with open('favorites.json', 'a+') as f:
        json.dump(data, f, indent=4)



@bot.command()
async def ping(ctx):
    await ctx.send(f'ping: `{bot.latency * 1000}`ms')

@bot.command()
async def anime(ctx, anime: str):
    if anilist_req.get_info_anime == False:
        await ctx.send(f"Results: Not Found! \n {anilist_req.get_info_anime(anime)}")
    else:
        await ctx.send(f"Maybe this is what you are looking for: https://www.anilist.co/anime/{anilist_req.get_info_anime(anime)}")

@bot.command()
async def surprise(ctx):
    await ctx.send(f"Today's Surprise https://anilist.co/anime/{random.randint(11111, 200000)}")

@bot.command()
async def helpme(ctx):
    await ctx.send(f" ### NotaAnilistBot \n *anime* : Search Anime | !nota search <anime_name> \n *ping*: Bot connection check \n *surprise*: Today your locky day! \n *user : Search user | !nota user <username>*")


@bot.command()
async def user(ctx, user: str):
    await ctx.send(f"{anilist_req.get_info_user(user)}")



load_dotenv()
TOKEN = os.getenv('TOKEN')
bot.run(TOKEN)
