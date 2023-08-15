import discord
# import os
import things

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('{0.user} is ready and surfing the market'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$moon'):
        await message.channel.send('to the moon!')

client.run(things.CLAVIS)