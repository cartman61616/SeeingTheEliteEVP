import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='!', description='EVP Bot for Seeing The Elite')

tooSweetList = ['https://tenor.com/view/too-sweet-gif-9536867',
                'https://tenor.com/view/too_sweet-kenny_omega-young_bucks-red_shoes-gif-9909622',
                'https://tenor.com/view/adam-cole-nxt-bulletclub-baybay-adam-gif-12121153',
                'https://tenor.com/view/bullet-club-too-sweet-wrestlers-gif-11235479']

orangeList = [
    'https://tenor.com/view/aew-best-friends-gobble-orange-cassidy-gif-15679150',
    'https://tenor.com/view/orange-cassidy-aew-thumbs-up-gif-15305280'
]

moxList = [
    'https://tenor.com/view/aew-wrestling-ring-gif-14861128',
    'https://tenor.com/view/aew-jon-moxley-smiling-happy-surprised-gif-15520949'
]

zoidbergList = [
    'https://tenor.com/view/zoidberg-laughing-evil-evil-laugh-wiggle-gif-4892702',
    'https://tenor.com/view/zoidberg-futurama-gif-9244526',
    'https://tenor.com/view/zoidberg-futurama-hooray-me-selflove-gif-4732893'
]

keanuList = [
    'https://tenor.com/view/keanu-whoa-gif-14216217',
    'https://tenor.com/view/keanu-reeves-whoa-wow-gif-14148374',
    'https://tenor.com/view/keanu-glare-gif-12443545'
]

owenList = [
    'https://tenor.com/view/owenwilsonwow-wow-ohwow-owen-wilson-gif-6103373',
    'https://tenor.com/view/oh-wow-gif-6103374',
    'https://tenor.com/view/owen-wilson-owenwilsonwow-wow-ohwow-gif-6111923'
]

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


@bot.command()
async def britt(ctx):
    await ctx.send('https://tenor.com/view/britt-baker-concerned-worried-pray-prays-gif-15698479')


@bot.command()
async def whataboutzoidberg(ctx):
    await ctx.send(random.choice(zoidbergList))


@bot.command()
async def woah(ctx):
    await ctx.send(random.choice(keanuList))


@bot.command()
async def wow(ctx):
    await ctx.send(random.choice(owenList))


@bot.command()
async def hybrid(ctx):
    await ctx.send('https://tenor.com/view/angelico-jack-evans-aew-gif-14949575')


@bot.command()
async def orange(ctx):
    await ctx.send(random.choice(orangeList))


@bot.command()
async def mox(ctx):
    await ctx.send(random.choice(moxList))

@bot.command()
async def lexicon(ctx):
    await ctx.send('https://media.giphy.com/media/XFpQMOOlO0HioCij92/giphy.gif')

bot.run()

