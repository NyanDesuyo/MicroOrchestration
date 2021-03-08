import os
from dotenv import load_dotenv, find_dotenv
from pathlib import Path

import discord
from discord.ext import commands, tasks

from pymongo import MongoClient
clientMongo = MongoClient(os.getenv('DB_CONNECT'))
database = clientMongo['micro_orchestration']

load_dotenv(find_dotenv())


client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(" '.' for commands"), status=discord.Status.online)
    print('Logged in as {0.user}'.format(client))


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send('Load: {0}'.format(extension))


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send('Unload: {0}'.format(extension))


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send('{0} Reloaded'.format(extension))

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command used.')


client.run(os.getenv('TOKEN'))
