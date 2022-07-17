import json
import discord
import os

from dotenv import dotenv_values

from core import insertQuestionController
from core import generatePdfController
from core import listController
from core import DiscordProvider

config = dotenv_values(".env")

client = discord.Client()

@client.event
async def on_message(message): 

    discordProvider = DiscordProvider(discord)
    
    if message.content.startswith("-"):
        
        messageList = message.content.split(" ")

        # Quando nenhum parâmetro é passado 
        if (len(messageList) == 1):
            
            infoEmbed = discord.Embed(title="Guia",  color=0x4B8970)
            infoEmbed.add_field(name="- ajuda", value="Exibir informações e opções que você pode usar", inline=False)

            await message.channel.send(embed=infoEmbed)

        # Opções de ajuda
        elif (message.content == "- ajuda"):

            await discordProvider.help(message)
 
        # Listar todas as disciplinas disponíveis
        elif (message.content == "- listar"):

            responseList = listController.handle()

            await discordProvider.list(responseList, message) 

        # Regra para inserir exercício 
        elif (len(messageList) > 1 and messageList[1] == "inserir"):
            
            await discordProvider.insert(message, messageList, client, insertQuestionController) 
       
        # Gerar arquivo de exercícios
        elif (len(messageList) > 1 and messageList[1] == "requisitar"):

            await discordProvider.request(message, messageList, generatePdfController)

DISCORD_TOKEN = config["DISCORD_TOKEN"] or os.getenv("DISCORD_TOKEN")
client.run(DISCORD_TOKEN)

