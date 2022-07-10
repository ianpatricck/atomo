import json

from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from random import randint

class GeneratePdfController:

    def __init__(self, mongoProvider):
        self.mongoProvider = mongoProvider

    def handle(self, data):  

        data = json.loads(data)

        filename = data["ramo"]
        
        # Extensão da classe Canvas para o arquivo
        file = canvas.Canvas(f"build/{filename}.pdf")

        discipline = self.mongoProvider["disciplines"].find_one({ "tag": data["disciplina"] })
        branch = self.mongoProvider["branches"].find_one({ "tag": data["ramo"] })

        if ((discipline == None or discipline == len(discipline) == 0) or (branch == None or len(branch) == 0)):
            return {
                "status": False,
                "data": "Objeto não encontrato ou inexistente"
            }

        file.setTitle("Devst - " + discipline["name"])
    
        # Cordenadas das linhas para separar o documento
        oLine = [0, 700, 600, 700]

        file.setStrokeColor("gray")
        file.setLineWidth(.1)

        file.line(oLine[0], oLine[1], oLine[2], oLine[3])

        # Faz o desenho do cabeçalho do arquivo
        self.__drawFileHeader(file, discipline, branch)

        # Busca as questões por meio do dado passado e as desenha em ordem
        self.__drawFileBody(file, data)

        file.showPage()
        file.save()

        return {
            "status": True,
            "data": "Arquivo gerado com sucesso!"
        }

    def __drawFileHeader(self, file, discipline, branch): 
      
        # Ícone do arquivo
        file.drawInlineImage(f"assets/devst.png", 80, 760, 50, 50)

        # Título da disciplína
        file.setFont("Courier", 20)
        file.drawCentredString(300, 760, discipline["name"])

        file.setFont("Courier", 15)
        file.drawCentredString(300, 740, branch["name"])

    def __drawFileBody(self, file, data):

        questions = []

        # Busca as questões relacionadas com a disciplína e ramo desejado e aloca em uma lista
        [questions.append(question) for question in self.mongoProvider["questions"].find({ "disciplina": data["disciplina"], "ramo": data["ramo"] })]
    
        randQuestions = []

        # Verifica se existe questões repetidas
        count = 0
        
        while (len(randQuestions) != 4):
            rand = randint(0, len(questions) - 1)
        
            if questions[rand] not in randQuestions:
                randQuestions.append(questions[rand])

            count = count + 1

        rightInitialTextPosX = 10
        rightInitialTextPosY = 580 

        # Desenha as questões no arquivo
        for index, item in enumerate(randQuestions, 1):
 
            paragraphQuestion = Paragraph(str(index) + " - " + item["enunciado"] + "<br/><br/>" + "<br/>".join(item["alternativas"]))
            paragraphQuestion.wrapOn(file, 500, 500)
            paragraphQuestion.drawOn(file, rightInitialTextPosX, rightInitialTextPosY) 

            rightInitialTextPosY-=150

        feedback = []

        # Gabarito
        for index, item in enumerate(randQuestions, 1):
            feedback.append(str(index) + " - " + item["gabarito"])
       
        paragraphQuestion = Paragraph(" | ".join(feedback))
        paragraphQuestion.wrapOn(file, 150, 80)
        paragraphQuestion.drawOn(file, 450, 20)
