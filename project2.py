import discord
from discord.ext import commands, tasks
import random
from discord import Streaming
from discord.utils import get
from discord import * 
import time 
import datetime 
from datetime import datetime
import json
from discord import file
from easy_pil import *
import typing
from typing import Optional
import math
import asyncio
import Pong_cogs
from Pong_cogs import Pong 
from discord import RawReactionActionEvent
from discord.utils import find
from datetime import datetime, timezone, timedelta
import requests 
import re
import os 
import psutil
import pdb
#import vacefron


bot = commands.Bot(command_prefix="legobot::", intents=discord.Intents.all())

bot.remove_command("help")



#@bot.event
#async def on_ready():
	#changeStatus.start()
    
	#print("bot est en ligne")
    
	#synced = await bot.tree.sync()
	#print("syncroniser")
    

@bot.event
async def on_ready():
    editChannel.start()
    changeStatus.start()
    print("en ligne")
    #bot.add_view(Auto_role(), 1209903636474372137)
    synced = await bot.tree.sync()

discord.app_commands.tree

totalm = discord.Guild._member_count

#status = ["avec legoeloi | .help", "discord | .help", "avec moi-meme | .help", "avec toi | .help", "avec Luck(ニンフィア) | .help", "ma vie de bot | .help", "avec Flovv | .help", "rien | .help"]


channeln = bot.get_channel(1111722478616715407)

@tasks.loop(minutes = 0, seconds = 40)
async def changeStatus():
    onligne = await bot.fetch_guild(1008865119943524363, with_counts=True)
    streamer = random.choice(["Legoeloi faire des video", "Flovv jouer a Lord Mobille", "Luck(ニンフィア) me developper", "discord", "rien", "ma vie de bot", "legobot::help", f"{onligne.approximate_member_count} membres"])

    await bot.change_presence(activity=discord.Streaming(name=streamer, url= "https://www.twitch.tv/botpersonaliserparkillian"))



	#game = discord.Game(random.choice(status))
	#await bot.change_presence(status = discord.Status.online, activity = game)

@tasks.loop(minutes= 10, seconds= 30)
async def editChannel():
    channeln = bot.get_channel(1111722478616715407)
    enligne = await bot.fetch_guild(1008865119943524363, with_counts=True)
    await channeln.edit(name = f"en ligne {enligne.approximate_presence_count} / {enligne.approximate_member_count} membres")






channel = (1008865119943524366)

@bot.event
async def on_member_join(member):
    
    channel = bot.get_channel(1008865119943524366)
    image = discord.Member.display_avatar
    embed = discord.Embed(title = (member), description = "bienvenue a toi sur le serveur de legoeloi", color = 0xFFE033)
    embed.set_image(url=member.display_avatar)

    embed.add_field(name = "total des menbres", value = (member.guild.member_count))
    embed.set_footer(text=member.guild.name, icon_url=member.guild.icon)
    embed.timestamp = datetime.now()
    await channel.send(f"merci {member.mention}")

    await channel.send(embed= embed)
    guild = member.guild
    #channeln = bot.get_channel(1111722478616715407)
    #   await channeln.edit(name = f"total des membre: {member.guild.member_count}")



@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1008865119943524366)
    embed = discord.Embed(title =f"dommage {member.name}", description = "un menbre vient de nous quitter", color =0xBE2808)

    await channel.send(embed= embed)
    guild = member.guild
    #await bot.get_channel(1172247861671115407)
    #await channeln.edit(name = f"total des membre: {member.guild.member_count}")




@bot.event
async def on_message_delete(message: discord.Message):
    chanlogs = bot.get_channel(1422990188635881675)
    chanmess = message.channel
    autheur = message.author
    dateact = datetime.now()
    fordat = dateact.strftime("%m/%d/%Y, %I:%M %p") #pourcent x c'est pour la date sa marche pas 
    #iconserv = discord.Guild.icon
    #iconservv = iconserv.url
    dellogem = discord.Embed(title="supression d'un message \n", description=f"message de {autheur} poster dans <#{chanmess.id}>", color=discord.Color.random())

    dellogem.add_field(name="le contenu : ", value=f"{message.content}", inline=False)
    #dellogem.add_field(name="supprimer le : ", value=f"{fordat}")
    dellogem.set_footer(text=message.guild.name, icon_url=message.guild.icon)
    dellogem.timestamp = datetime.now()

    await chanlogs.send(embed= dellogem)

@bot.event
async def on_message_edit(before: discord.Message, after: discord.message):
    chanlogss = bot.get_channel(1422990188635881675)
    chanmesss = before.channel
    autheurs = before.author
    dateacts = datetime.now()
    fordats = dateacts.strftime("%m/%d/%Y, %I:%M %p") #pourcent x c'est pour la date sa marche pas 
    editem = discord.Embed(title="edition d'un message \n", description=f"message de {autheurs} poster dans <#{chanmesss.id}>", color=discord.Color.random())

    editem.add_field(name="avant : ", value=f"{before.content}", inline=False)
    editem.add_field(name="apres : ", value=f"{after.content}", inline=False)
    #editem.add_field(name="\n modifier le : ", value=f"{fordats}")
    editem.set_footer(text=before.guild.name, icon_url=before.guild.icon)
    editem.timestamp = datetime.now()

    await chanlogss.send(embed= editem)


@bot.command()
async def help(ctx):
	help_embed = discord.Embed(title="help commande de legobot", description="les commande pour acceder au chategorie de commande", color=discord.Color.random())

	help_embed.add_field(name="legobot", value="je suis un bot pour le serveur de legoeloi creer par Luck(二ンフㇶア)", inline=False)
	help_embed.add_field(name="legobot::help", value="affiche cette commande", inline=False)
	help_embed.add_field(name="legobot::help_math", value="voir les commande qui font des calcule mathematique", inline=False)
	help_embed.add_field(name="legobot::help_info", value="affiche les commande regroupant plusieur info", inline=False)
	help_embed.add_field(name="legobot::help_time", value="pour les commande de date", inline=False)
	help_embed.add_field(name="legobot::help_basique", value="voir les commande simple et classique", inline=False)
	help_embed.add_field(name="legobot::help_modo", value="voir les commande de moderation fasable que par le staff", inline=False)
	help_embed.add_field(name="legobot::help_gestion", value="voir les commande pour gerer le serv fesable que par le staff", inline=False)
    
    

	await ctx.send(embed=help_embed)



@bot.command()
async def help_math(ctx):
	helpm_embed = discord.Embed(title="help commande de legobot", description="les commande de la chategorie math", color=discord.Color.random())

	helpm_embed.add_field(name="legobot", value="je suis un bot pour le serveur de legoeloi creer par Luck(二ンフㇶア)", inline=False)
	helpm_embed.add_field(name="legobot::help_math", value="affiche cette commande", inline=False)
	helpm_embed.add_field(name="/multiplication", value="pour faire un multiplication", inline=False)
	helpm_embed.add_field(name="/division", value="pour faire une division", inline=False)
	helpm_embed.add_field(name="/addition", value="permet de faire une addition", inline=False)
	helpm_embed.add_field(name="/soustraction", value="permet de faire une soustraction", inline=False)

	await ctx.send(embed=helpm_embed)


@bot.command()
async def help_info(ctx):
	helpi_embed = discord.Embed(title="help commande de legobot", description="les commande de la chategorie info", color=discord.Color.random())

	helpi_embed.add_field(name="legobot", value="je suis un bot pour le serveur de legoeloi creer par Luck(二ンフㇶア)", inline=False)
	helpi_embed.add_field(name="legobot::help_info", value="affiche les commande de cette chategorie", inline=False)
	helpi_embed.add_field(name="legobot::liens", value="envoie les liens des reseaux de legoeloi", inline=False)
	helpi_embed.add_field(name="legobot::modo", value="envoie un message pour les personne demandant a etre modo", inline=False)
	helpi_embed.add_field(name="legobot::majuscule", value="utiliser pour envoier un message en cas d'abus de majuscule", inline=False)
	helpi_embed.add_field(name="legobot::tm", value="envoie le monbre totale de menbre", inline=False)

	await ctx.send(embed=helpi_embed)


@bot.command()
async def help_time(ctx):
	helpt_embed = discord.Embed(title="help commande de legobot", description="les commande de la chategorie time", color=discord.Color.random())

	helpt_embed.add_field(name="legobot", value="je suis un bot pour le serveur de legoeloi creer par Luck(二ンフㇶア)", inline=False)
	helpt_embed.add_field(name="legobot::help_time", value="affiche les commande de cette chategorie", inline=False)
	helpt_embed.add_field(name="/temps", value="te donne la date et l'heure du moment", inline=False)
	helpt_embed.add_field(name="/timestamp", value="te donne la valeur actuele du timestamp", inline=False)

	await ctx.send(embed=helpt_embed)


@bot.command()
async def help_basique(ctx):
	helpb_embed = discord.Embed(title="help commande de legobot", description="les commande de la chategorie basique", color=discord.Color.random())

	helpb_embed.add_field(name="legobot", value="je suis un bot pour le serveur de legoeloi creer par Luck(二ンフㇶア)", inline=False)
	helpb_embed.add_field(name="legobot::help_basique", value="affiche les commande de cette chategorie", inline=False)
	helpb_embed.add_field(name="legobot::ing", value="envoie ong ", inline=False)
	helpb_embed.add_field(name="legobot::salut", value="envoie salut", inline=False)
	helpb_embed.add_field(name="legobot::yo", value="repond yo", inline=False)
	helpb_embed.add_field(name="legobot::ping", value="repond pong avel le temps de l'attense", inline=False)
	helpb_embed.add_field(name="/test", value="une simple commande test", inline=False)
	helpb_embed.add_field(name="/hi", value="repond hello", inline=False)

	await ctx.send(embed=helpb_embed)

@bot.command()
@commands.has_permissions(ban_members = True)
async def help_modo(ctx):
	helpmo_embed = discord.Embed(title="help commande de legobot", description="les commande de la chategorie modo", color=discord.Color.random())

	helpmo_embed.add_field(name="legobot", value="je suis un bot pour le serveur de legoeloi creer par Luck(二ンフㇶア)", inline=False)
	helpmo_embed.add_field(name="legobot::help_modo", value="affiche les commande de cette chategorie", inline=False)
	helpmo_embed.add_field(name="legobot::ban", value="pour bannir un membre", inline=False)
	helpmo_embed.add_field(name="legobot::kick", value="kick un membre pas sur du fonctionement", inline=False)
	helpmo_embed.add_field(name="/dit", value="emvoier un message sous le non du bot", inline=False)
	helpmo_embed.add_field(name="legobot::message", value="envoie un message priver a un membre", inline=False)

	await ctx.send(embed=helpmo_embed)

@bot.command()
@commands.has_permissions(manage_channels= True)
async def help_gestion(ctx):
	helpg_embed = discord.Embed(title="help commande de legobot", description="les commande de la chategorie gestion", color=discord.Color.random())
	helpg_embed.add_field(name="legobot", value="je suis un bot pour le serveur de legoeloi creer par Luck(二ンフㇶア)", inline=False)
	helpg_embed.add_field(name="legobot::help_gestion", value="affiche les commande de cette chategorie", inline=False)
	helpg_embed.add_field(name="legobot::tchaname", value="renomer un channel textuelle", inline=False)
	helpg_embed.add_field(name="legobot::vchaname", value="changer le non d'un channel vocal", inline=False)
	helpg_embed.add_field(name="legobot::textsup", value="supprimer un channel textuelle", inline=False)
	helpg_embed.add_field(name="legobot::voicesup", value="supprimer un channel vocal", inline=False)

	await ctx.send(embed=helpg_embed)

@bot.command()
async def help_level(ctx):
    helpn_emb = discord.Embed(title="help command de legobot", description="les commande de la category level", color=discord.Color.random())

    helpn_emb.add_field(name="legobot", value="je suis un bot pour le serveur de legoeloi creer par Luck(二ンフㇶア)", inline=False)
    helpn_emb.add_field(name="legobot::help_level", value="affiche les commande de cette categorie", inline=False)
    helpn_emb.add_field(name="legobot::rank", value="affiche ton niveau est experience", inline=False)
    helpn_emb.add_field(name="legobot::rank <userid>", value="en fesant rank suivi de l'id d'un menbre tu peut voir son niveau", inline=False)
    helpn_emb.add_field(name="legobot::topxp", value="affiche le classement des menbre avec leur xp", inline=False)
    helpn_emb.add_field(name="legobot::level", value="affiche le classement des membre avec leur niveaux", inline=False)

    await ctx.send(embed=helpn_emb)

@bot.command()
async def testchan(ctx):
    chanlist = await bot.fetch_guild(1008865119943524363, with_counts=True)
    listchan = len(list(chanlist.text_channels))
    
    await ctx.send(f"il y'a {listchan} channel")

@bot.command()
async def untest(ctx):
    enbtest = discord.Embed(title="je test des ecrit", description="c'est des test", color=discord.Color.random())

    enbtest.add_field(name="le test", value='\n```py\n\nimport datetime\n\nprint("hello word !")\n```', inline=False)
    enbtest.add_field(name="le test", value="est fait", inline=False)

    await ctx.send(embed=enbtest)

@bot.command()
async def userinfo(ctx, idmenbre: discord.User):
    infoem = discord.Embed(title=f"information de {idmenbre.display_name}", description=f"info de {idmenbre.display_name}: ({idmenbre.name})", color=discord.Color.random())

    infoem.set_thumbnail(url=f"{idmenbre.avatar}")
    infoem.add_field(name="mention", value=f"{idmenbre.mention}", inline=True)
    infoem.add_field(name="id :", value=f"{idmenbre.id}", inline=True)
    infoem.add_field(name="creer le :", value=f"{idmenbre.created_at}")

    await ctx.send(embed=infoem)

    #await ctx.send(f"user name : {idmenbre.name} \n display name : {idmenbre.display_name} \n creer le : {idmenbre.created_at}")


@bot.command()
async def uneAutreCommande(ctx):
    ctx.send('cest une autre commande' )


@bot.command()
async def chaine(ctx, commande: str, texte: str, param1=None , param2=None, param3=None):
    if commande == "upper":
        texte = texte.upper()
        await ctx.send(texte)
    elif commande == "lower":
        texte = texte.lower()
        await ctx.send(texte)
    elif commande == "len":
        resultstrch = len(texte)
        await ctx.send(resultstrch)
    elif commande == "replace":
        texte = texte.replace(param1, param2)
        await ctx.send(texte)
    elif commande == "index":
        param1 = int(param1)
        resultind = texte[param1]
        await ctx.send(resultind)
    elif commande == "split":
        texte = texte.split(param1)
        await ctx.send(texte)
    elif commande == "replaceo":
        param3 = int(param3)
        texte = texte.replace(param1, param2, param3)
        await ctx.send(texte)
    elif commande == "remove":
        texte = texte[:texte.index(param1)] + texte[texte.index(param1)+1:]
        await ctx.send(texte)

    else:
        await ctx.send("commande pas reconue")




@bot.command()
async def info(ctx):
    pid = os.getpid()
    python_process = psutil.Process(pid)
    memoryUse = python_process.memory_info()[0]/2.**20  # memory use in GB...I think
    pourcent = python_process.memory_info()[0] * 100 / psutil.virtual_memory().total
    memorytotal = psutil.virtual_memory().total / 2.**30
    #bot_latency = round(self.bot.latency * 1000)
    info_embed = discord.Embed(title="commande info", description="des information sur le bot", color=discord.Color.random())
    info_embed.add_field(name="memory use", value=f"{memoryUse} Mo", inline=False)
    info_embed.add_field(name="total ram", value=f"{memorytotal} Go", inline=False)
    info_embed.add_field(name="pourcentage", value=f"{pourcent} %", inline=False)
    info_embed.add_field(name="ping du bot", value=f"{round(bot.latency * 1000)} ms", inline=False)
    await ctx.send(embed=info_embed)
    #await ctx.send(f'memory use:, {memoryUse} go')
    #await ctx.send(f"total {memorytotal} go")
    #await ctx.send(f" pourcentage {pourcent} %")
    #await ctx.send(f'pong avec une latence de {round(bot.latency * 1000)}ms')

def check_if_it_is_me(interaction: discord.Interaction) -> bool:
    return interaction.user.id == 777223645038247946

@bot.tree.command()
@app_commands.check(check_if_it_is_me)
async def only_for_me(interaction: discord.Interaction):
    await interaction.response.send_message('I know you!', ephemeral=True)


@bot.command()
async def visual(ctx):
	await ctx.send("commande fait sur visual studio code")

@bot.command()
async def testguild(ctx):
    guild_id = discord.Guild.id
    
    if message.Guild.id == 1008865119943524363:
        await ctx.send("c'est le serv de eloi")
    else:
        await ctx.send("pas le serveur")

@bot.command()
async def pro(ctx):
    proprio = discord.Guild.owner
    vpro = bot.get_user(proprio)
    await ctx.send(f"le createur est {vpro}")

@bot.command()
async def clap(ctx, phrase: str):
    phrase = phrase.strip()
    phrase = phrase.upper()
    phrase = phrase.replace(" ", ":clap:")
    await ctx.send(f":clap:{phrase}:clap:")



@bot.command()
async def add(ctx, nb1: float, nb2: float):
    resulte = nb1 + nb2
    await ctx.send(f"sa fait {resulte}")


@bot.command()
async def dectobits(ctx, nonbredec: int):
    bit_count = math.floor(math.log2(nonbredec)) + 1
    await ctx.send(f"le nombre de bits pour stoquer {nonbredec} est de {bit_count} bits")
    await ctx.send("grace a math.floor(math.log2(leNomnre)) + 1 ")





@bot.command()
async def toilete(ctx):
    adim = []
    role1 = discord.Guild.get_role(role_id =1069976682129268736)
    lm = role1.members
    for user in list(lm):
        adim[user]
    
    await ctx.send(f"test {user}")

@bot.command()
async def choix(ctx, *args):
    finale = (random.choice(args))
    await ctx.send(f"le choix est {finale}")

@bot.command()
async def insta_cest_des_connard(ctx):
    await ctx.send("oui c'est des fils de putes qui savent rien faire ")



@bot.command()
async def timea(ctx):
    await ctx.send(time.strftime("%b %a %I %p "))

@bot.command()
async def debug(ctx, unecommand):
    #result = pdb.run(unecommand)      
    await ctx.send(result)


@bot.tree.command()
async def test(interaction: discord.Interaction):
    """Help""" #Description when viewing / commands
    await interaction.response.send_message("hello")

@bot.event
async def on_raw_reaction_add(payload):
    
    
    message_id = payload.message_id
    
    if message_id == 1335638326543257752:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)
        #roleee = discord.utils.get(guild.roles, name="marchepas")
        #member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
        if payload.emoji.name == "clap":
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            #roleee = discord.utils.get(guild.roles, name="marchepas")
            await member.add_roles(1335658621085810688)
            
        
        #if roleee is not None:
            #member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            #if member is not None:
                #await member.add_roles(roleee)
            #else:
                #print("menbre pas trouver")
        #else:
            #print("role pas trouvé")






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
async def spam(ctx, spamed: discord.Member or discord.Role, value: int):
    
    i = 1
    while(i <= value):
        await ctx.send(f"{spamed.mention} {i} sur {value}")
        i = i+1 

    
@bot.command()
@commands.is_owner()
async def pick(ctx):
    regarder = ["c'est dessin anime1",  "c'est dessin anime", "c'est dessin anime2","scienceetonante", "scienceetonante2", "scienceetonante1","leotechmaker", "leotechmaker2", "leotechmaker1", "polo","pickdeux", "peut importe", "c'est dessin anime3", "leo techmaker3", "pick", "pick", "pick", "pick", "scienceetonante3", "peux importe", "docseven"]
    await ctx.send(random.choice(regarder))


@bot.command()
@commands.is_owner()
async def pickdeux(ctx):
    regardedr = ["c'est dessin anime1",  "c'est dessin anime", "c'est dessin anime2","scienceetonante", "scienceetonante2", "scienceetonante1","leotechmaker", "leotechmaker2", "leotechmaker1", "polo","picktrois", "autre", "c'est dessin anime", "leotechmaker", "pick", "pick", "pick", "pick", "scienceetonante", "peux importe", "docseven"]
    await ctx.send(random.choice(regardedr))

@bot.command()
@commands.is_owner()
async def pickspecial(ctx):
	regarders = ["c'est dessin anime", "scienceetonante", "leotechmaker", "docseven", "polo", "pierrecroce", "ben", "code lyoko"]
	await ctx.send(random.choice(regarders))


@bot.command()
@commands.is_owner()
async def picktrois(ctx):
    regarder = ["c'est dessin anime1",  "c'est dessin anime", "c'est dessin anime2","scienceetonante", "scienceetonante2", "scienceetonante1","leotechmaker", "leotechmaker2", "leotechmaker1", "polo","choix avec 3 de chaque 2 pick et trash", "polo1", "codelyoko", "docseven", "c'est dessin anime", "peux inporte", "scienceetonante", "pick", "leotechmaker", "pick"]
    await ctx.send(random.choice(regarder))


@bot.command()
@commands.is_owner()
async def poloc(ctx):
	regarders = ["fall guy", "mario maker", "mario partt", "roblox", "splix.io", "sliter.io", "agario.io", "clustertruck", "housse flipper", "geometry dash", "minecraft", "ramdom"]
	await ctx.send(random.choice(regarders))

@bot.command()
@commands.is_owner()
async def cdac(ctx):
	regarders = ["top10", "soloal", "thematique", "classique", "classique anne sport", "ramdom"]
	await ctx.send(random.choice(regarders))


@bot.command()
@commands.is_owner()
async def trashc(ctx):
	regarderse = ["principal", "bandicoot", "science", "peut importe"]
	await ctx.send(random.choice(regarderse))


@bot.command()
async def message(ctx, user:discord.Member, *, message=None):
	message = message
	await user.send(message)

discord.Guild.member_count

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



"""
@bot.hybrid_command(name="ban", description="bannir un menbre")
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await ctx.ban(reason = reason)


from datetime import datetime, timezone, timedelta

# Définir le décalage horaire de Tokyo (UTC+9)
tokyo_timezone = timezone(timedelta(hours=9))

# Obtenir la date et l'heure actuelles à Tokyo
heure_tokyo = datetime.now(tokyo_timezone)

# Afficher l'heure de Tokyo
print("L'heure actuelle à Tokyo est :", heure_tokyo)
from datetime import datetime, timezone, timedelta

# Définir le décalage horaire de Tokyo (UTC+9)
tokyo_timezone = timezone(timedelta(hours=9))

# Obtenir la date et l'heure actuelles à Tokyo
heure_tokyo = datetime.now(tokyo_timezone)

# Formater l'heure de Tokyo
heure_formatee = heure_tokyo.strftime("%m/%d %H:%M")

# Afficher l'heure de Tokyo
print("L'heure actuelle à Tokyo est :", heure_formatee)

from datetime import datetime, timezone, timedelta

# Définir le décalage horaire de Tokyo (UTC+9)
tokyo_timezone = timezone(timedelta(hours=9))

# Dictionnaires des noms des mois et des jours en japonais
mois_japonais = {
    1: "一月", 2: "二月", 3: "三月", 4: "四月", 5: "五月", 6: "六月",
    7: "七月", 8: "八月", 9: "九月", 10: "十月", 11: "十一月", 12: "十二月"
}

jour_japonais = {
    0: "月曜日", 1: "火曜日", 2: "水曜日", 3: "木曜日",
    4: "金曜日", 5: "土曜日", 6: "日曜日"
}

# Obtenir la date et l'heure actuelles à Tokyo
heure_tokyo = datetime.now(tokyo_timezone)

# Obtenir le numéro du mois et du jour
numero_mois = heure_tokyo.month
numero_jour_semaine = heure_tokyo.weekday()

# Obtenir les noms en japonais
nom_mois_japonais = mois_japonais[numero_mois]
nom_jour_semaine_japonais = jour_japonais[numero_jour_semaine]

# Formater l'heure de Tokyo avec les noms en japonais
heure_formatee = "{}月 {} {}".format(nom_mois_japonais, heure_tokyo.day, nom_jour_semaine_japonais)

# Afficher l'heure de Tokyo
print("L'heure actuelle à Tokyo est :", heure_formatee)

"""

@bot.command()
async def tm(member):
	await member.send(f"totale des menbre sur le serveur {member.guild.member_count} menbre")

@bot.command()
async def pingm(ctx, user:discord.Member):
    await ctx.send(f"hey {user.mention} ```{user.name}```")


@bot.command()
async def tt(ctx):
    # Dictionnaires des noms des mois et des jours en japonais
    tokyo_timezone = timezone(timedelta(hours=9))
    mois_japonais = {
    1: "1月", 2: "2月", 3: "3月", 4: "4月", 5: "5月", 6: "6月",
    7: "7月", 8: "8月", 9: "9月", 10: "10月", 11: "11月", 12: "12月"
}

    jour_japonais = {
    0: "月曜日", 1: "火曜日", 2: "水曜日", 3: "木曜日",
    4: "金曜日", 5: "土曜日", 6: "日曜日"
}

    #Obtenir la date et l'heure actuelles à Tokyo
    heure_tokyo = datetime.now(tokyo_timezone)

    # Obtenir le numéro du mois et du jour
    numero_mois = heure_tokyo.month
    numero_jour_semaine = heure_tokyo.weekday()

    # Obtenir les noms en japonais
    nom_mois_japonais = mois_japonais[numero_mois]
    nom_jour_semaine_japonais = jour_japonais[numero_jour_semaine]
    hm = datetime.now(tokyo_timezone)
    hmfor = hm.strftime("%H:%M")
    an = datetime.now(tokyo_timezone)
    ye = an.strftime("%Y")

    # Formater l'heure de Tokyo avec les noms en japonais
    heure_formatee = "{}{}日 {}".format(nom_mois_japonais, heure_tokyo.day, nom_jour_semaine_japonais)
    await ctx.send(f"a tokyo on est le: {ye}年{heure_formatee} a {hmfor} ")
    frtem = time.strftime("%b %a %I %p ")
    await ctx.send(f"est en france {frtem}")



@bot.command(name="embed")
@commands.has_permissions(manage_messages=True)
async def embed(ctx, channel: commands.TextChannelConverter):
    await ctx.send(f"{ctx.author} envoyez votre message dans les 60 secondes")
    try:

        msg = await bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=60)
        embed = discord.Embed(
                    type='article',
                    description=msg.content
                    )
        await channel.send(embed=embed)
 

    except asyncio.TimeoutError:
        await ctx.send("Temps écoulé relancez la commande.")

@bot.command()
async def presence(ctx):
    persent = await bot.fetch_guild(1008865119943524363, with_counts=True)
    await ctx.send(f"le nombre en ligne {persent.approximate_presence_count} utilisateur")

@bot.tree.context_menu()
async def react(interaction: discord.Interaction, message: discord.Message):
    await interaction.response.send_message('Very cool message!', ephemeral=True)

@bot.command()
async def salut(ctx):
	await ctx.send("salut")

@app_commands.context_menu()
async def ban(interaction: discord.Interaction, user: discord.Member):
    await interaction.response.send_message(f'Should I actually ban {user}...', ephemeral=True)

@bot.tree.command()
async def hi(interaction: discord.Interaction):
	await interaction.response.send_message("hello")


@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
	await interaction.response.send_message(f"hello {interaction.user.mention} c'est une slash command")



@bot.tree.command(name="badge")
async def hello(interaction: discord.Interaction):
	await interaction.response.send_message(f"coucou {interaction.user.mention} c'est pour activer le badge")




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
async def multiplication(interaction: discord.Interaction, thing_to_say: float, thing_to_say2: float):
    result = float(thing_to_say) * float(thing_to_say2)
    await interaction.response.send_message(f"le resultat de {thing_to_say} fois {thing_to_say2} est de {result}")



@bot.tree.command()
@app_commands.describe(thing_to_say = "nonbre 1", thing_to_say2 = "nonbre 2")
async def division(interaction: discord.Interaction, thing_to_say: float, thing_to_say2: float):
    result = float(thing_to_say) / float(thing_to_say2)
    await interaction.response.send_message(f"le resultat de {thing_to_say} diviser par {thing_to_say2} est de {result}")


@bot.tree.command()
@app_commands.describe(thing_to_say = "nonbre 1", thing_to_say2 = "nonbre 2")
async def addition(interaction: discord.Interaction, thing_to_say: float, thing_to_say2: float):
    result = float(thing_to_say) + float(thing_to_say2)
    await interaction.response.send_message(f"le resultat de {thing_to_say} plus {thing_to_say2} est de {result}")



@bot.tree.command()
@app_commands.describe(thing_to_say = "nonbre 1", thing_to_say2 = "nonbre 2")
async def soustraction(interaction: discord.Interaction, thing_to_say: float, thing_to_say2: float):
    result = float(thing_to_say) - float(thing_to_say2)
    await interaction.response.send_message(f"le resultat de {thing_to_say} moins {thing_to_say2} est de {result}")



@bot.tree.command()
@app_commands.describe(thing_to_say = "nonbre 1", thing_to_say2 = "nonbre 2")
async def power(interaction: discord.Interaction, thing_to_say: float, thing_to_say2: float):
    result = float(thing_to_say) ** float(thing_to_say2)
    bit_count = math.floor(math.log2(result)) + 1
    await interaction.response.send_message(f"le resultat de {thing_to_say} a la puissance {thing_to_say2} est de {result} et le nombre de bits et de {bit_count} bits")


@bot.command()
async def char(ctx, number: int):
    await ctx.send(f"le nombre {number} de valeur hexadecimal {number:0x} et binaire {number:0b} correspond en unicode a {number:0c}")



@bot.event
async def on_message(message):
    
    
    
    
    
    if message.author.bot == False:
    
        if message.author.guild.id == 1008865119943524363:
        
            
            with open('llevel.json', 'r') as f:
                users = json.load(f)
                gain = [10, 15, 20, 25, 30]
                ajj = random.choice(gain)
            
            

                await update_data(users, message.author)
                

                
                
            
                if message.content.startswith('legobot::'):
                    await add_experience(users, message.author, 0)
                else:
                    await add_experience(users, message.author, ajj)
                await level_up(users, message.author, message)

                
                with open('llevel.json', 'w') as f:
                    json.dump(users, f, sort_keys=True, indent=4)
        
        

    await bot.process_commands(message)


async def auto_responce(message, user: discord.User, dm: discord.DMChannel):
    if message in dm:
        await user.send("test")
 
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
async def level(ctx):
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
    title = f'Top 10 des plus haut niveau sur le serveur de legoeloi',
    description = 'les plus haut niveau',
    color=discord.Color.random()
  )
  
  index = 1
  for amt in total:
    id_ = leaderboard[amt]
    
    member = bot.get_user(id_)

    
    

    emb.add_field(name = f'{index}: {member}', value = f'{amt} xp est level {int(0.1*(math.sqrt(amt)))}', inline=False)
    
    
    
    if index == 10:
      break
    else:
      index += 1
      
  await ctx.send(embed = emb)


async def Getindex(utilisateur: discord.Member):
    with open('llevel.json', 'r') as f:

        users = json.load(f)
    lede = {}
    toto = []
    for user in list(users):
        name = int(user)
        total_amt = users[str(user)]['totalexp']
        lede[total_amt] = name
        toto.append(total_amt)

    toto = sorted(toto,reverse=True)

    index = 1
    for amt in toto:
        _id = lede[amt]
        mem = bot.get_user(_id)

        if mem == utilisateur:
            return f"{index} / {len(toto)}"
        else:
            index +=1
    
    

async def Test():
    tab = ("yo", "reyo", "yoyoy")
    index = 2
    return f"{index}/{len(tab)}"


@bot.command()
async def teste(ctx):
    le_retour = await Test()    
    await ctx.send(le_retour)


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

        #position = level(index)

     
        membre= discord.Member.name
        image = ctx.author.avatar
        lvl = users[str(id)]['last_level']
        pos = await Getindex(ctx.author)
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
        enb.add_field(name="ta position", value=f"{pos}")
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
async def testrank(ctx, member: discord.Member = None):
    if not member:
        id = ctx.message.author.id
        with open('llevel.json', 'r') as f:
            users = json.load(f)

        #position = level(index)

     
        #embre= discord.Member.name
        #image = ctx.author.avatar
        lvl = users[str(id)]['last_level']
        #pos = await Getindex(ctx.author)
        #exp = users[str(id)]['experience']
        total = users[str(id)]['totalexp']
        exp_prochain = ((int(lvl) + 1 ) / 0.1) ** 2
        #percent = total / exp_prochain * 100
        exp_tu_as_eu = (int(lvl) / 0.1 ) ** 2
        exp_apres = exp_prochain - exp_tu_as_eu
        exp_tu_as = total - exp_tu_as_eu
        position = await Getindex(ctx.author)
        percent = (exp_tu_as / exp_apres) * 100
        #exp_prochain = int(exp_prochain)
        #rolec = ctx.author.role
        color = f"{ctx.author.color}"
        user_data = {  # Most likely coming from database or calculation
            "name": ctx.author.display_name,  # The user's name
            "xp": exp_tu_as,
            "xpafter": exp_apres,
            "next_level_xp": exp_prochain,
            "level": lvl,
            "percentage": percent,
            "total": total,
            "rank": position,
        }

        background = Editor(Canvas((934, 282), "#23272a"))
        profile_picture = await load_image_async(str(ctx.author.avatar.url))
        profile = Editor(profile_picture).resize((190, 190)).circle_image()

        # For profile to use users profile picture load it from url using the load_image/load_image_async function
        # profile_image = load_image(str(ctx.author.avatar_url))
        # profile = Editor(profile_image).resize((150, 150)).circle_image()


        poppins = Font.poppins(size=30)

        background.rectangle((20, 20), 894, 242, "#2a2e35")
        background.paste(profile, (50, 50))
        background.ellipse((42, 42), width=206, height=206, outline="#43b581", stroke_width=10)
        background.rectangle((260, 180), width=630, height=40, fill="#484b4e", radius=20)
        background.bar(
            (260, 180),
            max_width=630,
            height=40,
            percentage=user_data["percentage"],
            fill=color,
            radius=20,
        )       
        background.text((270, 120), user_data["name"], font=poppins, color=color)
        background.text(
            (870, 125),
            f"{user_data['xp']} / {user_data['xpafter']}",
            font=poppins,
            color="#00fa81",
            align="right",
        )

        rank_level_texts = [
            Text("position ", color="#00fa81", font=poppins),
            Text(f"{user_data['rank']}", color="#1EAAFF", font=poppins),
            Text("  exp ", color="#00fa81", font=poppins),
            Text(f"{user_data['total']}", color="#1EAAFF", font=poppins),
            Text("   Level ", color="#00fa81", font=poppins),
            Text(f"{user_data['level']}", color="#1EAAFF", font=poppins),
        ]       

        background.multi_text((850, 30), texts=rank_level_texts, align="right")

        file = discord.File(fp=background.image_bytes, filename="levelcard.png")
        #await ctx.send(file=file)

        if total !=0:
            
            await ctx.send(file=file)
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











class Auto_role(discord.ui.View):
    def __init__(self):
        super().__init__()
    
    @discord.ui.button(label="test 1", style=discord.ButtonStyle.green)
    async def test_1(self, interaction: discord.Interaction, Button: discord.ui.Button):
        test_1_role = discord.utils.get(interaction.guild.roles, name="test 1")

        if test_1_role in interaction.user.roles:
            await interaction.user.remove_roles(test_1_role)
            await interaction.response.send_message("le role test 1 vous a etait enlever", ephemeral=True)
        else:

            await interaction.user.add_roles(test_1_role)
            await interaction.response.send_message("le role test 1, vous a etait donner", ephemeral= True)
    
    @discord.ui.button(label="test 2", style=discord.ButtonStyle.blurple)
    async def test_2(self, interaction: discord.Interaction, Button: discord.ui.Button):
        test_2_role = discord.utils.get(interaction.guild.roles, name="test 2")

        if test_2_role in interaction.user.roles:
            await interaction.user.remove_roles(test_2_role)
            await interaction.response.send_message("vous avait plus le role test 2", ephemeral=True)
        else:

            await interaction.user.add_roles(test_2_role)
            await interaction.response.send_message("le role test 2, vous a etait donner", ephemeral=True)
    
    @discord.ui.button(label="test 3", style=discord.ButtonStyle.red)
    async def test_3(self, interaction: discord.Interaction, Button: discord.ui.Button):
        test_3_role = discord.utils.get(interaction.guild.roles, name="test 3")

        if test_3_role in interaction.user.roles:
            await interaction.user.remove_roles(test_3_role)
            await interaction.response.send_message("le role test 3 vous a etait enlever", ephemeral=True)
        else:

            await interaction.user.add_roles(test_3_role)
            await interaction.response.send_message("le role test 3, vous a etait donner", ephemeral=True)
        

@bot.command()
@commands.has_permissions(manage_channels=True)
async def auto_roles(ctx):
    rembed = discord.Embed(title= "auto role", description= "appuis pour avoir le role indiquer sur le bouton")
    await ctx.send(embed = rembed, view = Auto_role())


"""
leaderboard = {}
total=[]
    for user in list(users):
        name = int(user)
        total_amt = users[str(user)]['totalexp']
        total_amt2 = users[str(user)]['level']
        leaderboard[total_amt] = name
        total.append(total_amt)

    total = sorted(total,reverse=True)

    index = 1
    for amt in total:
        id_ = leaderboard[amt]
    
        member = bot.get_user(id_)

        if ctx.author = member:
            position = index
        else:
            index += 1
"""


async def setup(bot):
    await bot.add_cog(Pong(bot))


bot.run(token)


#ancient 


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
    



class Auto_role(discord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)
    
    @discord.ui.button(label="test 1", style=discord.ButtonStyle.green)
    async def test_1(self, interaction: discord.Interaction, Button: discord.ui.Button):
        test_1_role = discord.utils.get(interaction.guild.roles, name="test 1")

        if test_1_role in interaction.user.roles:
            await interaction.user.remove_roles(test_1_role)
            await interaction.response.send_message("le role test 1 vous a etait enlever", ephemeral=True)
        else:

            await interaction.user.add_roles(test_1_role)
            await interaction.response.send_message("le role test 1, vous a etait donner", ephemeral= True)
    
    @discord.ui.button(label="test 2", style=discord.ButtonStyle.blurple)
    async def test_2(self, interaction: discord.Interaction, Button: discord.ui.Button):
        test_2_role = discord.utils.get(interaction.guild.roles, name="test 2")

        if test_2_role in interaction.user.roles:
            await interaction.user.remove_roles(test_2_role)
            await interaction.response.send_message("vous avait plus le role test 2", ephemeral=True)
        else:

            await interaction.user.add_roles(test_2_role)
            await interaction.response.send_message("le role test 2, vous a etait donner", ephemeral=True)
    
    @discord.ui.button(label="test 3", style=discord.ButtonStyle.red)
    async def test_3(self, interaction: discord.Interaction, Button: discord.ui.Button):
        test_3_role = discord.utils.get(interaction.guild.roles, name="test 3")

        if test_3_role in interaction.user.roles:
            await interaction.user.remove_roles(test_3_role)
            await interaction.response.send_message("le role test 3 vous a etait enlever", ephemeral=True)
        else:

            await interaction.user.add_roles(test_3_role)
            await interaction.response.send_message("le role test 3, vous a etait donner", ephemeral=True)
        

@bot.command()
@commands.has_permissions(manage_channels=True)
async def auto_roles(ctx):
    rembed = discord.Embed(title= "auto role", description= "appuis pour avoir le role indiquer sur le bouton")
    await ctx.send(embed = rembed, view = Auto_role())


async def setup(bot):
    await bot.add_cog(Pong(bot))


bot.run(token)




