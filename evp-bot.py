import discord

bot = discord.Client()


@bot.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = 'Welcome {0.mention}! How did you find our show?'.format(member)
        await guild.system_channel.send(to_send)


@bot.command()
async def toosweet(ctx):
    await ctx.send('https://tenor.com/view/bullet-club-too-sweet-wrestlers-gif-11235479')


@bot.command()
async def hug(ctx):
    await ctx.send('https://tenor.com/view/aew-trent-beretta-chuck-taylor-orange-cassidy-best-friends-gif-14962323')

# @bot.command()
# async def lechampion(ctx)
#     await

bot.run()
