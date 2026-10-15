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

bot = commands.Bot(command_prefix='!', intents=intents)

# replace with your desired channel
channel_id = 1234567891234567890

# custom server-only emoji. you can remove it or change it to ur emoji ids
emoji1 = "<:haha:1234567891234567890>"
emoji2 = "<:kzNekogun:1234567891234567890>"

# roles you want to mention. times are in 24-hour format. change to your role ids
roles = {
    1234567891234567890: (9, 0),
    1234567891234567890: (11, 0),
    1234567891234567890: (16, 0),
    1234567891234567890: (17, 0),
    1234567891234567890: (18, 0),
    1234567891234567890: (19, 0),
    1234567891234567890: (20, 0),
    1234567891234567890: (21, 0)
}

@bot.event
async def on_ready():
    print(f"The bot is ready to do its thing as {bot.user.name}")
    reminder.start()

# your timezone
tz = "Asia/Dhaka"
shomoyzone = pytz.timezone(tz)

# checks every minute to see if the current time matches with time selected above
@tasks.loop(minutes=1)
async def reminder():
    current_time = datetime.datetime.now(shomoyzone)
    channel = bot.get_channel(channel_id)

    for role, (hour, min) in roles.items():
        if current_time.hour == hour and current_time.minute == min:
            notifying_role = channel.guild.get_role(role)
            if notifying_role:
                await channel.send(f"## {notifying_role.mention} It's time for you to study. Ya told me to remind you about studying\n\nComplete Your due studies and HW's or Im preparing my triple katana {emoji1} {emoji2}\n### __tips__\n- If you need any help, feel free to ask in https://discord.com/channels/1234567891234567890/1234567891234567890\n- If you want to join a group study while it's going on, feel free to do so in https://discord.com/channels/1234567891234567890/1234567891234567890")

# simple 'hello' command for the bot
@bot.command()
async def hello(ctx):
    await ctx.send(f"hello {ctx.author.mention}")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
