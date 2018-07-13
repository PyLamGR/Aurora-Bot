import time
import discord
from discord.ext import commands
import lang


class Members:
    """Management functions for members"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=['member_since'])
    async def joined(self, ctx, member: discord.Member = None):
        """Says when a member joined."""
        if member is None:
            return await self.bot.say(lang.TAG_REQUIRED)

        joined_at = member.joined_at  # TODO: Add args for simple & detailed printing
        await self.bot.say('{0.name} joined in {1}'.format(member, joined_at))
        parsed_joined_at = time.strptime(joined_at)
        print(time.strftime("%a %b %d %H:%M:%S %Y", parsed_joined_at))

    @joined.error
    async def joined_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.BadArgument):
            await self.bot.say(lang.MEMBER_NOT_FOUND)
        elif isinstance(error, discord.ext.commands.UserInputError):
            await self.bot.say("Input error")
        elif isinstance(error, discord.ext.commands.Context):
            await self.bot.say(lang.MEMBER_NOT_FOUND)
        else:
            await self.bot.say(lang.UNKNOWN_ERROR)

    @commands.group(pass_context=True)
    async def cool(self, ctx):
        """Says if a user is cool.
        In reality this just checks if a subcommand is being invoked.
        """
        if ctx.invoked_subcommand is None:
            await self.bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))

    @cool.command(name='bot')
    async def _bot(self):
        """Is the bot cool?"""
        await self.bot.say('Yes, the bot is cool.')


def setup(bot):
    bot.add_cog(Members(bot))
