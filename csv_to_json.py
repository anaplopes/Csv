import csv, json


class Csv:
    
    def __init__(self, csvFilePath, jsonFilePath):
        self.csvFilePath = csvFilePath
        self.jsonFilePath = jsonFilePath
        
    def read_csv(self):
        with open(self.csvFilePath, newline='') as csvFile:
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
            jsonFile.write(json.dumps(self.read_csv(), indent=4))


if __name__ == '__main__':
    c = 'path.csv'
    j = 'path.json'
    new = Csv(c, j).create_json()
    