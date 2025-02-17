import discord
from discord.ext import commands
import os
import platform
import ctypes
import json
import requests
import base64
import asyncio
import datetime
from discord.errors import HTTPException
from colorama import Fore
from termcolor import colored
import time
import textstat
from pystyle import Colors, Colorate
import random

RESET = '\033[0m'

os.system('cls')

def log(msg):
    current_time = time.strftime("%H:%M", time.localtime())
    print(RESET + f" {current_time} | " + Colors.purple + 'Command ' + RESET + '|' + f" {msg}")


with open("config.json", "r") as file:
    config = json.load(file)
    token = config.get("token")
    prefix = config.get("prefix")
    version = config.get("version")

api_key = "heKjcZQmRH-UsxBoxE4sWUuymiRGfEJ-FPTwqrvfyM"

def save_config(config):
    with open("config.json", "w") as file:
        json.dump(config, file, indent=4)

start_time = datetime.datetime.utcnow()

bot = commands.Bot(command_prefix=prefix, description='not a selfbot', self_bot=True, help_command=None)

LIGHT_PINK = '\033[38;5;13m'  # Light magenta (often considered as light pink in terminals)
WHITE = '\033[38;5;15m'  # White color code
RESET = '\033[0m'

def menu(bot):
 if platform.system() == "Windows":
        os.system('cls')
 else:
        os.system('clear')

 text = r"""               
     []                         ██████╗██╗      ██████╗ ██╗   ██╗██████╗ 
            0        &         ██╔════╝██║     ██╔═══██╗██║   ██║██╔══██╗     0         $
                               ██║     ██║     ██║   ██║██║   ██║██║  ██║                    ~~
       *                       ██║     ██║     ██║   ██║██║   ██║██║  ██║          ^         \
                  !            ╚██████╗███████╗╚██████╔╝╚██████╔╝██████╔╝   .         /\
             ~~                 ╚═════╝╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝ 
                                         github.com/scarlmao                                              
"""

 print(Colorate.Vertical(Colors.purple_to_blue, text,1))
 time.sleep(0.2)  
 print(Colors.purple + ' [+] ' + RESET + f"VERSION {version}")
 print(Colors.purple + ' [+] ' + RESET + f"PREFIX {prefix}")

nitrosnipe = False


@bot.event
async def on_ready():
    if platform.system() == "Windows":
        ctypes.windll.kernel32.SetConsoleTitleW(f"Cloud SB v{version} | Tribute")
        os.system('cls')
    else:
        os.system('clear')
    menu(bot)

@bot.command()
async def dmall(ctx, msg):
    for member in ctx.guild.members:
        try:
            # Attempt to send a DM to each member
            await member.send(msg)
        except:
            continue

    msg = f"{prefix}dmall"
    log(msg)

@bot.command()
async def hentai(ctx):
        r = requests.get(f"https://nekobot.xyz/api/image?type={random.choice(['hentai', 'hass', 'hboobs', 'hmidriff', 'hthigh', 'hanal'])}")
        data = r.json()
        await ctx.send(data["message"])
        msg = f"{prefix}hentai"
        log(msg)

@bot.command()
async def thigh(ctx):
    r = requests.get("https://nekobot.xyz/api/image?type=thigh")
    data = r.json()
    await ctx.send(data["message"])
    msg = f"{prefix}thigh"
    log(msg)

@bot.command()
async def prandom(ctx):
    r = requests.get("https://nekobot.xyz/api/image?type=neko")
    data = r.json()
    await ctx.send(data["message"])
    msg = f"{prefix}prandom"
    log(msg)

@bot.command()
async def clean(ctx):
    if ctx.author.guild_permissions.administrator:
            for channel in ctx.guild.channels:
                try:
                    await channel.delete()
                    await asyncio.sleep(.30)
                except:
                    pass

    msg = f"{prefix}clean"
    log(msg)



@bot.command()
async def webhookspam(ctx, webhook, amount, *, msg):
    for i in range(amount):
     r = requests.post(webhook, json={"username": "Spammed By Cloud Sb", "avatar_url": "", "content": msg})
    await ctx.send('Spammed Webhook')
    msg = f"{prefix}webhookspam"
    log(msg)

@bot.command()
async def webhookdelete(ctx, webhook):
    r = requests.delete(webhook)
    await ctx.send('Webhook Deleted')
    msg = f"{prefix}webhookdelete"
    log(msg)


@bot.command()
async def nuke(ctx, arg=None):
    cloud_msg = f"""
```ansi
[35m[CLOUD SELFBOT] VERSION : [1.1] PREFIX : [.][2m
```
"""
    help_msg = f"""
```ansi
[31m[NUKE COMMANDS][0m
-- [37m.nuke <msg> | Nukes The whole server bans everyone removes all channels and more[0m
-- [37m.dmall <msg> | sends a message to everyone in the server[0m
-- [37m.clean | removes all channels from the server[0m
-- [37m.webhookspam <webhook> <amount> <msg> | spams a message in a webhook[0m
-- [37m.webhookdelete <webhook> | deletes a webhook[0m
```
"""
    
    

    if arg == "help":
        await ctx.send(cloud_msg)
        await ctx.send(help_msg)
        msg = f"{prefix}nuke help"
        log(msg)
    else:
        if ctx.author.guild_permissions.administrator:
            for channel in ctx.guild.channels:
                try:
                    await channel.delete()
                    await asyncio.sleep(.30)
                except:
                    pass
            for role in ctx.guild.roles:
                try:
                    await role.delete()
                    await asyncio.sleep(.30)
                except:
                    pass

            try:
                await ctx.guild.edit(name="Nuked by " + ctx.author.name)
            except:
                pass

            for _ in range(250):
                channel = await ctx.guild.create_text_channel(name="Nuked by " + ctx.author.name)
                await channel.send(f'{arg}')
                await asyncio.sleep(.25)
        msg = f"{prefix}nuke"
        log(msg)   


    


@bot.command()
async def help(ctx):
    cloud_msg = f"""
```ansi
[35m[CLOUD SELFBOT] VERSION : [1.1] PREFIX : [.][2m
```
"""
    help_msg = f"""

```ansi
[36m[HELP][0m
- [33m[FUN][0m
-- [37m{prefix}gay <@user> | Returns the gayness of a user[0m
-- [37m{prefix}cat | Returns a picture of a cat[0m
-- [37m{prefix}dog | Returns a picture of a dog[0m
-- [37m{prefix}ghost <@user> | Ghost pings a user[0m
-- [37m{prefix}joke | Returns a joke[0m
-- [37m{prefix}dick <@user> | Returns the dick length of someone [0m
-- [37m{prefix}kiss <@user> | Kisses a user [0m
-- [37m{prefix}nitro | Responds with a random nitro code[0m
-- [37m{prefix}cf | Flips a coinflip[0m
-- [37m{prefix}eightball <question> | Gives a response to your question[0m
-- [37m{prefix}age <@user> | Returns an estimated age of user based on preivous text[0m
- [35m[UTILS][0m
-- [37m{prefix}help | Returns this message[0m
-- [37m{prefix}purge | Clears all messages[0m
-- [37m{prefix}ftoken <userid> | Sends the token of the discord user[0m
-- [37m{prefix}nitrosniper | Automatically find nitro gift codes when their sent to a server your in[0m
-- [37m{prefix}fetch | Fetches the members in a server[0m
-- [37m{prefix}ping | Sends the bots ping[0m
-- [37m{prefix}spam <amount> <msg> | Spams a message you want[0m
-- [37m{prefix}uptime | Returns how long the bot has been running[0m
-- [37m{prefix}nuke help | Sends The commands you can use for nuking[0m
- [31m[NSFW][0m
-- [37m{prefix}boobs | Returns a picture of boobs[0m
-- [37m{prefix}anal | Returns a picture of anal[0m
-- [37m{prefix}ass | Returns a picture of ass[0m
-- [37m{prefix}thigh | Returns a picture of thigh[0m
-- [37m{prefix}prandom | Returns a random nsfw gif[0m
-- [37m{prefix}hentai | Returns a picture of hentai[0m
```
"""
    await ctx.send(cloud_msg)
    await ctx.send(help_msg)
    msg = f"{prefix}help"
    log(msg)





@bot.event
async def on_message(message):
    global nitrosnipe
    if nitrosnipe == True:
        if "discord.gift/" in message.content:
            msg = message.content
            log(msg)
    await bot.process_commands(message)

def get_readability_scores(text):
    fk_grade_level = textstat.flesch_kincaid_grade(text)
    return fk_grade_level

# Function to translate grade level to age
def grade_level_to_age(grade_level):
    if grade_level < 1:
        return "Below Kindergarten"
    elif 1 <= grade_level < 2:
        return "Age 6-7"
    elif 2 <= grade_level < 3:
        return "Age 7-8"
    elif 3 <= grade_level < 4:
        return "Age 8-9"
    elif 4 <= grade_level < 5:
        return "Age 9-10"
    elif 5 <= grade_level < 6:
        return "Age 10-11"
    elif 6 <= grade_level < 7:
        return "Age 11-12"
    elif 7 <= grade_level < 8:
        return "Age 12-13"
    elif 8 <= grade_level < 9:
        return "Age 13-14"
    elif 9 <= grade_level < 10:
        return "Age 14-15"
    elif 10 <= grade_level < 11:
        return "Age 15-16"
    elif 11 <= grade_level < 12:
        return "Age 16-17"
    elif grade_level >= 12:
        return "Age 17+ (College/Adult)"
    else:
        return "Unknown Age Range"
    
@bot.command()
async def nitrosniper(ctx):
    global nitrosnipe
    if nitrosnipe == False:
     nitrosnipe = True
     await ctx.send('[>] Nitro Sniper Turned On')

     msg = f"{prefix}nitrosniper"
     log(msg)
    else:
     nitrosnipe = False
     await ctx.send('[>] Nitro Sniper Turned Off')

     msg = f"{prefix}nitrosniper"
     log(msg)

@bot.command()
async def age(ctx, user: discord.Member):
    text = ""
    async for message in ctx.channel.history(limit=100):
        if message.author == user:  
            text += message.content + "\n"
    
    
    if not text:
        await ctx.send(f"No messages found from {user.mention}.")
        return

    
    grade_level = get_readability_scores(text)
    

    age_range = grade_level_to_age(grade_level)

    
    await ctx.send(f"Grade Level for {user.mention}: {grade_level}\nEstimated Age Range: {age_range}")
    msg = f"{prefix}age"
    log(msg)

@bot.command()
async def uptime(ctx):
    await ctx.message.delete()
    now = datetime.datetime.now(datetime.timezone.utc)
    delta = now - start_time
    hours, remainder = divmod(int(delta.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    if days:
        time_format = "**{d}** days, **{h}** hours, **{m}** minutes, and **{s}** seconds."
    else:
        time_format = "**{h}** hours, **{m}** minutes, and **{s}** seconds."
    uptime_stamp = time_format.format(d=days, h=hours, m=minutes, s=seconds)
    await ctx.send(uptime_stamp)
    msg = f"{prefix}uptime"
    log(msg)

@bot.command()
async def poll(ctx, *, msg):
    message = await ctx.send(f'```Poll: {msg}```')
    await message.add_reaction('✅')
    await message.add_reaction('❌')
    msg = f"{prefix}poll"
    log(msg)

@bot.command()
async def hypesquad(ctx, house):
        if house == "balance":
            await bot.user.edit(house=discord.HypeSquadHouse.balance)
            await ctx.message.edit(f"🪄 HypeSquad balance ``{house}``", delete_after=3)
        elif house == "bravery":
            await bot.user.edit(house=discord.HypeSquadHouse.bravery)
            await ctx.message.edit(f"🪄 HypeSquad bravery ``{house}``", delete_after=3)
        elif house == "brilliance":
            await bot.user.edit(house=discord.HypeSquadHouse.brilliance)
            await ctx.message.edit(f"🪄 HypeSquad brilliance ``{house}``", delete_after=3)
        else:
            await ctx.message.edit(('hype_fail'), delete_after=3)
        
        msg = f"{prefix}hypesquad"
        log(msg)

@bot.command()
async def spam(ctx, amount, *, message):
    for i in range(int(amount)):
        await ctx.send(message)
    msg = f"{prefix}spam"
    log(msg)

@bot.command()
async def ping(ctx):
        latency = requests.get("https://discord.com/api/users/@me", headers={"Authorization":token}).elapsed.total_seconds()
        msg = f"Your latency is {round(latency * 1000)}ms"

        await ctx.send(msg)
        msg = f"{prefix}ping"
        log(msg)

@bot.command()
async def eightball(ctx, *, question: str):
        responses = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it",
            "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again",
            "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
            "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

        await ctx.send(random.choice(responses))
        msg = f"{prefix}eightball"
        log(msg)

@bot.command()
async def insult(ctx):
        r = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
        insult = r.json()["insult"]
        await ctx.send(insult)
        msg = f"{prefix}insult"
        log(msg)

@bot.command()
async def fetch(ctx):
    await ctx.message.delete()
    members = ctx.guild.members
    file_name = "member_ids.txt"
    with open(file_name, "w") as file:
        for member in members:
            file.write(f"User: {member.name}, ID: {member.id}\n")
    await ctx.send("Heres The Scraped Users", file=discord.File(file_name))
    os.remove(file_name)
    msg = f"{prefix}fetch"
    log(msg)

@bot.command()
async def cf(ctx):
    sides = ["heads","tails"]
    await ctx.send(random.choice(sides))
    msg = f"{prefix}cf"
    log(msg)

@bot.command()
async def ftoken(ctx, id):
    discordid = str(id).encode('utf-8')
    token = base64.b64encode(discordid).decode('utf-8')
    tokenf = token + "." + "######" + "." + "########################"
    await ctx.send(tokenf)
    msg = f"{prefix}ftoken"
    log(msg)

@bot.command()
async def kiss(ctx, user: str=None):
    r = requests.get('https://nekos.life/api/v2/img/kiss')
    image = r.json()["url"]
    await ctx.send(image)
    msg = f"{prefix}kiss"
    log(msg)

@bot.command()
async def purge(ctx):
    await ctx.message.delete()
    await ctx.channel.purge(limit=1000)  
    await ctx.send("Channel nuked! All messages have been deleted.", delete_after=5) 
    msg = f"{prefix}purge"
    log(msg)


@bot.command()
async def joke(ctx):
    r = requests.get('https://icanhazdadjoke.com/slack')
    joke = r.json()["attachments"][0]["text"]
    await ctx.send(joke)
    msg = f"{prefix}joke"
    log(msg)

@bot.command()
async def gay(ctx, user: str=None):
    await ctx.send(f"{user} is {random.randint(1, 100)}% Gay")
    msg = f"{prefix}gay"
    log(msg)

@bot.command()
async def dick(ctx, user: str=None):
    await ctx.send(user + f"'s Dick is {random.random(1,12)} Inches")
    msg = f"{prefix}dick"
    log(msg)

@bot.command()
async def cat(ctx):
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    if response.status_code == 200:
            data = json.loads(response.text)
            cat_image = data[0]['url']
            await ctx.message.edit(cat_image)
    msg = f"{prefix}cat"
    log(msg)

@bot.command()
async def dog(ctx):
    r = requests.get('https://dog.ceo/api/breeds/image/random')
    image = r.json()["message"]
    await ctx.send(image)
    msg = f"{prefix}dog"
    log(msg)
    
@bot.command()
async def ghost(ctx, user: str=None):
     await ctx.message.delete()
     message = await ctx.send(user)
     await message.delete(delay=1)
     msg = f"{prefix}ghost"
     log(msg)

@bot.command()
async def boobs(ctx):
 if isinstance(ctx.channel, discord.TextChannel):
    if ctx.channel.nsfw:
     headers = {
          "authorization": api_key
     }
     r = requests.get('https://api.night-api.com/images/nsfw/boobs',headers=headers)
     image = r.json()["content"]["url"]
     await ctx.send(image)
     msg = f"{prefix}boobs"
     log(msg)
 else:
       headers = {
          "authorization": api_key
     }
       r = requests.get('https://api.night-api.com/images/nsfw/boobs',headers=headers)
       image = r.json()["content"]["url"]
       await ctx.send(image)
       msg = f"{prefix}boobs"
       log(msg)

@bot.command()
async def anal(ctx):
   if isinstance(ctx.channel, discord.TextChannel):
    if ctx.channel.nsfw:
     headers = {
          "authorization": api_key
     }
     r = requests.get('https://api.night-api.com/images/nsfw/anal',headers=headers)
     image = r.json()["content"]["url"]
     await ctx.send(image)
     msg = f"{prefix}gay"
     log(msg)
   else:
       headers = {
          "authorization": api_key
     }
       r = requests.get('https://api.night-api.com/images/nsfw/anal',headers=headers)
       image = r.json()["content"]["url"]
       await ctx.send(image)
       msg = f"{prefix}gay"
       log(msg)


@bot.command()
async def ass(ctx):
 if isinstance(ctx.channel, discord.TextChannel):
    if ctx.channel.nsfw:
     headers = {
          "authorization": api_key
     }
     r = requests.get('https://api.night-api.com/images/nsfw/ass',headers=headers)
     image = r.json()["content"]["url"]
     await ctx.send(image)
     msg = f"{prefix}ass"
     log(msg)
 else:
       headers = {
          "authorization": api_key
     }
       r = requests.get('https://api.night-api.com/images/nsfw/ass',headers=headers)
       image = r.json()["content"]["url"]
       await ctx.send(image)
       msg = f"{prefix}ass"
       log(msg)

@bot.command()
async def nitro(ctx):
    code = "".join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890") for _ in range(16))
    await ctx.send(f"discord.gift/{code}")
    msg = f"{prefix}nitro"
    log(msg)
bot.run(token)