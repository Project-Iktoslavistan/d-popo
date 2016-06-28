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

settings_file = open("./login.json", 'r')
settings = json.loads(settings_file.read())
settings_file.close()

# Link Start!
@dpol.event
async def on_ready():
    print("D-Popo is online. Start Time: %s" % time.strftime("%Y-%m-%d %H:%M:%S"))
    print('Linked to Discord - User: %s [%s]' % (dpol.user.name,dpol.user.id))
    print('------')


#ctx is for context
@dpol.command(pass_context=True)
async def records(ctx, user:discord.Member):
    
    asql = await aiomysql.connect(settings["sqlhost"], port, settings["sqluser"], settings["sqlpassword"], settings["sqldb"], loop = loop)
    
    
  

# Replace token with your own development token.
dpol.run('token')

