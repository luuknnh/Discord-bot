import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import requests
import json


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(
        f'{client.user} is connected to the following guild:\n'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    
    # if message.content.startswith('quote'):
    #     quote = get_quote() 
    #     await message.channel.send(quote)
        
    # if message.content == 'punch':
    #     punch()
        
if __name__ == "__main__":
    client.run(TOKEN)
