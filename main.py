import discord
import asyncio
from utils import param
from functions import (error_embed, fact_embed, get_num_fact, 
                    terraria_embed, valorant_embed)

# All intents set to True for future tests
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} logged in!')

    await client.change_presence(
        status=discord.Status.online, 
        activity=discord.Game(param('activity'))
        )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('numberfact'):
        try:
            number = int(message.content[10:])
        except ValueError:
            content = error_embed(
                error_text='You need to write a valid number.',
                footer_text='Example: numberfact 1729'
                )
            return await message.channel.send(embed=content)
        
        fact_text = get_num_fact(number=number)

        if not fact_text:
            content = error_embed(
                error_text='Something went wrong...',
                footer_text='Sorry :('
                )
            return await message.channel.send(embed=content)

        content = fact_embed(number=number, fact_text=fact_text)
        return await message.channel.send(embed=content)
        
    if message.content.startswith('terrariacall'):
        if not len(message.mentions):
            return await message.channel.send('You need to mention people!')
        
        try:
            for member in message.mentions:
                await member.send(embed=terraria_embed(user=message.author, 
                target=member))
        except:
            await message.channel.send('Something went wrong...')
        else:
            await message.channel.send('Invitations sent!')

    if message.content.startswith('valorantcall'):
        if not len(message.mentions):
            return await message.channel.send('You need to mention people!')
        
        try:
            for member in message.mentions:
                await member.send(embed=valorant_embed(user=message.author, 
                target=member))
        except:
            await message.channel.send('Something went wrong...')
        else:
            await message.channel.send('Invitations sent!')

    if message.content.startswith(f'count for {param("countname")} pls'):
        for i in range(1, 451):
            await message.channel.send(str(i))
            await asyncio.sleep(1)       
        

client.run(open('token.txt', 'r').read())