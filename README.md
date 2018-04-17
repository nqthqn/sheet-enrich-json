# sheet-enrich-json

  - This script reads in data/iso-639-3_Name_Index_20180123.tab
  - It converts this to a dict of dicts (with languages codes as the keys)
  - It then "enriches" each dict by pulling in columns from other CSVs with matching Id's
  - Finally it writes this dict to a file; "languages.json"
