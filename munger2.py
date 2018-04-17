#!/usr/bin/env python3

import csv
import json


def makeDictFromCsv(filename: str) -> dict:
    d = {}
    with open(filename, encoding='utf-8-sig') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            d[row['Id']] = dict(row)
    return d


def enrichRow(row: dict, enrichers: list) -> None:
    for enrichment in enrichers:
        if row['Id'] in enrichment:
            otherRow = enrichment[row['Id']]
    if otherRow:
        for key in otherRow.keys():
            if otherRow[key]:
                row[key] = otherRow[key]


# Read everything into memory
languages = makeDictFromCsv('iso-639-3_Name_Index_20180123.tab')

# Create the list of enrichers
enrichers = [
    makeDictFromCsv('iso-639-3_20180123.tab'),
    makeDictFromCsv('iso-639-3_Retirements_20180123.tab'),
    makeDictFromCsv('iso-639-3-macrolanguages_20180123.tab')
]

# Enrich with vitamins and minerals :)
for id_, row in languages.items():
    enrichRow(row, enrichers)

# Write to json file
with open('languages.json', 'w') as outfile:
    json.dump(languages, outfile, indent=4, sort_keys=True, ensure_ascii=False)
