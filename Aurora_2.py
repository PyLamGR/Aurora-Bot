import discord
import asyncio
from discord import HTTPException,NotFound

client = discord.Client()
all_commands = {"!hello", "!pm", "!clock", "!amiadmin", "!everyone", "!online", "!makeadmin", "!removeadmin"}

@client.event
async def on_ready():
    print("Bot is ready")
    print("Name:{0} ID:{1}".format(client.user.name, client.user.id))
    for channel in client.get_all_channels():
        if channel.name == "general":
            await client.send_message(client.get_channel(str(channel.id)), "Hi i'm {0} type help for extensions".format(client.user.name))
            break

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
        if message.content.startswith("!help"):
            for command in all_commands:
                await client.send_message(message.channel, command)
        elif message.content.startswith("!hello"):
            await client.send_message(message.channel, "Hello " + message.author.mention)
        elif message.content.startswith("!pm"):
            try:
                name = message.content.split(" ")[1]
                found_member = None
                for member in client.get_all_members():
                    if member.name == name:
                        found_member = member
                        break
                if found_member is None:
                    await client.send_message(message.channel, "User {0} not found".format(name))
                    return
                await client.send_message(found_member, "User {0} wanted me to pm you".format(message.author.name))
            except IndexError:
                await client.send_message(message.channel, "Invalid command.Must be : !pm namegoeshere")
        elif message.content.startswith("!amiadmin"):
            for role in message.author.roles:
                if role.permissions.administrator:
                    await client.send_message(message.channel, "You're an admin")
                    return
            await client.send_message(message.channel, "You're not an admin")
        elif message.content.startswith("!everyone"):
            for member in client.get_all_members():
                await client.send_message(message.channel, member.name)
        elif message.content.startswith("!online"):
            for member in client.get_all_members():
                if member.status == discord.Status.online:
                    await client.send_message(message.channel, member.name)
        elif message.content.startswith("!makeadmin"):
            # TODO makeadmin and removeadmin extensions raises FORBIDDEN ERROR find a way to solve it
            for role in message.author.roles:
                if role.permissions.administrator:
                    try:
                        name = message.content.split(" ")[1]
                        for member in client.get_all_members():
                            if member.name == name:
                                list_of_servers_roles = message.channel.server.roles
                                for certain_role in list_of_servers_roles:
                                    if certain_role.permissions.administrator:
                                        await client.add_roles(member, certain_role)
                    except IndexError:
                        await client.send_message(message.channel, "Invalid command.Must be : !makeadmin namegoeshere")
        elif message.content.startswith("!removeadmin"):
            pass
        elif message.content.startswith("!sendinvite"):
            # TODO doesn't work find a way to fix it
            try:
                users_id = message.content.split(" ")[1]
                try:
                    invite = await client.create_invite(destination=message.channel, temporary=False, max_uses=1)
                    try:
                        client.send_message(client.get_user_info(users_id), invite)
                    except NotFound:
                        await client.send_message(message.channel, "User with ID:{0} not found".format(users_id))
                except HTTPException:
                    await client.send_message(message.channel, "Error occurred while creating an invite")
            except IndexError:
                await client.send_message(message.channel, "Invalid command.Must be : !pm namegoeshere")
# This is where you paste your bots token:
client.run("TOKEN")
