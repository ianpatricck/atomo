import json

class InsertQuestionController:
    
    def __init__(self, mongoProvider):
        self.mongoProvider = mongoProvider

    def handle(self, data):

        questionSentData = json.loads(data)

        # Verifica se o objeto enviado está vázio
        if (len(questionSentData) == 0):
            return {
                "status": False,
                "data": "Campos enviados estão vázios"
            }

        for key, value in questionSentData.items():
            if (value == "" or len(value) == 0 or value == None):
                return {
                    "status": False,
                    "data": "Algo deu errado"
                }

        questionsCol = self.mongoProvider["questions"]
        questionsCol.insert_one(questionSentData)

        return {
            "status": True,
            "data": "Questão enviada com sucesso"
        } 
