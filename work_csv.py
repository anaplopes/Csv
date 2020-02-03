import csv, json
from datetime import datetime, date
from connection import ConnectMongo

class WorkCsv:
    
    def __init__(self, csvFilePath):
        self.csvFilePath = csvFilePath
        
    def read_csv(self):
        with open(self.csvFilePath, newline='') as csvFile:
            csvRead = csv.reader(csvFile, delimiter=';')
            data = []

            for row in csvRead:
                data.append({
                    "dsStatus": "disponível",
                    "atendimento": {
                        "cdId":row[0],
                        "dtAtendimento":datetime.strptime(row[1], '%d/%m/%Y'),
                    }
                })
            
            return data

    def insertmany_mongo(self, db, collection):
        conn = ConnectMongo()
        session = conn.connect_db(db, collection)
        return session.insert_many(self.read_csv())


    def create_json(self, jsonFilePath):
        with open(jsonFilePath, 'w', encoding='UTF-8') as jsonFile:
            jsonFile.write(json.dumps(self.read_csv(), indent=4, ensure_ascii=False))
