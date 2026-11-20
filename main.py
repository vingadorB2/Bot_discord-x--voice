import os
import discord
from discord.ext import commands
import requests
import pyttsx3

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print("Bot online")

    for servidor in bot.guilds:
        canal = servidor.system_channel

        if canal is not None:
            await canal.send("Bot ligado!")

@bot.command()
async def start(ctx):
    await ctx.send("bem vindo!")

def get_fact():
    url = "https://uselessfacts.jsph.pl/random.json"

    response = requests.get(url, timeout=10)

    # Útil para visualizar todos os campos recebidos
    print(response.json())

    if response.status_code != 200:
        return None

    dados = response.json()
    return dados.get("text")

def speak(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()
    
@bot.command()
async def fact(ctx):
    texto = get_fact()
    if texto:
        await ctx.send(texto)
        speak(texto)
    else:
        await ctx.send("Não foi possível buscar uma curiosidade agora.")

bot.run(os.environ["DISCORD_TOKEN"])