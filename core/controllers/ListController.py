
class ListController:
    
    def __init__(self, mongoProvider):
        self.mongoProvider = mongoProvider

    def handle(self):
        
        try:
           
            results = []
 
            for item in self.mongoProvider["branches"].find({}, { "_id": 0, "tag": 0 }):
                results.append(item)

            return {
                "status": True,
                "data": results
            }

        except:
            return {
                "status": False,
                "data": "Não foi possível realizar a ação"
            }
