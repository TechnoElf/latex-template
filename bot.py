# boot.py
import os
import glob

import discord
from discord.message import Attachment

TOKEN = 'NzY3MDA0NjYyNzIxMDE5OTA1.X4rmwQ.kOcZMd5nx8KYLmUVRDK3MpaU1h0'
GUILD = 'EI TUM 2020 :*'

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    guild = discord.utils.get(client.guilds, name=GUILD)
    channel = discord.utils.get(guild.text_channels, name="korrekturen")
    pdf_file = glob.glob("*.pdf").pop(0)
    with open(pdf_file, 'rb') as fp:
        await channel.send(file=discord.File(fp, glob.glob(pdf_file).pop(0)))
    await client.close()


client.run(TOKEN)

'''
# client.user
# guild.name
# guild.id
# guild.members
# guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
# guild = discord.utils.get(client.guilds, name=GUILD)

@client.event ODER
class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
client = CustomClient()

@client.event
async def on_member_join(member):
    await member.create_dm()  # Waiting for execution of subroutines before continuing with "await"
    await member.dm_channel.send("Hallo")
'''
