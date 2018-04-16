import csv
import glob

path = "iso-639-3*.tab"
for filename in glob.glob(path):
    with open(filename, 'r') as isoFile:
        sheetreader = csv.reader(isoFile, delimiter='\t')
        print("------------")
        for row in sheetreader:
            print(row)
