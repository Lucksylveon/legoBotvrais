import discord
from discord.ext import commands, tasks
import random
from discord import Streaming
from discord.utils import get
from discord import app_commands
import time 
import datetime 
from datetime import datetime
import json
from discord import file
#from easy_pil import Editor, load_image_async, font
import typing
from typing import Optional
import math

import Pong_cogs
from Pong_cogs import Pong 

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

bot.remove_command("help")



@bot.event
async def on_ready():
	changeStatus.start()
	print("bot est en ligne")
	synced = await bot.tree.sync()
	print("syncroniser")


status = ["avec legoeloi|.help", "discord|.help", "avec moi-meme|.help", "avec toi|.help", "avec Luck(ニンフィア)|.help", "ma vie de bot|.help"]

channeln = bot.get_channel(1111722478616715407)

@tasks.loop(minutes = 1, seconds = 45)
async def changeStatus():
    
	game = discord.Game(random.choice(status))
	await bot.change_presence(status = discord.Status.online, activity = game)


@tasks.loop(minutes = 5, seconds= 30)
async def editchan(member):
    channeln = bot.get_channel(1111722478616715407)
    await channeln.edit(name= f"membre {member.guild.member_count}")

channel = (1008865119943524366)

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1008865119943524366)
    embed = discord.Embed(title = (member), description = "bienvenue a toi sur le serveur de legoeloi", color = 0xFFE033)
    embed.set_image(url=member.display_avatar)

    embed.add_field(name = "total des menbres", value = (member.guild.member_count))
    await channel.send(f"merci {member.mention}")

    await channel.send(embed= embed)
    guild = member.guild
    channeln = bot.get_channel(1111722478616715407)
    await channeln.edit(name = f"total des membre: {member.guild.member_count}")




@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1008865119943524366)
    embed = discord.Embed(title =f"dommage {member.name}", description = "un menbre vient de nous quitter", color =0xBE2808)

    await channel.send(embed= embed)
    guild = member.guild
    channeln = bot.get_channel(1111722478616715407)
    await channeln.edit(name = f"total des membre: {member.guild.member_count}")


@bot.command()
async def help(ctx):
	help_embed = discord.Embed(title="help commande de legobot", description="les commande pour acceder au chategorie de commande", color=discord.Color.random())

	help_embed.add_field(name="legobot", value="je suis un bot pour le serveur de legoeloi creer par Luck(二ンフㇶア)", inline=False)
	help_embed.add_field(name=".help", value="affiche cette commande", inline=False)
	help_embed.add_field(name=".help_math", value="voir les commande qui font des calcule mathematique", inline=False)
	help_embed.add_field(name=".help_info", value="affiche les commande regroupant plusieur info", inline=False)
	help_embed.add_field(name=".help_time", value="pour les commande de date", inline=False)
	help_embed.add_field(name=".help_basique", value="voir les commande simple et classique", inline=False)
	help_embed.add_field(name=".help_modo", value="voir les commande de moderation fasable que par le staff", inline=False)
	help_embed.add_field(name=".help_gestion", value="voir les commande pour gerer le serv fesable que par le staff", inline=False)
    
    

	await ctx.send(embed=help_embed)



@bot.command()
async def help_math(ctx):
	helpm_embed = discord.Embed(title="help commande de legobot", description="les commande de la chategorie math", color=discord.Color.random())

	helpm_embed.add_field(name="legobot", value="je suis un bot pour le serveur de legoeloi creer par Luck(二ンフㇶア)", inline=False)
	helpm_embed.add_field(name=".help_math", value="affiche cette commande", inline=False)
	helpm_embed.add_field(name="/multiplication", value="pour faire un multiplication", inline=False)
	helpm_embed.add_field(name="/division", value="pour faire une division", inline=False)
	helpm_embed.add_field(name="/addition", value="permet de faire une addition", inline=False)
	helpm_embed.add_field(name="/soustraction", value="permet de faire une soustraction", inline=False)

	await ctx.send(embed=helpm_embed)


@bot.command()
async def help_info(ctx):
	helpi_embed = discord.Embed(title="help commande de legobot", description="les commande de la chategorie info", color=discord.Color.random())

	helpi_embed.add_field(name="legobot", value="je suis un bot pour le serveur de legoeloi creer par Luck(二ンフㇶア)", inline=False)
	helpi_embed.add_field(name=".help_info", value="affiche les commande de cette chategorie", inline=False)
	helpi_embed.add_field(name=".liens", value="envoie les liens des reseaux de legoeloi", inline=False)
	helpi_embed.add_field(name=".modo", value="envoie un message pour les personne demandant a etre modo", inline=False)
	helpi_embed.add_field(name=".majuscule", value="utiliser pour envoier un message en cas d'abus de majuscule", inline=False)
	helpi_embed.add_field(name=".tm", value="envoie le monbre totale de menbre", inline=False)

	await ctx.send(embed=helpi_embed)


@bot.command()
async def help_time(ctx):
	helpt_embed = discord.Embed(title="help commande de legobot", description="les commande de la chategorie time", color=discord.Color.random())

	helpt_embed.add_field(name="legobot", value="je suis un bot pour le serveur de legoeloi creer par Luck(二ンフㇶア)", inline=False)
	helpt_embed.add_field(name=".help_time", value="affiche les commande de cette chategorie", inline=False)
	helpt_embed.add_field(name="/temps", value="te donne la date et l'heure du moment", inline=False)
	helpt_embed.add_field(name="/timestamp", value="te donne la valeur actuele du timestamp", inline=False)

	await ctx.send(embed=helpt_embed)


@bot.command()
async def help_basique(ctx):
	helpb_embed = discord.Embed(title="help commande de legobot", description="les commande de la chategorie basique", color=discord.Color.random())

	helpb_embed.add_field(name="legobot", value="je suis un bot pour le serveur de legoeloi creer par Luck(二ンフㇶア)", inline=False)
	helpb_embed.add_field(name=".help_basique", value="affiche les commande de cette chategorie", inline=False)
	helpb_embed.add_field(name=".ing", value="envoie ong ", inline=False)
	helpb_embed.add_field(name=".salut", value="envoie salut", inline=False)
	helpb_embed.add_field(name=".yo", value="repond yo", inline=False)
	helpb_embed.add_field(name=".ping", value="repond pong avel le temps de l'attense", inline=False)
	helpb_embed.add_field(name="/test", value="une simple commande test", inline=False)
	helpb_embed.add_field(name="/hi", value="repond hello", inline=False)

	await ctx.send(embed=helpb_embed)

@bot.command()
@commands.has_permissions(ban_members = True)
async def help_modo(ctx):
	helpmo_embed = discord.Embed(title="help commande de legobot", description="les commande de la chategorie modo", color=discord.Color.random())

	helpmo_embed.add_field(name="legobot", value="je suis un bot pour le serveur de legoeloi creer par Luck(二ンフㇶア)", inline=False)
	helpmo_embed.add_field(name=".help_modo", value="affiche les commande de cette chategorie", inline=False)
	helpmo_embed.add_field(name=".ban", value="pour bannir un membre", inline=False)
	helpmo_embed.add_field(name=".kick", value="kick un membre pas sur du fonctionement", inline=False)
	helpmo_embed.add_field(name="/dit", value="emvoier un message sous le non du bot", inline=False)
	helpmo_embed.add_field(name=".message", value="envoie un message priver a un membre", inline=False)

	await ctx.send(embed=helpmo_embed)

@bot.command()
@commands.has_permissions(manage_channels= True)
async def help_gestion(ctx):
	helpg_embed = discord.Embed(title="help commande de legobot", description="les commande de la chategorie gestion", color=discord.Color.random())
	helpg_embed.add_field(name="legobot", value="je suis un bot pour le serveur de legoeloi creer par Luck(二ンフㇶア)", inline=False)
	helpg_embed.add_field(name=".help_gestion", value="affiche les commande de cette chategorie", inline=False)
	helpg_embed.add_field(name=".tchaname", value="renomer un channel textuelle", inline=False)
	helpg_embed.add_field(name=".vchaname", value="changer le non d'un channel vocal", inline=False)
	helpg_embed.add_field(name=".textsup", value="supprimer un channel textuelle", inline=False)
	helpg_embed.add_field(name=".voicesup", value="supprimer un channel vocal", inline=False)

	await ctx.send(embed=helpg_embed)

@bot.command()
async def help_level(ctx):
    helpn_emb = discord.Embed(titre="help command de legobot", description="les commande de la category level", color=discord.Color.random())

    helpn_emb.add_field(name="legobot", value="je suis un bot pour le serveur de legoeloi creer par Luck(二ンフㇶア)", inline=False)
    helpn_emb.add_field(name=".help_level", value="affiche les commande de cette categorie", inline=False)
    helpn_emb.add_field(name=".rank", value="affiche ton niveau est experience", inline=False)
    helpn_emb.add_field(name=".rank <userid>", value="en fesant rank suivi de l'id d'un menbre tu peut voir son niveau", inline=False)
    helpn_emb.add_field(name=".topxp", value="affiche le classement des menbre avec leur xp", inline=False)
    helpn_emb.add_field(name=".level", value="affiche le classement des membre avec leur niveaux", inline=False)

    await ctx.send(embed=helpn_emb)



@bot.command()
async def visual(ctx):
	await ctx.send("commande fait sur visual studio code")



@bot.command()
async def pro(ctx):
    proprio = discord.Guild.owner
    vpro = bot.get_user(proprio)
    await ctx.send(f"le createur est {vpro}")




@bot.tree.command()
async def test(interaction: discord.Interaction):
    """Help""" #Description when viewing / commands
    await interaction.response.send_message("hello")



@bot.command()
async def liens(ctx):
	youtubel = "https://www.youtube.com/@legoeloi"
	twitchl = "https://www.twitch.tv/eloilego"
	embed = discord.Embed(title = "les different reseaux de legoeloi", description = f"rejoint legoeloi\n sur youtube {youtubel}\n et aussi sur twitch {twitchl}")
	embed.set_thumbnail(url = "https://yt3.ggpht.com/FjFZ_kuW_FU301P5a5J3pn-tz1epiCPXjBjBQxrsIqlPTu-op8lvkHLGJuchuE57ekXJigQpta0=s176-c-k-c0x00ffffff-no-rj-mo")

	await ctx.send(embed = embed)


@bot.command()
async def modo(ctx):
	await ctx.send("pas la peine de demander a etre modo on ne demande pas les droit d'etre modo se sont les droit de modo qui vienne a toi")


    
@bot.command()
@commands.is_owner()
async def pick(ctx):
    regarder = ["trash", "sciencetrash", "trashbandicout", "c'est dessin anime", "scienceetonante", "leotechmaker", "polo"]
    await ctx.send(random.choice(regarder))


@bot.command()
@commands.is_owner()
async def pickspecial(ctx):
	regarders = ["trash", "sciencetrash", "trashbandicout", "c'est dessin anime", "scienceetonante", "leotechmaker", "docseven", "polo", "pierrecroce", "ben", "code lyoko"]
	await ctx.send(random.choice(regarders))

@bot.command()
async def message(ctx, user:discord.Member, *, message=None):
	message = message
	await user.send(message)



@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason = None):
	await member.kick(reason = reason)
   

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit= amount)


@bot.command()
async def majuscule(ctx):
	await ctx.send("dans la vie tu parle pas en criant ici c'est pareille tu evite l'abus de majuscule merci")

@bot.hybrid_command(name="ban", description="bannir un menbre")
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)



@bot.command()
async def tm(member):
	await member.send(f"totale des menbre sur le serveur {member.guild.member_count} menbre")

@bot.command()
async def pingm(ctx, user:discord.Member):
    await ctx.send(f"hey {user.mention} ```{user.name}```")






@bot.command()
async def salut(ctx):
	await ctx.send("salut")


@bot.tree.command()
async def hi(interaction: discord.Interaction):
	await interaction.response.send_message("hello")


@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
	await interaction.response.send_message(f"hello {interaction.user.mention} c'est une slash command")


@bot.tree.command()
async def temps(interaction: discord.Interaction):
    actuel = datetime.now()
    await interaction.response.send_message(actuel)


@bot.tree.command()
async def timestamp(interaction: discord.Interaction):

    await interaction.response.send_message(f"le timestamp actuelle est de {time.time()} seconde ecouler depuis le 1 janvier 1970 00h00")




@bot.hybrid_command(name="tchaname", description="change le non d'un channel text")
@commands.has_permissions(manage_channels = True)
async def tchaname(ctx, channel: discord.TextChannel, *, new_name):

    await channel.edit(name=new_name)
    await ctx.send("le chanel a etait rename")
    
   


@bot.hybrid_command(name="voicesup", desciption="suprime un channel vocal")
@commands.has_permissions(manage_channels = True)
async def voicesup(ctx, channel: discord.VoiceChannel):
    await channel.delete()
    await ctx.send("channel supprimer")


@bot.hybrid_command(name="textsupee", description="suprime un challe textuelle")
@commands.has_permissions(manage_channels = True)
async def textsupee(ctx, channel: discord.TextChannel):
	await channel.delete()


@bot.hybrid_command(name="textsup", description="supprimer un channel text")
@commands.has_permissions(manage_channels = True)
async def textsup(ctx, channel: discord.TextChannel):
    await channel.delete()
    await ctx.send("channel supprimer")


@bot.hybrid_command(name="vchaname", description="change le non d'un channel vocal")
@commands.has_permissions(manage_channels = True)
async def vchaname(ctx, channel: discord.VoiceChannel, *, new_name):
    await channel.edit(name=new_name)
    await ctx.send("channel rename")


@bot.tree.command(name="dit")
@app_commands.describe(thing_to_say = "que veut tu dire")
async def dit(interaction: discord.Interaction, thing_to_say: str):
	await interaction.response.send_message(f"{interaction.user.name} a dit {thing_to_say}")



@bot.tree.command()
@app_commands.describe(thing_to_say = "nonbre 1", thing_to_say2 = "nonbre 2")
async def multiplication(interaction: discord.Interaction, thing_to_say: int, thing_to_say2: int):
    result = thing_to_say * thing_to_say2
    await interaction.response.send_message(f"le resultat de {thing_to_say} fois {thing_to_say2} est de {result}")



@bot.tree.command()
@app_commands.describe(thing_to_say = "nonbre 1", thing_to_say2 = "nonbre 2")
async def division(interaction: discord.Interaction, thing_to_say: int, thing_to_say2: int):
    result = thing_to_say / thing_to_say2
    await interaction.response.send_message(f"le resultat de {thing_to_say} diviser par {thing_to_say2} est de {result}")


@bot.tree.command()
@app_commands.describe(thing_to_say = "nonbre 1", thing_to_say2 = "nonbre 2")
async def addition(interaction: discord.Interaction, thing_to_say: int, thing_to_say2: int):
    result = thing_to_say + thing_to_say2
    await interaction.response.send_message(f"le resultat de {thing_to_say} plus {thing_to_say2} est de {result}")



@bot.tree.command()
@app_commands.describe(thing_to_say = "nonbre 1", thing_to_say2 = "nonbre 2")
async def soustraction(interaction: discord.Interaction, thing_to_say: int, thing_to_say2: int):
    result = thing_to_say - thing_to_say2
    await interaction.response.send_message(f"le resultat de {thing_to_say} moins {thing_to_say2} est de {result}")



@bot.tree.command()
@app_commands.describe(thing_to_say = "nonbre 1", thing_to_say2 = "nonbre 2")
async def power(interaction: discord.Interaction, thing_to_say: int, thing_to_say2: int):
    result = thing_to_say ** thing_to_say2
    await interaction.response.send_message(f"le resultat de {thing_to_say} a la puissance {thing_to_say2} est de {result}")


@bot.event
async def on_message(message):
    
    
        
    
    
    if message.author.bot == False:
            
        with open('llevel.json', 'r') as f:
            users = json.load(f)
            gain = [10, 15, 20, 25, 30]
            ajj = random.choice(gain)
        
            gaina = [30, 45, 60, 75, 90]
            ajja = random.choice(gaina)

            await update_data(users, message.author)
            
            if message.author.guild_permissions.manage_channels == True:
                if message.content.startswith('.'):
                    await add_experience(users, message.author, 0)
                else:
                    await add_experience(users, message.author, ajja)
            else:
                if message.content.startswith('.'):
                    await add_experience(users, message.author, 0)
                else:
                    await add_experience(users, message.author, ajj)
            await level_up(users, message.author, message)

            with open('llevel.json', 'w') as f:
                json.dump(users, f)

    await bot.process_commands(message)





async def update_data(users, user):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['last_level'] = 0
        users[f'{user.id}']['totalexp'] = 0
        users[f'{user.id}']['level'] = 0


async def add_experience(users, user, exp):
    #users[f'{user.id}']['experience'] += exp
    users[f'{user.id}']['totalexp'] += exp


async def level_up(users, user, message):
    with open('llevel.json', 'r') as g:
        levels = json.load(g)
    last_level = users[f'{user.id}']['last_level']
    lvl = users[f'{user.id}']['level']
    experience = users[f'{user.id}']['totalexp']
    channelv = bot.get_channel(1008906740538019911)
    lvl = 0.1*(math.sqrt(experience))
    if int(lvl) > last_level:
        await channelv.send(f'{user.mention} tu as telement parler que tu est niveau: {int(lvl)}')
        users[f'{user.id}']['last_level'] = int(lvl)
"""

async def level_up(users, user, message):
    with open('llevel.json', 'r') as g:
        levels = json.load(g)
    experience = users[f'{user.id}']['totalexp']
    lvl_start = users[f'{user.id}']['level']
    channelv = bot.get_channel(1008906740538019911)
    lvl_final = lvl_start + 1
    back_xp = (100 + lvl_final ** 3)
    xp_need = (100 + lvl_final ** 3)
    if experience > xp_need:
        await channelv.send(f'{user.mention} tu as telement parler que tu est niveau: {lvl_final}')
        users[f'{user.id}']['level'] = lvl_final
        users[f'{user.id}']['experience'] -= back_xp
"""


@bot.hybrid_command(name="level", description="donne le classement")
async def level(ctx, x=10):
  with open('llevel.json', 'r') as f:
    
    users = json.load(f)
    
  leaderboard = {}
  total=[]
  
  
  
  for user in list(users):
    name = int(user)
    total_amt = users[str(user)]['totalexp']
    total_amt2 = users[str(user)]['level']
    leaderboard[total_amt] = name
    
    
    total.append(total_amt)

    

   

  

    

  total = sorted(total,reverse=True)
  

  
  

  emb = discord.Embed(
    title = f'Top {x} des plus haut niveau sur le serveur de legoeloi',
    description = 'les plus haut niveau',
    color=discord.Color.random()
  )
  
  index = 1
  for amt in total:
    id_ = leaderboard[amt]
    
    member = bot.get_user(id_)

    
    

    emb.add_field(name = f'{index}: {member}', value = f'{amt} xp est level {int(0.1*(math.sqrt(amt)))}', inline=False)
    
    
    
    if index == x:
      break
    else:
      index += 1
      
  await ctx.send(embed = emb)


@bot.hybrid_command(name="levelancien", description="donne votre place dans le leaderboard")
async def levelancient(ctx, x=10):
  with open('llevel.json', 'r') as f:
    
    users = json.load(f)
    
  leaderboard = {}
  total=[]
  lvl = users[f'{user.id}']['level']


  for user in list(users):
    name = int(user)
    total_amt = users[str(user)]['experience']
    leaderboard[total_amt] = name
    total.append(total_amt)

    

    

  total = sorted(total,reverse=True)
  

  em = discord.Embed(
    title = f'Top {x} des plus haut niveau sur le serveur de legoeloi',
    description = 'les plus haut niveau',
    color=discord.Color.random()
  )
  
  index = 1
  for amt in total:
    id_ = leaderboard[amt]
    member = bot.get_user(id_)
    
    
    em.add_field(name = f'{index}: {member}', value = f'niveaux {lvl} est xp {amt}', inline=False)
    
    
    if index == x:
      break
    else:
      index += 1
      
  await ctx.send(embed = em)

@bot.command()
async def yo(ctx):
	await ctx.reply("yo")

@bot.command()
async def ping(ctx):
	await ctx.reply(f'pong avec une latence de {round(bot.latency * 1000)}ms')

@bot.hybrid_command(name="rank", description="afffiche votre rang")
async def rank(ctx, member: discord.Member = None):
    if not member:
        id = ctx.message.author.id
        with open('llevel.json', 'r') as f:
            users = json.load(f)

        

     
        membre= discord.Member.name
        image = ctx.author.avatar
        lvl = users[str(id)]['last_level']
        #exp = users[str(id)]['experience']
        total = users[str(id)]['totalexp']
        exp_prochain = ((int(lvl) + 1 ) / 0.1) ** 2
        exp_prochain = int(exp_prochain)
        exp_tu_as_eu = (int(lvl) / 0.1 ) ** 2
        exp_apres = exp_prochain - exp_tu_as_eu
        exp_tu_as = total - exp_tu_as_eu
        #expl = expf - expd
        #usep = exp - expd
        enb = discord.Embed(title=f"xp total {total}", description="en bas ton niveaux et progression", color=discord.Color.random())
        enb.set_author(name=ctx.author.display_name)
        enb.set_thumbnail(url=f"{image}")
        enb.add_field(name="le niveau", value=f"{lvl}")
        enb.add_field(name="progression", value=f"{int(exp_tu_as)} / {int(exp_apres)} xp")
        enb.add_field(name="level suivant", value=f"{int(exp_apres - exp_tu_as)} xp", inline=False)
        #enb.add_field(name="experience", value=f"{exp} xp total")
        
        if total !=0:
            
            await ctx.send(embed = enb)
        else:
            await ctx.send("vous n'avez pas d'exp commencer par parler dans les channel pour en accumuller")
        
    else:
        id = member.id
        with open('llevel.json', 'r') as f:
            users = json.load(f)
        lvl = users[str(id)]['last_level']
        exp = users[str(id)]['totalexp']
        await ctx.send(f'{member} a le niveau {lvl}!')
        await ctx.send(f'sont xp est de {exp}')


@bot.command()
async def givexp(ctx, user, value: int):
    with open('llevel.json', 'r') as f:
        users = json.load(f)
    users[f'{user}']['experience'] += value
    
    await ctx.send(f"{value} a etait ajouter a {user}")
    






async def setup(bot):
    await bot.add_cog(Pong(bot))


bot.run(token)