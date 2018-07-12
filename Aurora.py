import json
import logging
import discord
import random

from discord.ext import commands

# from discord import NotFound, HTTPException

# Setup Logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.FileHandler('aurora.log', encoding='utf-8')
handler.setFormatter(logging.Formatter('{asctime}:{levelname}:{name}:{message}', style='{'))
logger.addHandler(handler)

# Load Configuration file
with open('conf.json') as fp:
    conf = json.load(fp)


bot = commands.Bot(command_prefix=conf['prefix'], description=conf['description'])


client = discord.Client()
extensions = ['rng']

all_commands = {"!hello", "!pm", "!clock", "!amiadmin", "!everyone", "!online", "!makeadmin", "!removeadmin"}


@bot.event
async def on_ready():
    print("Aurora is ready for action!\n"
          "Logged in as: \n"
          " Username: {0} \n"
          " UID: {1} \n"
          "----------------------------\n"
          "{2}"
          .format(bot.user.name, bot.user.id, conf['description']))


@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

# @bot.command()
# async def roll(dice : str):
#     """Rolls a dice in NdN format."""
#     try:
#         rolls, limit = map(int, dice.split('d'))
#     except Exception:
#         await bot.say('Format has to be in NdN!')
#         return
#
#     result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
#     await bot.say(result)


if __name__ == "__main__":
    for extension in extensions:
        try:
            bot.load_extension('extensions.'+extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    bot.run(conf['token'])
