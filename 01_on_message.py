import discord
import random
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.WARNING)

yoda_isms = [
  'Fear is the path to the dark side. Fear leads to anger. Anger leads to hate. Hate leads to suffering',
  'Once you start down the dark path, forever will it dominate your destiny. Consume you, it will',
  'Always pass on what you have learned',
  'Patience you must have my young Padawan',
  'In a dark place we find ourselves, and a little more knowledge lights our way',
  'Death is a natural part of life. Rejoice for those around you who transform into the Force. Mourn them do not. Miss them do not. Attachment leads to jealously. The shadow of greed, that is',
  'Powerful you have become, the dark side I sense in you',
  'Train yourself to let go of everything you fear to lose',
  'Feel the force!',
  'Truly wonderful the mind of a child is',
  'Do or do not. There is no try',
  'Great warrior. Wars not make one great',
  'Size matters not. Look at me. Judge me by my size, do you? Hmm? Hmm. And well you should not. For my ally is the Force, and a powerful ally it is. Life creates it, makes it grow. Its energy surrounds us and binds us. Luminous beings are we, not this crude matter. You must feel the Force around you; here, between you, me, the tree, the rock, everywhere, yes. Even between the land and the ship',
  'The dark side clouds everything. Impossible to see the light, the future is',
  'You will find only what you bring in'
]

yoda_gifs = [
  './gifs/yoda1.gif',
  './gifs/yoda2.gif',
  './gifs/yoda3.gif',
  './gifs/yoda4.gif',
  './gifs/yoda5.gif',
  './gifs/yoda6.gif',
  './gifs/yoda7.gif',
  './gifs/yoda8.gif',
  './gifs/yoda9.gif',
  './gifs/yoda10.gif'
]

yoda_emojis = [
  '\U0001F320',
  '\U0001FA90',
  '\U0001F31F',
  '\U0001F30C',
  '\U0001F47D'
]

intents = discord.Intents(messages=True, guilds=True, reactions=True)

client = discord.Client()

@client.event
async def on_ready():
  print('Bot online... it is')

# Message is actually a dict here.
# It also stores information like author channel etc.
@client.event
async def on_message(message):
  # Need to ensure we don't cause a recursive loop with the bot
  if message.author == client.user:
    return

  if client.user.mentioned_in(message):
    print('Sending yoda gif')
    await message.channel.send(random.choice(yoda_isms))
    with open(random.choice(yoda_gifs), 'rb') as f:
      picture = discord.File(f)
      await message.channel.send(file=picture)
  else:
    print('Reacting to message!')
    await message.add_reaction(random.choice(yoda_emojis))

client.run('<DISCORD_TOKEN>')
