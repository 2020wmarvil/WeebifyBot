import discord
from dotenv import load_dotenv
from pathlib import Path
import os

# ----------- Load secrets file -----------
load_dotenv(dotenv_path=Path('.env'))
BOT_TOKEN = os.getenv('BOT_TOKEN')

# ----------- Boilerplate ------------
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# ----------- Helper Functions ------------
def is_image(filename):
    return filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png") or filename.endswith(".webp")

# ----------- Client events -----------
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return
    
    if not message.attachments:
        return

    for attachment in message.attachments:
        if is_image(attachment.filename):

            image_data = await attachment.read()

            #if is_anime(image):
            #    await message.delete()
            #    message.add_reaction()
            #    # TODO: send a warning and accumulate penalty counter per user, ban after X penalties
            #else:

            await message.channel.send(content=attachment.url)

@client.event
async def on_message_edit(before: discord.Message, after: discord.Message):
    if after.author == client.user:
        return
    
    if not after.attachments:
        return
    
    await after.channel.send('You thought you could evade me???')

# ----------- Launch the bot -----------
client.run(BOT_TOKEN)