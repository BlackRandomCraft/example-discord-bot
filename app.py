import disnake
from disnake.ext import commands
bot = commands.Bot(command_prefix="*", intents=disnake.Intents.all())

@bot.slash_command(description="sel beaver")
async def sellbeaver(interaction: disnake.AppCmdInter):
    await interaction.send("sold another <@541679146355392522>!")

@bot.slash_command(description="get beaver")
async def getbeaver(interaction: disnake.AppCmdInter):
    await interaction.send("u get new <@541679146355392522>!")

@bot.slash_command(description="get beaver")
async def getbeaver(interaction: disnake.AppCmdInter):
    await interaction.send("u get new <@541679146355392522>!")

bot.run("UR_TOKEN_HERE")