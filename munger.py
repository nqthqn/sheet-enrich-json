## -*- coding: utf-8 -*-

import csv
import json


# Id	Ref_Name	Ret_Reason	Change_To	Ret_Remedy	Effective
retirFileSheet = list(csv.reader(
    open('iso-639-3_Retirements_20180123.tab', encoding='utf-8'), delimiter='\t'))

# Part2B	Part2T	Part1	Scope	Language_Type	Ref_Name	Comment
partsFileSheet = list(csv.reader(
    open('iso-639-3_20180123.tab', encoding='utf-8'), delimiter='\t'))

# Id	Print_Name	Inverted_Name
namesFileSheet = list(csv.reader(
    open('iso-639-3_Name_Index_20180123.tab', encoding='utf-8'), delimiter='\t'))

# M_Id	I_Id	I_Status
macroFileSheet = list(csv.reader(
    open('iso-639-3-macrolanguages_20180123.tab', encoding='utf-8'), delimiter='\t'))

def getRetiredData(child):
    for row in retirFileSheet:
        if child == row[0]:
            return {
                "Ref_Name": row[1],
                "Ret_Reason": row[2],
                "Change_To": row[3],
                "Ret_Remedy": row[4],
                "Effective": row[5]
            }
    return None

def getMacroLang(child):
    for row in macroFileSheet:
        if child == row[1]:
            return {
                "macro": row[0],
                "status": row[2]
            }
    return None


def getCoreData(child):
    for row in partsFileSheet:
        if child == row[0]:
            return {
                "Part2B": row[1],
                "Part2T": row[2],
                "Part1": row[3],
                "Scope": row[4],
                "Language_Type": row[5],
                "Ref_Name": row[6],
                "Comment": row[7]
            }
    return None


langs = []

for row in namesFileSheet:
    iso639_3_id_code = row[0]
    iso639_3_print_name = row[1]
    iso639_3_inverted_name = row[2]

    lang = {
        "ID": iso639_3_id_code,
        "Print_Name": iso639_3_print_name,
        "Inverted_Name": iso639_3_inverted_name
    }

    macro = getMacroLang(lang["ID"])
    if macro:
        lang["Macro"] = macro

    coreData = getCoreData(lang["ID"])
    if coreData and coreData["Part2B"]:
        lang["ISO639-2B"] = coreData["Part2B"]
    if coreData and coreData["Part2T"]:
        lang["ISO639-2T"] = coreData["Part2T"]
    if coreData and coreData["Part1"]:
        lang["ISO639-1"] = coreData["Part1"]
    if coreData and coreData["Scope"]:
        lang["Scope"] = coreData["Scope"]
    if coreData and coreData["Language_Type"]:
        lang["Language_Type"] = coreData["Language_Type"]
    if coreData and coreData["Ref_Name"]:
        lang["Ref_Name"] = coreData["Ref_Name"]
    if coreData and coreData["Comment"]:
        lang["Comment"] = coreData["Comment"]

    retiredData = getRetiredData(lang["ID"])

    if retiredData and retiredData["Ref_Name"]:
        lang["Ref_Name"] = retiredData["Ref_Name"]
    if retiredData and retiredData["Ret_Reason"]:
        lang["Ret_Reason"] = retiredData["Ret_Reason"]
    if retiredData and retiredData["Change_To"]:
        lang["Change_To"] = retiredData["Change_To"]
    if retiredData and retiredData["Ret_Remedy"]:
        lang["Ret_Remedy"] = retiredData["Ret_Remedy"]
    if retiredData and retiredData["Effective"]:
        lang["Effective"] = retiredData["Effective"]

    langs.append(lang)


with open('output.json', 'w') as outfile:
    json.dump(langs, outfile, indent=4, sort_keys=True, ensure_ascii=False)
