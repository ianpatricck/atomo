class ListController:
    
    def __init__(self, mongoProvider):
        self.mongoProvider = mongoProvider

    def handle(self):
        
        try:
           
            results = {}

            for discipline in self.mongoProvider["disciplines"].find({}, { "_id": 0, "tag": 0 }):
                if not discipline["name"] in results:
                    results[discipline["name"]] = []
            
            for branch in self.mongoProvider["branches"].find({}, { "_id": 0, "tag": 0 }):
                for discipline in self.mongoProvider["disciplines"].find({}, { "_id": 0 }):
                    if (discipline["tag"] == branch["discipline_tag"]):
                        results[discipline["name"]].append(branch["name"])

            return {
                "status": True,
                "data": results
            }

        except:
            return {
                "status": False,
                "data": "Não foi possível realizar a ação"
            }
