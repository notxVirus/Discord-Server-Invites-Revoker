import discord
from discord.ext import commands
import os
import colorama
from colorama import Fore, init
colorama.init()

access = [1,2,3,4,5] # who can use bot commands
wl = [1,2,3,4,5] # bot will not revoke invite links of users in this list

client = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

@client.event
async def on_conect():
	print(f"{Fore.YELLOW}LOADING{Fore.RESET} | Connecting to the API")

@client.event
async def on_ready():
	print(f"{Fore.GREEN}SUCCESS{Fore.RESET} | Logged in as {Fore.CYAN}{client.user}{Fore.RESET}")
	print(f"{Fore.YELLOW}INFO{Fore.RESET} | Bot Invite Link: https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=0&scope=bot%20applications.commands")

@client.command(aliases = ['revoke'])
async def start(ctx):
	if ctx.author.id in access:
		invites = len(await ctx.guild.invites())
		if invites == 0:
			return await ctx.send(f"[`ERROR`](https://github.com/notxVirus) | There's no invites on this Discord server.")
		msg = await ctx.send(f"Starting the process of revoking server invites.\nSending logs in Command Prompt.\nServer invites amount: **{invites}**")
		await ctx.send("Developed by [xVirus](https://github.com/notxVirus)")
		a = 0
		for i in await ctx.guild.invites():
			os.system(f"title Successfully revoked {a} server invites. {invites} invites left.")
			try:
				if i.inviter.id in wl:
					print(f"{Fore.WHITE}WHITELISTED{Fore.RESET} | {i} | {i.inviter} ({i.inviter.id})")
				else:
					await i.delete()
					a += 1
					invites = len(await ctx.guild.invites())
					print(f"{Fore.GREEN}SUCCESS{Fore.RESET} | Revoked {i} | {i.inviter} ({i.inviter.id})")
					os.system(f"title Successfully revoked {a} out of {invites} server invites.")
			except Exception as e:
				print(f"{Fore.RED}ERROR{Fore.RESET} | {e}")
		print(f"{Fore.GREEN}SUCCESS{Fore.RESET} | Deactivated {a} server invites.")
		await msg.reply(f"[`DONE`](https://github.com/notxVirus) | Successfully revoked **{a}** server invites.")
		await ctx.send("Thanks for using our script!\nDeveloped by [xVirus](https://github.com/notxVirus)")
		print("Thanks for using our script!\nDeveloped by xVirus - https://github.com/notxVirus")
	else:
		await ctx.send("stfu, nigga. u can't use this command.", delete_after = 10)

client.run("YOUR DISCORD BOT TOKEN")
