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
     
     
@commands.has_permissions(manage_messages=True)
@bot.command()
async def poll(ctx, question, *options: str):
    """
    Make a Poll with 2 or 4 arguments
    
    Syntax = Yes or no question
                [~poll "question" "option1" "option2"] 
             4 options question
                [~poll "question" "option1" "option2" "option3" "option4"]
    """

    if len(options) == 2 and options[0] == "yes" and options[1] == "no":
        reactions = ['👍', '👎']
    else:
        reactions = ['1️⃣', '2️⃣', '3️⃣', '4️⃣' ]

    description = []
    for x, option in enumerate(options):
        description += '\n {} {}'.format(reactions[x], option)

    poll_embed = discord.Embed(title=question, color=3447003, description=''.join(description))

    react_message = await ctx.send(embed=poll_embed)

    for reaction in reactions[:len(options)]:
        await react_message.add_reaction(reaction)
     
     
     
if __name__ == "__main__":
    bot.run(TOKEN)