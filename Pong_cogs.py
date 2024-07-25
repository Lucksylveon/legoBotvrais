import discord
from discord.ext import commands
import random

class Pong(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Pong on ready")
    
    @commands.command()
    async def pong(self, ctx):
        bot_latency = round(self.bot.latency * 1000)
        await ctx.send(f"ping avec une latence de {bot_latency} ms")
