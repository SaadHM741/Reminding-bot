import discord
from discord.ext import commands, tasks
import logging
from dotenv import load_dotenv
import os
import datetime
import pytz

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='r%', intents=intents)

channel_id = 1458484400944713861

emoji1 = "<:haha:1403584025175654562>"
emoji2 = "<:kzNekogun:1403583894065774592>"

roles = {
    1464890944754159637: (9, 0),
    1464892722635739236: (11, 0),
    1464892891406143715: (16, 0),
    1464893041537056920: (17, 0),
    1464893187146514575: (18, 0),
    1464893188069265553: (19, 0),
    1464893200060776631: (20, 0),
    1464893203571544116: (21, 0),
    1464893206314352640: (22, 0),
    1464893208541528207: (0, 0),
    1464893210215186444: (4, 0),
    1464893211666546698: (5, 0),
    1464893213843128472: (6, 0),
    1470067244007424101: (23, 0),
    1470067424203374755: (7, 0),
    1470067579560136784: (8, 0),
    1470067667628064903: (10, 0)
}

@bot.event
async def on_ready():
    print(f"The bot is ready to do its thing as {bot.user.name}")
    reminder.start()

tz = "Asia/Dhaka"
shomoyzone = pytz.timezone(tz)

@tasks.loop(minutes=1)
async def reminder():
    current_time = datetime.datetime.now(shomoyzone)
    channel = bot.get_channel(channel_id)

    for role, (hour, min) in roles.items():
        if current_time.hour == hour and current_time.minute == min:
            notifying_role = channel.guild.get_role(role)
            if notifying_role:
                await channel.send(f"## {notifying_role.mention} It's time for you to study. Ya told me to remind you about studying\n\nComplete Your due studies and HW's or Im preparing my triple katana {emoji1} {emoji2}\n### __tips__\n- If you need any help, feel free to ask in https://discord.com/channels/1402345409908838520/1458484367281356851\n- If you want to join a group study while it's going on, feel free to do so in https://discord.com/channels/1402345409908838520/1410282915593584750")

@bot.command()
async def hello(ctx):
    await ctx.send(f"hello {ctx.author.mention}")

@bot.command()
async def ip(ctx):
    await ctx.reply("The ip of our minecraft SMP (java 1.21.11) is: 'theoblivionpeaksmpofhomiesreborn.progamer.me'")

bot.run(token, log_handler=handler, log_level=logging.INFO)