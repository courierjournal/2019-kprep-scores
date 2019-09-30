import pandas as pd
import json
import hashlib


"""
This script processes the raw data provided by KDE and outputs a
csv and json file we can use in the app.
"""

# If a school doesn't have elementary, middle, high in it append it to the name


def getNameLabel(name, level):
    level = level.lower()
    labels = {"es": "Elementary", "ms": "Middle", "hs": "High"}
    if not labels[level] in name:
        if level == "hs":
            return name + " (High School)"
        else:
            return name + " (" + labels[level] + ")"
    else:
        return name

# Create a real uid for each school


def getUid(arr):
    strToHash = arr
    if type(arr) == list:
        strToHash = ''.join(str(e) for e in arr)
    newHash = int(hashlib.sha256(strToHash.encode('utf-8')).hexdigest(), 16)
    return str(newHash)


# ********************************************************
# CREATE AN INITIAL LIST OF SCHOOLS INCLUDING STAR RATING
# ********************************************************
# Options:
sourceFile = "../raw-data/All_SRC_Embargo_Datasets_2019/ACCOUNTABILITY_PROFILE.xlsx"
sourceSheet = "DATA"
includeDistricts = False

df = pd.read_excel(sourceFile, sheet_name=sourceSheet)
schoolListRaw = json.loads(
    df.where((pd.notnull(df)), None).to_json(orient='records'))
schoolListJson = []
for school in schoolListRaw:
    if type(school["STARS"]) is int:
        if includeDistricts == False and school['STATE_SCH_ID'] != None:
            schoolListJson.append(
                {
                    "id": school["STATE_SCH_ID"],
                    "uid": getUid([school['SCH_NAME'], school['LEVEL'], school['STATE_SCH_ID']]),
                    "name": school["SCH_NAME"],
                    "nameLabel": getNameLabel(school['SCH_NAME'], school['LEVEL']),
                    "level": school["LEVEL"],
                    "stars": school["STARS"],
                    "county": school["CNTYNAME"],
                    "district": school["DIST_NAME"],
                    "classification": school["FED_CLASS"],
                    "classificationReason": school["REASON"]
                }
            )


# *************************
# EXTRACT SCHOOL META DATA
# *************************
# Options
sourceFile = "../raw-data/All_SRC_Embargo_Datasets_2019/DISTRICT_SCHOOL_LIST.xlsx"
sourceSheet = "DATA"

df = pd.read_excel(sourceFile, sheet_name=sourceSheet)
schoolMetaListRaw = json.loads(
    df.where((pd.notnull(df)), None).to_json(orient='records'))
schoolMetaListJson = []
for school in schoolMetaListRaw:
    schoolMetaListJson.append(
        {
            "id": school["STATE_SCH_ID"],
            "lat": school["LATITUDE"],
            "lng": school["LONGITUDE"],
            "address": school["ADDRESS"]
        }
    )

# ******************
# EXTRACT GRAD RATE
# ******************
# Options
sourceFile = "../raw-data/All_SRC_Embargo_Datasets_2019/GRADUATION_RATE.xlsx"
sourceSheet = "DATA"

df = pd.read_excel(sourceFile, sheet_name=sourceSheet)
gradRateRaw = json.loads(
    df.where((pd.notnull(df)), None).to_json(orient='records'))
gradRateJson = []
for school in gradRateRaw:
    if school['DEMOGRAPHIC'] == "TST":
        gradRateJson.append({
            "uid": getUid([school['SCH_NAME'], "HS", school['STATE_SCH_ID']]),
            "gradRate": school['GRADRATE4YR']
        })


# *********************************
# CONVERT THE DICTS TO A DATAFRAME
# *********************************
# Options
dictList = ["schoolListJson", "schoolMetaListJson", "gradRateJson"]

df = {}
for item in dictList:
    df[item] = pd.DataFrame.from_dict(eval(item), orient="columns")


# *******************************************
# MERGE THE DATAFRAMES BASED ON A COMMON KEY
# *******************************************
result = df["schoolListJson"].merge(df["schoolMetaListJson"], on="id")
result = result.merge(df["gradRateJson"], how="left", on="uid")


# WRITE CSV OUTPUT FOR DEBUGGING
outputFile = "../raw-data/processed.csv"
result.to_csv(outputFile)


# WRITE PRIMARY DATA FILE
outputFile = "../src/data/2019-kprep-scores.json"
output = []
for index, school in result.transpose().to_dict().items():
    output.append(
        {
            "n": school["name"],
            "d": school["district"],
            "s": school["stars"],
            "c": school["classification"],
            "r": school["classificationReason"],
            "t": [],
        }
    )


with open(outputFile, "w") as f:
    json.dump(output, f)
