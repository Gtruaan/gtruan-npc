import discord
import requests

"""
Usage of numberfact
"""
def error_embed(error_text='', footer_text=''):
    embed = discord.Embed(color=0xad0000)
    embed.add_field(name="Whoops!", value=error_text, inline=False)
    embed.set_footer(text=footer_text)
    return embed

def fact_embed(number=0, fact_text=''):
    embed=discord.Embed(color=0x5fb2f2)
    embed.add_field(name=f"An interesting fact about {number}...", 
    value=f"Did you know that {fact_text}?", inline=False
    )
    embed.set_footer(
    text='This fact was generated using numbersapi (http://numbersapi.com/)'
    )
    return embed

def get_num_fact(number=0):
    default_text = ("This number is kinda boring?... " +
    "Maybe **you** could discover something interesting!")
    response = requests.get(f"http://numbersapi.com/{number}?default={default_text}")
    
    if response.status_code != 200:
        return None
    return response.text

"""
Game invites
"""
def terraria_embed(user=None, target=None):
    if user is not None and target is not None:
        embed=discord.Embed(title=f"Hey {target.name}, wanna play Terraria with" + 
        f" {user.name}?", description="It's gonna be fun!", color=0x74aa7a)
        embed.set_author(name=f"{user.name} says:", icon_url=f"{user.avatar_url}")
        embed.set_image(url=
        "https://icon-library.com/images/terraria-icon/terraria-icon-28.jpg")
        embed.set_footer(text="You can't block these kinds of messages (yet)")
        return embed

def valorant_embed(user=None, target=None):
    if user is not None and target is not None:
        embed=discord.Embed(title=f"Hey {target.name}, wanna play Valorant with" 
        + f"{user.name}?", description="It's gonna be fun!", color=0xd1593f)
        embed.set_author(name=f"{user.name} says:", icon_url=f"{user.avatar_url}")
        embed.set_image(url="https://img.icons8.com/color/480/valorant.png")
        embed.set_footer(text="You can't block these kinds of messages (yet)")
        return embed