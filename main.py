from colorama import Fore, init, Style
import discord
from discord.ext import commands
import asyncio
import requests
import datetime
import re


AriesXJanky = commands.Bot(command_prefix='.', self_bot=True)
init(autoreset=True, convert=True)
AriesXJanky.remove_command('help')

token = ' put your token here'

@AriesXJanky.event
async def on_connect():
    print(
        f"""{Fore.GREEN}
 █████╗ ██████╗ ██╗███████╗███████╗    ███████╗███╗   ██╗██╗██████╗ ███████╗██████╗ 
██╔══██╗██╔══██╗██║██╔════╝██╔════╝    ██╔════╝████╗  ██║██║██╔══██╗██╔════╝██╔══██╗
███████║██████╔╝██║█████╗  ███████╗    ███████╗██╔██╗ ██║██║██████╔╝█████╗  ██████╔╝
██╔══██║██╔══██╗██║██╔══╝  ╚════██║    ╚════██║██║╚██╗██║██║██╔═══╝ ██╔══╝  ██╔══██╗
██║  ██║██║  ██║██║███████╗███████║    ███████║██║ ╚████║██║██║     ███████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝    ╚══════╝╚═╝  ╚═══╝╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
                                                                                    
                                                                                    

________________________________________________________________________________________________________

MADE 
    BY
      ARIES 
           AND 
             JANKY 
________________________________________________________________________________________________________
"""
                                                                                                                        )

@AriesXJanky.event
async def on_message(message):
    if 'https://discord.gift/' in message.content:
        print(Fore.WHITE+"=> [INFO] Nitro Gift Found, Claiming...")
        code = message.content.split('https://discord.gift')[1].split(' ')[0]
        headers = {'Authorization': token, 'Content-Type': 'application/json', 'Accept': 'application/json'}
        json = {
            'channel_id': None,
            'payment_source_id': None
        }
        r = requests.post('https://discordapp.com/api/v6/entitlements/gift-codes/'+code+'/redeem',headers=headers, json=json)
        if r.status_code == 200:
            print(Fore.GREEN + "[<3] Nitro Gift Claimed")
        else:
            print(Fore.RED + "[</3] Nitro Code Invalid")

AriesXJanky.run(token, bot=False)
