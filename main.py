import discord
import getDog
import getCat

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    print("message-->", message)
    if message.author == client.user:
        return

    if message.content.startswith('hi'):
        await message.channel.send("what do you want?")
        if message.channel.startswith('nothing'):
            await message.channel.send("Dont waste my time then")

    if message.content.startswith('dog'):
        await message.channel.send(getDog.doggie())
    if message.content.startswith('cat'):
        await message.channel.send(getCat.Cat())


client.run('MTA1MDQ3OTI0NDEwODY0MDMwNw.GQq-Kb.2UbnHzhvRmC5HUu94BR0HeCOtqmCclV3u5OyAU')