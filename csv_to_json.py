import csv, json


class Csv:
    
    def __init__(self):
        self.csvFilePath = 'csvFilePath.csv'
        self.jsonFilePath = 'jsonFilePath.json'
        
    def read_csv(self):
        with open(self.csvFilePath, newline='', encoding='utf-8') as csvFile:
            csvRead = csv.reader(csvFile, delimiter=';')
            data = []
            
            for row in csvRead:
                data.append({
                    "a": row[0],
                    "b": row[1],
                    "c": row[2],
                    "d": row[3],
                    "e":row[4]
                    })
                
            print('Finished')
            return data

    def create_json(self):
        with open(self.jsonFilePath, 'w') as jsonFile:
            jsonFile.write(json.dumps(data, indent=4))
