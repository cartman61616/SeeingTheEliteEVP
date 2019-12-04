import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='!', description='EVP Bot for Seeing The Elite')

tooSweetList = ['https://tenor.com/view/too-sweet-gif-9536867',
                'https://tenor.com/view/too_sweet-kenny_omega-young_bucks-red_shoes-gif-9909622',
                'https://tenor.com/view/adam-cole-nxt-bulletclub-baybay-adam-gif-12121153',
                'https://tenor.com/view/bullet-club-too-sweet-wrestlers-gif-11235479']


@bot.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = 'Welcome {0.mention}! How did you find our show?'.format(member)
        await guild.system_channel.send(to_send)


@bot.command(description='Give us a Tooooo Sweet')
async def toosweet(ctx):
    await ctx.send(random.choice(tooSweetList))


@bot.command(description='A hug from the best friends to a best friend')
async def hug(ctx):
    await ctx.send('https://tenor.com/view/aew-trent-beretta-chuck-taylor-orange-cassidy-best-friends-gif-14962323')


@bot.command()
async def lechampion(ctx):
    await ctx.send('https://tenor.com/view/aew-chris-jericho-bubbly-gif-15099023')

bot.run()

