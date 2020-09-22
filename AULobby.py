import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv( './.env')
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

lobby420 = ["000000", "NA"]

lobby1 = ["000000", "NA"]
lobby2 = ["000000", "NA"]
lobby3 = ["000000", "NA"]
lobby4 = ["000000", "NA"]
lobby5 = ["000000", "NA"]
lobby6 = ["000000", "NA"]
lobby7 = ["000000", "NA"]
lobby8 = ["000000", "NA"]
lobby9 = ["000000", "NA"]
lobby10 = ["000000", "NA"]

client = commands.Bot(command_prefix = "!lobby ")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("!lobby help"))
    print("AU Lobby is now running")


@client.command(aliases=["g", "G"])
async def get(ctx, num=123):
    
    result = ""

    if num == 1:
        result = "Lobby 1 | code: " + lobby1[0] + " server: " + lobby1[1]
    elif num == 2:
        result = "Lobby 2 | code: " + lobby2[0] + " server: " + lobby2[1]
    elif num == 3:
        result = "Lobby 3 | code: " + lobby3[0] + " server: " + lobby3[1]
    elif num == 4:
        result = "Lobby 4 | code: " + lobby4[0] + " server: " + lobby4[1]
    elif num == 5:
        result = "Lobby 5 | code: " + lobby5[0] + " server: " + lobby5[1]
    elif num == 6:
        result = "Lobby 6 | code: " + lobby6[0] + " server: " + lobby6[1]
    elif num == 7:
        result = "Lobby 7 | code: " + lobby7[0] + " server: " + lobby7[1]
    elif num == 8:
        result = "Lobby 8 | code: " + lobby8[0] + " server: " + lobby8[1]
    elif num == 9:
        result = "Lobby 9 | code: " + lobby9[0] + " server: " + lobby9[1]
    elif num == 10:
        result = "Lobby 10 | code: " + lobby10[0] + " server: " + lobby10[1]
    elif num == 420:
        result = "Lobby 420 | code: " + lobby420[0] + " server: " + lobby420[1]
    else:
        result = "invalid command"

    await ctx.send(result)

@client.command(aliases=["m", "M"])
@commands.has_role('Server Voter')
async def make(ctx, num : int, code, *, server):

    failed = False

    if num == 1:
        lobby1[0] = code.upper()
        lobby1[1] = server.upper()
    elif num == 2:
        lobby2[0] = code.upper()
        lobby2[1] = server.upper()
    elif num == 3:
        lobby3[0] = code.upper()
        lobby3[1] = server.upper()
    elif num == 4:
        lobby4[0] = code.upper()
        lobby4[1] = server.upper()
    elif num == 5:
        lobby5[0] = code.upper()
        lobby5[1] = server.upper()
    elif num == 6:
        lobby6[0] = code.upper()
        lobby6[1] = server.upper()
    elif num == 7:
        lobby7[0] = code.upper()
        lobby7[1] = server.upper()
    elif num == 8:
        lobby8[0] = code.upper()
        lobby8[1] = server.upper()
    elif num == 9:
        lobby9[0] = code.upper()
        lobby9[1] = server.upper()
    elif num == 10:
        lobby10[0] = code.upper()
        lobby10[1] = server.upper()
    elif num == 420:
        lobby420[0] = code.upper()
        lobby420[1] = server.upper()
    else:
        failed = True

    if not failed:
        await ctx.send("Lobby " + str(num) + " set. Code is " + code.upper() + " and is running on " + server.upper() + " servers")
    else:
        await ctx.send("invalid syntax or lobby.")

client.remove_command("help")

@client.command(aliases=["h", "H"])

async def help(ctx):
    await ctx.send("To find out a code for a lobby, type `!lobby get <lobby number>` \n"
    "If you want to set a code for a lobby, type `!lobby make <lobby #> <code> <NA|EU|Asia>`.\n\n"
    ""
    "***NOTE:   only people with the `Server Voter` role can use the `!lobby make` command.*** \n"
    "to get the `Server Voter` tag, vote here:\n"
    "https://top.gg/servers/734164220911812618/vote\n"
    "```New Aliases added\n"
    "Make = m\n"
    "Get = g\n"
    "Help = h\n"
    "\n"
    "E.g.: !lobby m 1 ABCDEF NA``` ")

client.run(DISCORD_TOKEN)