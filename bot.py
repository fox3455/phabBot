"""
Creator: Fox3455
======To Do======
This is the To Do list.
I will cross things off as
they are completed

To Add
-----------------
Add backup feature
Change status to reflect last backup
Add feature to start backup from discord
-----------------

Added
-----------------
Ping the server and print alive or dead
Describe what the bot is for
Changed the activity status to listening
-----------------
=================
"""

import logging
logging.basicConfig(level=logging.INFO)
import discord
from discord.ext import commands
import asyncio
import os
import socket
import sys
import subprocess
import psutil

website = "IP_OR_WEBDOMAIN"
backup = 0
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

@client.command()
async def startBackup(ctx):
    await ctx.send('feature not ready.')
    '''if backup == 0 :
        proc = subprocess.Popen(['PATH_TO_PROGRAM'], shell=True)
        psutil.Process(proc.pid)
        await ctx.send('Backup server is online and running.')
        backup = 1
    else:
        await ctx.send('Backup server already online.')'''

client.run("token")
