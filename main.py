# Work with Python 3.6
# -*- coding: iso-8859-1 -*-
import discord
import json
from discord.ext import commands
import os
import time

helpResponse = ['']
helpResponse.append("")
with open ("README.md", "r") as myfile:
    helpResponseTmp=myfile.readlines()
    indexCurr = 0;
    for i in range(0, len(helpResponseTmp)):
        if(len(helpResponse[indexCurr]) + len(helpResponseTmp[i]) > 1000):
            helpResponse.append(helpResponseTmp[i])
            indexCurr +=1
        else: 
            helpResponse[indexCurr] += helpResponseTmp[i]
            
client =  commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    global oldtime

client.run('OTMzNjY1OTY4NDI3Nzc4MDk5.Yek2MQ.CqKR2EMHnAdqGnJi0RmzlTg2X88')