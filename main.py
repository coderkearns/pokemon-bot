from os import listdir as ls

import discord
from discord.ext import commands


#############
# Bot Setup #
#############

prefix = "."
bot = commands.Bot(
	command_prefix=commands.when_mentioned_or(prefix),
	case_insensitive=True,
	activity=discord.Game("Pokémon | .help")
	)
bot.remove_command('help')


########
# Cogs #
########

for cog in ls("cogs"):
	if "." in cog:
		bot.load_extension("cogs."+cog.replace(".py",""))

def reload_cogs():
	print("Reloading...")
	for cog in ls("cogs"):
		if "." in cog:
			bot.reload_extension("cogs."+cog.replace(".py",""))
	print("Reloaded!")


##########
# Events #
##########

@bot.event
async def on_message(message):
	if message.content[1:7] == "reload": # reload on "{prefix}reload"
		reload_cogs()
		return
	await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
	errorname = str(type(error)).replace("<class '", "").replace("'>","")
	print(f"{errorname}: {error}")

@bot.event
async def on_ready():
		print(f'{bot.user} is now on Discord!')


###############
# Run the Bot #
###############

# Get TOKEN from env, or another source
from os import getenv
TOKEN = getenv("TOKEN")


from keep_alive import keep_alive
keep_alive()

bot.run(TOKEN)
