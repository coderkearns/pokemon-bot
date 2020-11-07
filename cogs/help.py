from discord import Embed
from discord.ext import commands

prefix = raise Exception("Replace this with the bot prefix")
embedcolor = 0x7289da


class HELP(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(
	name='help',
	aliases=["?"],
	help=f"""Commands
	EX: {prefix}help
	EX: {prefix}?
	EX: {prefix}help <command>
	EX {prefix}? <command>"""
	)
	async def _help(self, ctx, *, cmd=""):
		cmds = self.bot.commands
		cmd = cmd.replace("\t", "").replace("\n", "")
		if cmd == "":
			message = "The Pokedex options are:\n"
			if ctx.message.guild == None:
				for command in cmds:
					message += ctx.prefix + "**"+command.name+"**\t*"+command.help.split('\n')[0]+"*\n"
					if type(command) == commands.Group:
						for subc in command.walk_commands():
							message += f"{ctx.prefix}{command.name} **{subc.name}**\t*"+ subc.help.split('\n')[0] + "*\n"
			else:
				for command in cmds:
					if command.brief == None:
						message += ctx.prefix + "**"+command.name+"**\t*"+command.help.split('\n')[0]+"*\n"
						if type(command) == commands.Group:
							for subc in command.walk_commands():
								message += f"{ctx.prefix}{command.name} **{subc.name}**\t*"+ subc.help.split('\n')[0] + "*\n"
			e = Embed(description=message,title="Help",color=embedcolor)
		else:
			mycmd = None
			for command in cmds:
				if type(command) == commands.Group:
					for subcommand in command.commands:
						if subcommand.name == cmd.lower().replace(f"{command.name} ", ""):
							mycmd = subcommand
					if not mycmd:
						mycmd = command
				else:
					if command.name == cmd.lower():
						mycmd = command
			if mycmd == None:
				await ctx.send(embed=Embed(description=f"**{cmd}** is not a valid command.", color=embedcolor))
			else:
				e = Embed(description=mycmd.help.format(prefix=ctx.prefix), title=mycmd.name, color=embedcolor)

		await ctx.send(embed=e)



def setup(bot):
	bot.add_cog(HELP(bot))
