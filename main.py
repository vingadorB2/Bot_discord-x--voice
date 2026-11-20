import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import requests
import pyttsx3
import random

load_dotenv()

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

# ------------------- funcções

def speak(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()


def get_fact():
    url = "https://uselessfacts.jsph.pl/random.json"

    response = requests.get(url, timeout=10)

    # Útil para visualizar todos os campos recebidos
    print(response.json())

    if response.status_code != 200:
        return None

    dados = response.json()
    return dados.get("text")


lista = [
        "você é uma pessoa boa!",
        "Nunca desista de seus sonhos!",
        "tudo pode naquilo que se crê",
        "a força é testada quando ela é necessária",
        "Tempos dificeis sempre vão existir, e suas vitórias também",
        "O ser humano já saiu de seu planeta e criou inteligencia aritifical, você pode ser o próximo nome!",
        "Estando pobre ou não, fraco ou não, você que decide o fim de seu rumo"]

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


@bot.command()
async def start(ctx):
    await ctx.send("bem vindo!")

    
@bot.command()
async def fact(ctx):
    texto = get_fact()
    if texto:
        await ctx.send(texto)
        speak(texto)
    else:
        await ctx.send("Não foi possível buscar uma curiosidade agora.")

token = os.getenv("DISCORD_TOKEN")

if not token:
    raise RuntimeError("Configure DISCORD_TOKEN no arquivo .env ou como variável de ambiente.")

@bot.command()
async def motivation(ctx):
    await ctx.send(random.choice(lista))

bot.run(token)