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


# ia du level mais en mode cogs

import discord
from discord.ext import commands
import json, math, random, asyncio, time

class LevelsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.users = {}
        self.cooldowns = {}
        self.save_lock = asyncio.Lock()
        self.GUILD_ID = 1008865119943524363
        self.LEVEL_CHANNEL_ID = 1008906740538019911
        self.DATA_FILE = 'llevel.json'
        self.bot.loop.create_task(self.save_loop())

    async def cog_load(self):
        try:
            with open(self.DATA_FILE, 'r') as f:
                self.users = json.load(f)
            print("[Levels] llevel.json chargé")
        except FileNotFoundError:
            self.users = {}
            print("[Levels] Aucun fichier llevel.json, création d'un nouveau")

    async def save_loop(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            await asyncio.sleep(30)
            async with self.save_lock:
                with open(self.DATA_FILE, 'w') as f:
                    json.dump(self.users, f, indent=4)

    async def update_data(self, user):
        uid = str(user.id)
        if uid not in self.users:
            self.users[uid] = {
                "totalexp": 0,
                "last_level": 0
            }

    async def add_experience(self, user, exp):
        uid = str(user.id)
        self.users[uid]["totalexp"] += exp

    async def level_up(self, user, message):
        uid = str(user.id)
        experience = max(0, self.users[uid]["totalexp"])
        new_level = int(0.1 * math.sqrt(experience))
        old_level = self.users[uid]["last_level"]

        if new_level > old_level:
            channel = self.bot.get_channel(self.LEVEL_CHANNEL_ID)
            if channel:
                await channel.send(f'{user.mention} tu as tellement parlé que tu es niveau : **{new_level}**!')
            self.users[uid]["last_level"] = new_level

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot or not message.guild:
            return

        if message.guild.id!= self.GUILD_ID:
            return

        is_command = message.content.startswith("legobot::")

        if not is_command:
            now = time.time()
            if message.author.id in self.cooldowns and now - self.cooldowns[message.author.id] < 60:
                return
            self.cooldowns[message.author.id] = now

        async with self.save_lock:
            await self.update_data(message.author)

            if not is_command:
                gain = random.choice([10, 15, 20, 25, 30])
                await self.add_experience(message.author, gain)
                await self.level_up(message.author, message)

    @commands.hybrid_command(name="rank", description="Affiche votre rang ou celui d'un membre")
    async def rank(self, ctx, member: discord.Member = None):
        target = member or ctx.author
        uid = str(target.id)

        if uid not in self.users or self.users[uid]["totalexp"] == 0:
            return await ctx.send(f"{target.mention} n'a pas encore d'XP. Commence par parler!")

        total_xp = self.users[uid]["totalexp"]
        current_level = int(0.1 * math.sqrt(total_xp))

        xp_current_lvl = int((current_level / 0.1) ** 2)
        xp_next_lvl = int(((current_level + 1) / 0.1) ** 2)

        xp_progress = total_xp - xp_current_lvl
        xp_needed_for_lvl = xp_next_lvl - xp_current_lvl
        xp_to_next = xp_next_lvl - total_xp

        embed = discord.Embed(
            title=f"Rank de {target.display_name}",
            description=f"XP Total : **{total_xp}**",
            color=discord.Color.random()
        )
        embed.set_thumbnail(url=target.display_avatar.url)
        embed.add_field(name="Niveau", value=f"**{current_level}**", inline=True)
        embed.add_field(name="Progression", value=f"`{xp_progress} / {xp_needed_for_lvl}` XP", inline=True)
        embed.add_field(name="Level suivant", value=f"Encore `{xp_to_next}` XP", inline=False)

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(LevelsCog(bot))


#voila
