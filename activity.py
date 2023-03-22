import discord
from discord.ext import commands
from datetime import datetime
import os

bot = commands.Bot(command_prefix="$")


@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.online, activity=discord.Activity(
    type=discord.ActivityType.playing, name="Cu banii Simerienilor"
  ))
  print("Ready")

bot.run('OTMyMzI1MDA3OTAyNzg5NzA0.G4t9R2.IBWu33h_kJMA71jG19zWOcKf9UyjYiINUJpwdI')
