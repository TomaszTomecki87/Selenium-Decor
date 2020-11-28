import csv

def getCSVData(fileName):
    rows = []
    dataFile = open(fileName, 'r')
    reader = csv.reader(dataFile)
    next(reader)
    for i in reader:
        rows.append(i)
    return rows