import os
import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    print("initialized!")

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
    
@client.event
async def on_reaction_add(reaction, user):
    message = reaction.message
    channel = message.channel
    if user.id == message.author.id:
        await channel.send("thog not let you star own post, " + message.author.mention)
        await message.remove_reaction("⭐", user)
        return
    if reaction.emoji == "⭐":
        author = message.author
        newchannel = client.get_channel(932805793730941008)
        await newchannel.send(message.content + " (by " + message.author.mention + ")")

client.run(TOKEN)
