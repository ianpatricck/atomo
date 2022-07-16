import json
import uuid

class DiscordProvider:

    def __init__(self, discord):

        self.discord = discord

        self.successColor = 0x4B8970
        self.dangerColor = 0xff2939

    async def help(self, message):

        helpEmbed = self.discord.Embed(title="Ajuda",  color=self.successColor)

        helpEmbed.add_field(name="- inserir [tag_disciplina] [tag_ramo]", value="Inserir exercício problema \nEx: - inserir matematica razao_e_proporcao", inline=False)
        helpEmbed.add_field(name="- requisitar [tag_disciplina] [tag_ramo]", value="Obter PDF com exercícios \nEx: - requisitar fisica trabalho_e_energia", inline=False)
        helpEmbed.add_field(name="- listar", value="Ver disciplinas e ramos disponíveis", inline=False)

        await message.channel.send(embed=helpEmbed)

    async def list(self, responseList, message):

        if (responseList["status"] == True):
           
            listEmbed = self.discord.Embed(title="Listagem das disciplinas e ramos", color=self.successColor)

            for discipline, branches in responseList["data"].items():
                listEmbed.add_field(name=discipline, value='\n'.join(branches), inline=False)

            await message.channel.send(embed=listEmbed)

        else:
            print(responseList["data"])

    async def insert(self, message, messageList, client, insertQuestionController):

        insertOptions = {}

        insertOptions["disciplina"] = messageList[2]
        insertOptions["ramo"] = messageList[3]

        await message.channel.send("Escreva abaixo o enunciado do problema")

        def checkChannel(m):
            return m.channel == message.channel

        questionBody = await client.wait_for("message", check=checkChannel)

        insertOptions["enunciado"] = questionBody.content

        await message.channel.send("Informe as alternativas (separadas em vírgulas)")

        questionOptions = await client.wait_for("message", check=checkChannel)

        questionOptionsList = questionOptions.content.split(", ")

        if (len(questionOptionsList) < 2):
            errorEmbed = discord.Embed(title="Erro", color=self.successColor)
            errorEmbed.set_footer(text="Número de alternativas inválido")

            await message.channel.send(embed=errorEmbed)
            return 0

        insertOptions["alternativas"] = questionOptionsList

        await message.channel.send("Informe o gabarito da questão")

        questionFeedback = await client.wait_for("message", check=checkChannel)

        insertOptions["gabarito"] = questionFeedback.content

        await questionFeedback.delete()

        insertResultStatus = insertQuestionController.handle(json.dumps(insertOptions))

        responseEmbed = None

        if (insertResultStatus["status"] == True):
            responseEmbed = self.discord.Embed(title=insertResultStatus["data"], color=self.successColor)
        else:
            responseEmbed = self.discord.Embed(title=insertResultStatus["data"], color=self.dangerColor)

        await message.channel.send(embed=responseEmbed)

    async def request(self, message, messageList, generatePdfController):
        
        filename = str(uuid.uuid1())

        responseList = generatePdfController.handle(json.dumps({
            "disciplina": messageList[2],
            "ramo": messageList[3],
            "filename": filename
        }))
       
        if (responseList["status"] == True):
            
            file = self.discord.File(f"build/{filename}.pdf")
            
            embed = self.discord.Embed(title=responseList["data"], color=self.successColor)
            embed.set_footer(text="Atenção: os arquivos ficam disponíveis por um curto período de tempo")

            await message.channel.send(embed=embed, file=file)

        else:
            errorEmbed = self.discord.Embed(title=responseList["data"], color=self.dangerColor)
            await message.channel.send(embed=errorEmbed)

