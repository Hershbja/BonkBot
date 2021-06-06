import discord
import config
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if (message.author.id == 474033385279586332) and (message.channel.id == 834872545307656222):
        await message.add_reaction(":bonk:831668953872859206")

    if (message.author.id == 129455976658108416):
        await message.add_reaction(":kitty:851186465655226418")
        
        
        
client.run(config.token)