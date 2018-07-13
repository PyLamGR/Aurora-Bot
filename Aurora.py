import logging
from discord.ext import commands
from discord import Game
from configs import conf, lang

extensions = ['music', 'members', 'rng']


# Setup Logging
try:
    logger = logging.getLogger()
    logger.setLevel(conf['logging']['level'])
    handler = logging.FileHandler(conf['logging']['file'], encoding='utf-8')
    handler.setFormatter(logging.Formatter('{asctime}:{levelname}:{name}:{message}', style='{'))
    logger.addHandler(handler)
except Exception as e:
    exc = '{}: {}'.format(type(e).__name__, e)
    print('Failed to load configuration file {}\n{}'.format(conf['logging']['file'], exc))

bot = commands.Bot(command_prefix=conf['prefix'], description=conf['description'])


@bot.event
async def on_ready():
    print("Aurora is ready for action!\n"
          "Logged in as: \n"
          " Username: {0} \n"
          " UID: {1} \n"
          "----------------------------\n"
          "{2}"
          .format(bot.user.name, bot.user.id, conf['description']))
    if conf['presence']:
        await bot.change_presence(game=Game(name=conf['presence']))


@bot.command()
async def load(extension_name: str):
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("{} loaded.".format(extension_name))


@bot.command()
async def unload(extension_name: str):
    """Unloads an extension."""
    bot.unlo1ad_extension(extension_name)
    await bot.say("{} unloaded.".format(extension_name))


if __name__ == "__main__":


    for extension in extensions:
        # try:
        bot.load_extension('extensions.'+extension)
        # except Exception as e:
        #     exc = '{}: {}'.format(type(e).__name__, e)
        #     print('Failed to load extension {}\n{}'.format(extension, exc))

    bot.run(conf['token'], bot=True, reconnect=True)
