#!/usr/bin/python3.5

"""
	    D-Popo 0.0.1
	    by ki2ne [6/27/2016 00:02]

        D-popo is a Discord bot that is a part of the Iktoslavistan project that will be used for law enforcement.
        As the name suggests, it's "the popo [police]".
        
        It's still a WIP though.

	
"""

import discord, time, datetime
from discord.ext import commands
import aiomysql, asyncio, json

"""
    Predefined Stuff
"""

"""
    End Predefined Stuff
"""


dpol = commands.Bot(command_prefix="%")
loop = asyncio.get_event_loop()

with open("./login.json", 'r') as settings_file:
    settings = json.loads(settings_file.read())

# IEPD, reporting for duty!
@dpol.event
async def on_ready():
    print("D-Popo is online. Start Time: %s" % time.strftime("%Y-%m-%d %H:%M:%S"))
    print('Linked to Discord - User: %s [%s]' % (dpol.user.name,dpol.user.id))
    print('------')


#ctx is for context

@dpol.command(pass_context = True)
async def records(ctx, user:discord.Member):
    asql = await aiomysql.connect(settings["sqlhost"], port, settings["sqluser"], settings["sqlpassword"], settings["sqldb"], loop = loop)

@dpol.command(pass_context = True)
async def reports(ctx, action:str="lookup", rtype:str = "complaint", description:str = "", handler:discord.Member = ctx.message.author):
    if action == "lookup":
        # look up case reports.
        if rtype == "complaint":
        elif rtype == "crime":
        else:
            # look up by case number.
    elif action == "file":
        # file a new case report.
        if rtype == "complaint":
        elif rtype == "crime":
        else:
            # complain.
            await dpol.say("I cannot file a new report with that information.")
    elif action == "close":
        # close a case report.
    elif action == "open":
        # open or reopen a closed report.


# Replace token with your own development token.
dpol.run('token')

