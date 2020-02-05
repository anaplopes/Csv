from work_csv import WorkCsv

if __name__ == '__main__':
    csv = 'file.csv'
    WorkCsv(csv).create_json('file.json')
    WorkCsv(csv).insertmany_mongo('db_name', 'collection_name')
    print('Finished')
