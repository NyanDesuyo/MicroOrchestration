import os
import discord
from discord.ext import commands


class Collections(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Loaded Collections.py')

    # Commands
    @commands.command()
    async def test(self, ctx):
        await ctx.send('test!')


def setup(client):
    client.add_cog(Collections(client))
