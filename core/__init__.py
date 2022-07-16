from .database.mongo import database

from .controllers.InsertQuestionController import InsertQuestionController
from .controllers.GeneratePdfController import GeneratePdfController
from .controllers.ListController import ListController 

from .api.DiscordProvider import DiscordProvider

insertQuestionController = InsertQuestionController(database)
generatePdfController = GeneratePdfController(database)
listController = ListController(database)

