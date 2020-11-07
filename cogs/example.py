from discord.ext import commands


#######
# Cog #
#######

class Example(commands.Cog):
	def __init__(self, bot):
		self.bot = bot # Allows us to acces the bot in our commands with self.bot

	@commands.command(
		name="ping", # the name we can call the command with
		aliases=["ping-alias"], # any aliases to use instead of name
		help="Ping!" # This help test for !help ping
	)
	async def ping(self, ctx):
		await ctx.send("Pong!") # Sent "Pong!" back to the sender



def setup(bot):
	bot.add_cog(Example(bot))
