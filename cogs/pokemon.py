from discord.ext import commands

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
		self.bot = bot # Allows us to acces the bot in our commands with self.bot

    @commands.group(
    name="dex",
    aliases=["info"],
    pass_context=True
    )
        async def Dex(ctx):
            if ctx.invoked_subcommand is None:
                await bot.say('Invalid sub command passed...')

	@Dex.command(
		name="pokemon",
		help=helpify("Get info on a pokemon", ["pokemon"])
	)
	async def pokemon(self, ctx, *, name_or_id):
        try:
            id = int(name_or_id)
            with open(f"../pokemon/{name_or_id}.json", "r") as file:
                await ctx.send(file.read())
        except ValueError:
            with open("name_to_id.json", "r") as file:
                id_table = json.load(file)
                if (id_table.get(name_or_id)):
                    with open(f"../pokemon/{id_table.get(name_or_id)}.json", "r") as file:
                        await ctx.send(file.read())
                else:
                    await ctx.send(f"`{name_or_id}` doesn't seem to be a pokemon...)



def setup(bot):
	bot.add_cog(Pokemon(bot))
