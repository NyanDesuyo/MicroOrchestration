import discord
from discord.ext import commands

# import serial
# ser = serial.Serial('/dev/ttyACM0', 9600)  # making dynamic port??


class Arduino(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Loaded Arduino.py')

    @commands.command()
    async def turn_on(self, ctx):
        await ctx.send('Turn on')

    @commands.command()
    async def turn_off(self, ctx):
        await ctx.send('Turn off')

    @commands.command()
    async def status(self, ctx):
        await ctx.send('Status...')
        # TODO
        # return stats from something...
        # - termometer DT11
        # - water

    # TODO
    # make Command for read status from sensor
    # make Command for Trigger events
    #


def setup(client):
    client.add_cog(Arduino(client))
