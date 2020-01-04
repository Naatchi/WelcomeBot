import discord
import random
import asyncio
from discord.ext import commands

#I can move it over to @client.command() but thats for later
#i didnt do this because im lazy lol

client = discord.Client()


@client.event
async def on_ready():
    print('[LOGIN]{0.user}'.format(client))
    print('[READY]')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("?help"):
        await message.channel.send("Use `?ip` to get the ip!")

    if message.content.startswith("good bot"):
        c = [
            ":)",
            "Yay!",
            "Thanks!",
            "Beep Boop!",
            "*Happy Bot Sounds*"
        ]
        await message.channel.send(random.choice(c))

    if message.content.startswith("?ip"): #testing embeds idk in final build?
        embed = discord.Embed(Title='TEST', description='Build Server:', color=0x00ff00)
        embed.add_field(name='build.mineinabyss.ga', value='Survival Server', inline=False)
        embed.add_field(name="survive.mineinabyss.ga", value="Make sure to be on 1.13.2!", inline=False)
        await message.channel.send(message.channel, embed=embed)
      
@client.event #member join stuff
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name = 'general')
    d = ["Welcome",
        "Welcome!",
        "welcome!",
        "Hello There",
        "hello there",
            "Howdy",
            "howdy",
            "Hello @LoneReborn, Lord of odd jobs ! Welcome to the Abyss!"
         ]
    await channel.send(random.choice(d))
client.run("TOKEN")