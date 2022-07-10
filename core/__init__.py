from .database.mongo import database

from .controllers.InsertQuestionController import InsertQuestionController
from .controllers.GeneratePdfController import GeneratePdfController

insertQuestionController = InsertQuestionController(database)
generatePdfController = GeneratePdfController(database)

