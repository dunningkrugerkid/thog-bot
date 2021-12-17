import os
import discord
from dotenv import load_dotenv

load_dotenv()

GUILD = os.getenv('DISCORD_GUILD')
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f"{client.user} don't caare\n"
        f"{guild.name} is pretty cool.\n"
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'List of smelly people:\n - {members}')

@client.event
async def on_message(message):
    channel = message.channel
    if message.content.startswith('thogDecide'):
        def decideFate():
            import random
            choice = random.randint(0,1)
            return choice
            
        await channel.send("thog decide your fate")
        await channel.send("thog decided this...")

        choice = decideFate()
  
        if choice: # rolled a 1
            await channel.send("thog pine for violence. where tob? we have job to do.")
        else: # rolled a 0
            await channel.send("thog dont caare about killing you")
    elif message.content.startswith('does thog care'):
        await channel.send("thog dont caare")
        
    if "pog" in message.content.lower() and "not" not in message.content.lower():
        await message.add_reaction("🇵")
        await message.add_reaction("🇴")
        await message.add_reaction("🇬")

client.run(TOKEN)
