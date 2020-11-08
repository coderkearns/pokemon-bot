from discord.ext import commands
from discord import Embed, File
import json

def helpify(main, names=[], var=""):
	string = main + "\n"
	for name in names:
		string += "EX: {prefix}{name} {var}\n".format(name=name, var=var,prefix="{prefix}")
	return string

#######
# Cog #
#######

class Pokemon(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		
	@commands.group(
		name="dex",
		aliases=["info"],
		help=helpify("Pokedex!", ["dex", "info"]),
		pass_context=True
	)
	async def Dex(self, ctx):
		if ctx.invoked_subcommand is None:
			await ctx.send('Invalid sub command passed...')

	@Dex.command(
		name="pokemon",
		help=helpify("Get info on a pokemon", ["dex pokemon"])
	)
	async def pokemon(self, ctx, *, name_or_id):
		data = {}
		try:
			id = int(name_or_id)
			with open(f"pokemon/{name_or_id}.json", "r") as file:
				data = json.load(file)
		except ValueError:
			with open("pokemon/name_to_id.json", "r") as file:
				id_table = json.load(file)
				if (id_table.get(name_or_id)):
					with open(f"pokemon/{id_table.get(name_or_id)}.json", "r") as file2:
						data = json.load(file2)
				else:
					await ctx.send(f"`{name_or_id}` doesn't seem to be a pokemon...")
					return
		e = Embed(
			color=0xFFCB05,
			title=f"**{ data['name'] }**",
			description=f"""
			**ID**: { data['id'] }
			**Type**: { ", ".join(data['types']) }
			*Stats*
			\tHP: { data['hp'] } 
			\tAttack: { data['attack'] } 
			\tDefense: { data['defense'] } 
			\tSpecial Atk: { data['special_attack'] } 
			\tSpecial Def: { data['special_defense'] } 
			\tSpeed: { data['speed'] } 
			"""
		)
		img = File(f"images/{ data['name'].lower() }.png")
		e.set_thumbnail(url=f"attachment://{ data['name'].lower() }.png")
		await ctx.send(file=img,embed=e)
		



def setup(bot):
	bot.add_cog(Pokemon(bot))
