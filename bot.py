import logging
logging.basicConfig(level=logging.INFO)
import discord
from discord.ext import commands
import asyncio
import os
import socket
import sys

website = "IP_OR_WEBDOMAIN"
des = "I check to see if the Phabricator server is online or not! Please type ping to check."
prefix = "!"
token = ""

client = commands.Bot(command_prefix=prefix)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="To Phabricator"))
    print('Connected!')

@client.command()
async def who(ctx):
    await ctx.send(des)

@client.command()    
async def ping(ctx):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    rep = os.system('ping ' + website)
    if rep == 0:
        await ctx.send('Phabricator is up!')
    else:
        await ctx.send('Phabricator is down!')

client.run("token")
