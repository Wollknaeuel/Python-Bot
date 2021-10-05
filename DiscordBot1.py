import discord


import random

import datetime

from discord import Member
from discord.utils import get

import asyncio

import time

client = discord.Client()

@client.event
async def on_ready():
    print('Ich bin da mein Gebieter, ich bin {}'.format(client.user.name))
    client.loop.create_task(status_task())


#Status Anzeige welches spiel gespielt wird.
async def status_task():
    while True:
     await client.change_presence(activity=discord.Game('FF14'), status=discord.Status.online)
     await asyncio.sleep(5)
     await client.change_presence(activity=discord.Game('My Little Pony :D'), status=discord.Status.online)
     await asyncio.sleep(5)


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if 'Sklave' in message.content:
        await message.channel.send('Ja Herr, zu diensten')
    if message.content.startswith('!userinfo'):
        args = message.content.split(' ')
        if len(args) == 2:
            member: Member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
            if member:
                embed = discord.embed(title='Userinfo für {}'.format(member.name),
                                      description='Dies ist eine Userinfo für den User {}'.format(member.mention),
                                      color=0x22a7f0)
                embed.add_field(name='Server beigetreten', value=member.joined_at.strftime('%d/%m/%Y, %H:%M'),
                                inline=True)
                embed.add_field(name='Discord beigetreten', value=member.created_at.strftime('%d/%m/%Y, %H:%M'),
                                inline=True)
                rollen = ''
                for role in member.roles:
                    if not role.is_default():
                        rollen += '{} \r\n'.format(role.mention)
                if rollen:
                    embed.add_field(name='Rollen', value=rollen, inline=True)
                embed.set_thumbnail(url=member.avatar_url)
                embed.set_footer(text='Ich bin ein EmbedFooter.')
                await message.channel.send(embed=embed)

        if message.content.startswith('Moin'):
            await message.channel.send('Willkommen werter Gast.')
        if message.content.startswith('Hallo'):
            await message.channel.send('Willkommen werter Gast.')
        if message.content.startswith('Malzeit'):
            await message.channel.send('Willkommen werter Gast.')



client.run("hier das Token")
