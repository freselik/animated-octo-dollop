import random
import discord
from discord.ext import commands

BOT_PREFIX = ("^", "?")
TOKEN = "NTcxMzYzNDQ0NzQyMTYwMzg0.XMMp6Q.7IPG02np67wQ-r_WCXAoiBzr6BY"
# client = discord.Client()
client = commands.Bot(command_prefix=BOT_PREFIX)



@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="^help, ?help"))
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('^hello'):
        await message.channel.send('Hello!')
# Tablica z slowkami random pull a trigger

    nigger = [
        'Kill a nigger! :man_with_turban::skin-tone-5: :gun: ',
        'Kill a nigger! :boy::skin-tone-5: :gun: ',
        'Kill a nigger! :girl::skin-tone-5: :gun: ',
        'Kill a nigger! :woman::skin-tone-5: :gun: ',
        'Kill a nigger! :older_man::skin-tone-5: :gun: ',
        'Kill a nigger! :man::skin-tone-5: :gun: ',
        'Kill a nigger! :pregnant_woman::skin-tone-5: :gun: ',
        'Kill a nigger! ' + '{0.author.mention}'.format(message) + ' :gun:',
    ]
    if message.content.startswith('pull a trigger'):
        await message.channel.send(random.choice(nigger))

    if message.content.startswith('^best'):
        await message.channel.send('{0.author.mention}'.format(message) + ' is the best!!')

client.run(str(os.environ.get('NTcxMzYzNDQ0NzQyMTYwMzg0.XMMp6Q.7IPG02np67wQ-r_WCXAoiBzr6BY')))
