# Work with Python 3.6
# -*- coding: iso-8859-1 -*-
import discord
import json
from discord.ext import commands
import os
import time

client =  commands.Bot(command_prefix='!')

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
            

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    global oldtime

@client.command()
async def lidl(ctx):
    await ctx.send('Gde stanuje svezina i zivotna vedrina...U Lidlu, u Lidlu')

@client.command()
async def akcije(ctx):
    await ctx.send('https://www.lidl.rs/ponude-i-akcije')

@client.command()
async def stakupiti(ctx):
    responses = [
        'Svezi cevapi',
        'Pomorandze',
        'Mleko',
        'Kaktusi',
        'Krofna sa punjenjem od kajsije',
        'Krastavac',

                ]
    await ctx.send('Odgovor: {random.choice(responses)}')

client.run('OTMzNjY1OTY4NDI3Nzc4MDk5.Yek2MQ.CqKR2EMHnAdqGnJi0RmzlTg2X88')