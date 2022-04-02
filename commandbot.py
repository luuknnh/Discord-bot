import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

from functions import get_quote

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command()
async def punch(ctx, arg):
    """
    This command Punches a name after the command

    Args:
        ctx (_type_): _description_
        arg (_type_): _description_
    """
    
    await ctx.send(f'Punched {arg}')
 
    
@bot.command()
async def info(ctx):
    
    
    await ctx.send(ctx.guild)
    await ctx.send(ctx.author)
    await ctx.send(ctx.message.id)


@bot.command()
async def quote(ctx):
    """
    Send a random quote
    """
    quote = get_quote() 
    await ctx.send(quote)
     
     
     
     
if __name__ == "__main__":
    bot.run(TOKEN)