import random
import time
from discord.ext import commands
import discord
import datetime
TOKEN = ""
bot = commands.Bot(command_prefix="!")
number = [1, 2, 3]
choice = 0
@bot.event
async def on_ready():
    print(f'{bot.user} successfully logged in!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if 'hello' in message.content.lower() or 'hola' in message.content.lower() or 'hey' in message.content.lower():
        await message.channel.send("Hello there!")
    if 'fun' in message.content.lower() or 'lol' in message.content.lower() or 'lmao' in message.content.lower():
        choice = random.choice(number)
        if choice == 1:
            await message.channel.send("Tee-hee 🤭")
        if choice == 2:
            await message.channel.send("Rehehe 🤭")
        if choice == 3:
            await message.channel.send("Big funny 😆")
    if 'try' in message.content.lower():
        await message.channel.send("Don't try it!")
    if 'high' in message.content.lower():
        await message.channel.send("I have the high ground!")
    if 'child' in message.content.lower() or 'infant' in message.content.lower():
        choice = random.choice(number)
        if choice == 1 or choice == 2:
            await message.channel.send("https://thumbs.gfycat.com/FewSnappyCob-max-1mb.gif")
            await message.channel.send("Tee-hee 🤭")
        if choice == 3:
            await message.channel.send("I am sorry for my past sins")
            await message.add_reaction('☹')
    choice = random.choice(number)
    if 'bird' in message.content.lower() and 'biggest' in message.content.lower():
        if choice == 1:
            await message.channel.send("İ̷̺ ̷̮̽A̷̘̐M̶͕̊ ̸̒ͅB̶͕̈I̸̭̋G̵̗͒G̶͖͒E̸̥̓S̴̳̀T̷̳̎ ̷͖͋B̴͚̏I̸̚ͅR̵̫̿D̴̲̎")
            with open('Cawcaw.jpg', 'rb') as f:
                picture = discord.File(f)
            await message.channel.send(file=picture)
            f.close()
            choice = 0
        if choice == 2 or choice == 3:
            await message.channel.send("Literally me:")
            await message.channel.send("https://media.tenor.com/4EaC523qoQkAAAAC/big-bird-door.gif")
            choice = 0
    if 'bird' in message.content.lower() or 'ostrich' in message.content.lower():
        if choice == 1 or choice == 2:
            await message.channel.send("So yeah cawcaw I'm an ostrich")
        if choice == 3:
            with open('Cawcaw.jpg', 'rb') as f:
                picture = discord.File(f)
            await message.channel.send(file=picture)
            f.close()
    if 'good bot' in message.content.lower():
        choice = random.choice(number)
        if choice == 1:
            await message.channel.send("Thank you master 🥰")
        if choice == 2:
            await message.add_reaction('😚')
        if choice == 3:
            await message.channel.send("I've been a good boy!")
            await message.add_reaction('😎')
    if 'chees' in message.content.lower():
        choice = random.randrange(1,3)
        if choice == 1 or choice == 2:
            await message.channel.send("I love cheese")
        if choice == 2:
            await message.add_reaction('🧀')
    if 'crue' in message.content.lower() and 'thank' in message.content.lower():
        choice = random.randrange(1, 3)
        if choice == 1:
            await message.channel.send("You're welcome bro")
        if choice == 2:
            await message.channel.send("Anytime man")
        if choice == 3:
            await message.channel.send("No problem")

bot.run(TOKEN)
