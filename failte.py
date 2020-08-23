import discord
from discord.ext.commands import Bot

BOT_PREFIX = "f-"
BOT_TOKEN = "token"
WELCOME_CHANNEL_ID = ID

failte = Bot(command_prefix = BOT_PREFIX)

@bot.event
async def on_ready():
    print("Logged in as "+failte.user.name)

@bot.event
async def on_member_join(member):
    await failte.wait_until_ready()
    try:
        channel = failte.get_channel(WELCOME_CHANNEL_ID)
        try:
            embed = discord.Embed(colour = discord.Colour.green())
            embed.set_author(name = member.name,icon_url = member.avatar_url)
            embed.add_field(name = "Welcome",value = f"**Hello,{member.mention}! Welcome to {member.guild.name}\nCheck out** #info and #rules !",inline = False)
            embed.set_thumbnail(url = member.guild.icon_url)
            await channel.send(embed = embed)
        except Exception as e:
            raise e
    except Exception as e:
        raise e



failte.run(BOT_TOKEN)