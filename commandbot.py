import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

from functions import get_action, get_quote, get_wachttijd

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
    
@bot.command()
async def activity(ctx):
    """
    Send a random quote
    """
    act = get_action() 
    await ctx.send(act)
    
@bot.command()
async def wachttijd(ctx):
    """
    Get attractions wachttijden Efteling
    """
    main = get_wachttijd()
    print(main) 
    await ctx.send(main)
    
    
@bot.command()
async def ping(ctx):
    """
    Send a random quote
    """
    
    await ctx.send(f'Pong!')
     
     
     
     
if __name__ == "__main__":
    bot.run(TOKEN)