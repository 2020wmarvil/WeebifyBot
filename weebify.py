import discord
from dotenv import load_dotenv
from pathlib import Path
import os

# ----------- Load secrets file -----------
load_dotenv(dotenv_path=Path('.env'))
BOT_TOKEN = os.getenv('BOT_TOKEN')

# ----------- Boilerplate ------------
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# ----------- Client events -----------
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await message.channel.send('Hello!')

# ----------- Launch the bot -----------
client.run(BOT_TOKEN)