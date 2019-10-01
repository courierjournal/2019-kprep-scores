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
                    "starScore": school["OVERALL_SCORE"],
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


# **********************
# TRANSITION READY RATE
# **********************
sourceFile = "../raw-data/All_SRC_Embargo_Datasets_2019/TRANSITION_READINESS_ACCOUNTABILITY.xlsx"
sourceSheet = "DATA"
# Demographic = TST, Col = TRANSITIONRATE

df = pd.read_excel(sourceFile, sheet_name=sourceSheet)
transitionReadyRateRaw = json.loads(
    df.where((pd.notnull(df)), None).to_json(orient='records'))
transitionReadyRateJson = []
for school in transitionReadyRateRaw:
    if school['DEMOGRAPHIC'] == "TST":
        transitionReadyRateJson.append({
            "uid": getUid([school['SCH_NAME'], "HS", school['STATE_SCH_ID']]),
            "transitionReadyRate": school['TRANSITIONRATE']
        })


# ***************************
# ACCOUNTABILITY SCORES 2019
# ***************************
sourceFile = "../raw-data/All_SRC_Embargo_Datasets_2019/ACCOUNTABILITY_PROFICIENCY_LEVEL.xlsx"
sourceSheet = "DATA"

df = pd.read_excel(sourceFile, sheet_name=sourceSheet)
raw = json.loads(
    df.where((pd.notnull(df)), None).to_json(orient='records'))
# 2019 Reading
readingTotal2019 = []
readingWhite2019 = []
readingBlack2019 = []
readingNonFrl2019 = []
readingFrl2019 = []
readingNonEsl2019 = []
readingEsl2019 = []
readingNonSe2019 = []
readingSe2019 = []
# 2019 Math
mathTotal2019 = []
mathWhite2019 = []
mathBlack2019 = []
mathNonFrl2019 = []
mathFrl2019 = []
mathNonEsl2019 = []
mathEsl2019 = []
mathNonSe2019 = []
mathSe2019 = []

for school in raw:
    if school['SUBJECT'] == "RD":
        if school['DEMOGRAPHIC'] == "TST":
            readingTotal2019.append({
                "uid": getUid([school['SCH_NAME'], school['LEVEL'], school['STATE_SCH_ID']]),
                "readingTotal2019": school['PROFICIENT_DISTINGUISHED']
            })
        if school['DEMOGRAPHIC'] == "ETW":
            readingWhite2019.append({
                "uid": getUid([school['SCH_NAME'], school['LEVEL'], school['STATE_SCH_ID']]),
                "readingWhite2019": school['PROFICIENT_DISTINGUISHED']
            })
        if school['DEMOGRAPHIC'] == "ETB":
            readingBlack2019.append({
                "uid": getUid([school['SCH_NAME'], school['LEVEL'], school['STATE_SCH_ID']]),
                "readingBlack2019": school['PROFICIENT_DISTINGUISHED']
            })
        if school['DEMOGRAPHIC'] == "LUN":
            readingNonFrl2019.append({
                "uid": getUid([school['SCH_NAME'], school['LEVEL'], school['STATE_SCH_ID']]),
                "readingNonFrl2019": school['PROFICIENT_DISTINGUISHED']
            })
        if school['DEMOGRAPHIC'] == "LUP":
            readingFrl2019.append({
                "uid": getUid([school['SCH_NAME'], school['LEVEL'], school['STATE_SCH_ID']]),
                "readingFrl2019": school['PROFICIENT_DISTINGUISHED']
            })
        if school['DEMOGRAPHIC'] == "LEN":
            readingNonEsl2019.append({
                "uid": getUid([school['SCH_NAME'], school['LEVEL'], school['STATE_SCH_ID']]),
                "readingNonEsl2019": school['PROFICIENT_DISTINGUISHED']
            })
        if school['DEMOGRAPHIC'] == "LEP":
            readingEsl2019.append({
                "uid": getUid([school['SCH_NAME'], school['LEVEL'], school['STATE_SCH_ID']]),
                "readingEsl2019": school['PROFICIENT_DISTINGUISHED']
            })
        if school['DEMOGRAPHIC'] == "ACO":
            readingNonSe2019.append({
                "uid": getUid([school['SCH_NAME'], school['LEVEL'], school['STATE_SCH_ID']]),
                "readingNonSe2019": school['PROFICIENT_DISTINGUISHED']
            })
        if school['DEMOGRAPHIC'] == "ETW":
            readingSe2019.append({
                "uid": getUid([school['SCH_NAME'], school['LEVEL'], school['STATE_SCH_ID']]),
                "readingSe2019": school['PROFICIENT_DISTINGUISHED']
            })
    if school['SUBJECT'] == "MA":
        if school['DEMOGRAPHIC'] == "TST":
            mathTotal2019.append({
                "uid": getUid([school['SCH_NAME'], school['LEVEL'], school['STATE_SCH_ID']]),
                "mathTotal2019": school['PROFICIENT_DISTINGUISHED']
            })
        if school['DEMOGRAPHIC'] == "ETW":
            mathWhite2019.append({
                "uid": getUid([school['SCH_NAME'], school['LEVEL'], school['STATE_SCH_ID']]),
                "mathWhite2019": school['PROFICIENT_DISTINGUISHED']
            })
        if school['DEMOGRAPHIC'] == "ETB":
            mathBlack2019.append({
                "uid": getUid([school['SCH_NAME'], school['LEVEL'], school['STATE_SCH_ID']]),
                "mathBlack2019": school['PROFICIENT_DISTINGUISHED']
            })
        if school['DEMOGRAPHIC'] == "LUN":
            mathNonFrl2019.append({
                "uid": getUid([school['SCH_NAME'], school['LEVEL'], school['STATE_SCH_ID']]),
                "mathNonFrl2019": school['PROFICIENT_DISTINGUISHED']
            })
        if school['DEMOGRAPHIC'] == "LUP":
            mathFrl2019.append({
                "uid": getUid([school['SCH_NAME'], school['LEVEL'], school['STATE_SCH_ID']]),
                "mathFrl2019": school['PROFICIENT_DISTINGUISHED']
            })
        if school['DEMOGRAPHIC'] == "LEN":
            mathNonEsl2019.append({
                "uid": getUid([school['SCH_NAME'], school['LEVEL'], school['STATE_SCH_ID']]),
                "mathNonEsl2019": school['PROFICIENT_DISTINGUISHED']
            })
        if school['DEMOGRAPHIC'] == "LEP":
            mathEsl2019.append({
                "uid": getUid([school['SCH_NAME'], school['LEVEL'], school['STATE_SCH_ID']]),
                "mathEsl2019": school['PROFICIENT_DISTINGUISHED']
            })
        if school['DEMOGRAPHIC'] == "ACO":
            mathNonSe2019.append({
                "uid": getUid([school['SCH_NAME'], school['LEVEL'], school['STATE_SCH_ID']]),
                "mathNonSe2019": school['PROFICIENT_DISTINGUISHED']
            })
        if school['DEMOGRAPHIC'] == "ETW":
            mathSe2019.append({
                "uid": getUid([school['SCH_NAME'], school['LEVEL'], school['STATE_SCH_ID']]),
                "mathSe2019": school['PROFICIENT_DISTINGUISHED']
            })


# ***************************
# ACCOUNTABILITY SCORES 2018
# ***************************
sourceFile = "../raw-data/All_SRC_Embargo_Datasets_2019/ACCOUNTABILITY_PROFICIENCY_LEVEL_2018.xlsx"
sourceSheet = "DATA"

df = pd.read_excel(sourceFile, sheet_name=sourceSheet)
raw = json.loads(
    df.where((pd.notnull(df)), None).to_json(orient='records'))
# 2018 Reading
readingTotal2018 = []
readingWhite2018 = []
readingBlack2018 = []
readingNonFrl2018 = []
readingFrl2018 = []
readingNonEsl2018 = []
readingEsl2018 = []
readingNonSe2018 = []
readingSe2018 = []
# 2018 Math
mathTotal2018 = []
mathWhite2018 = []
mathBlack2018 = []
mathNonFrl2018 = []
mathFrl2018 = []
mathNonEsl2018 = []
mathEsl2018 = []
mathNonSe2018 = []
mathSe2018 = []

for school in raw:
    if school['SUBJECT'] == "RD":
        if school['DEMOGRAPHIC'] == "TST":
            readingTotal2018.append({
                "uid": getUid([school['SCH_NAME'], school['LEVEL'], school['STATE_SCH_ID']]),
                "readingTotal2018": school['PROFICIENT_DISTINGUISHED']
            })
        if school['DEMOGRAPHIC'] == "ETW":
            readingWhite2018.append({
                "uid": getUid([school['SCH_NAME'], school['LEVEL'], school['STATE_SCH_ID']]),
                "readingWhite2018": school['PROFICIENT_DISTINGUISHED']
            })
        if school['DEMOGRAPHIC'] == "ETB":
            readingBlack2018.append({
                "uid": getUid([school['SCH_NAME'], school['LEVEL'], school['STATE_SCH_ID']]),
                "readingBlack2018": school['PROFICIENT_DISTINGUISHED']
            })
        if school['DEMOGRAPHIC'] == "LUN":
            readingNonFrl2018.append({
                "uid": getUid([school['SCH_NAME'], school['LEVEL'], school['STATE_SCH_ID']]),
                "readingNonFrl2018": school['PROFICIENT_DISTINGUISHED']
            })
        if school['DEMOGRAPHIC'] == "LUP":
            readingFrl2018.append({
                "uid": getUid([school['SCH_NAME'], school['LEVEL'], school['STATE_SCH_ID']]),
                "readingFrl2018": school['PROFICIENT_DISTINGUISHED']
            })
        if school['DEMOGRAPHIC'] == "LEN":
            readingNonEsl2018.append({
                "uid": getUid([school['SCH_NAME'], school['LEVEL'], school['STATE_SCH_ID']]),
                "readingNonEsl2018": school['PROFICIENT_DISTINGUISHED']
            })
        if school['DEMOGRAPHIC'] == "LEP":
            readingEsl2018.append({
                "uid": getUid([school['SCH_NAME'], school['LEVEL'], school['STATE_SCH_ID']]),
                "readingEsl2018": school['PROFICIENT_DISTINGUISHED']
            })
        if school['DEMOGRAPHIC'] == "ACO":
            readingNonSe2018.append({
                "uid": getUid([school['SCH_NAME'], school['LEVEL'], school['STATE_SCH_ID']]),
                "readingNonSe2018": school['PROFICIENT_DISTINGUISHED']
            })
        if school['DEMOGRAPHIC'] == "ETW":
            readingSe2018.append({
                "uid": getUid([school['SCH_NAME'], school['LEVEL'], school['STATE_SCH_ID']]),
                "readingSe2018": school['PROFICIENT_DISTINGUISHED']
            })
    if school['SUBJECT'] == "MA":
        if school['DEMOGRAPHIC'] == "TST":
            mathTotal2018.append({
                "uid": getUid([school['SCH_NAME'], school['LEVEL'], school['STATE_SCH_ID']]),
                "mathTotal2018": school['PROFICIENT_DISTINGUISHED']
            })
        if school['DEMOGRAPHIC'] == "ETW":
            mathWhite2018.append({
                "uid": getUid([school['SCH_NAME'], school['LEVEL'], school['STATE_SCH_ID']]),
                "mathWhite2018": school['PROFICIENT_DISTINGUISHED']
            })
        if school['DEMOGRAPHIC'] == "ETB":
            mathBlack2018.append({
                "uid": getUid([school['SCH_NAME'], school['LEVEL'], school['STATE_SCH_ID']]),
                "mathBlack2018": school['PROFICIENT_DISTINGUISHED']
            })
        if school['DEMOGRAPHIC'] == "LUN":
            mathNonFrl2018.append({
                "uid": getUid([school['SCH_NAME'], school['LEVEL'], school['STATE_SCH_ID']]),
                "mathNonFrl2018": school['PROFICIENT_DISTINGUISHED']
            })
        if school['DEMOGRAPHIC'] == "LUP":
            mathFrl2018.append({
                "uid": getUid([school['SCH_NAME'], school['LEVEL'], school['STATE_SCH_ID']]),
                "mathFrl2018": school['PROFICIENT_DISTINGUISHED']
            })
        if school['DEMOGRAPHIC'] == "LEN":
            mathNonEsl2018.append({
                "uid": getUid([school['SCH_NAME'], school['LEVEL'], school['STATE_SCH_ID']]),
                "mathNonEsl2018": school['PROFICIENT_DISTINGUISHED']
            })
        if school['DEMOGRAPHIC'] == "LEP":
            mathEsl2018.append({
                "uid": getUid([school['SCH_NAME'], school['LEVEL'], school['STATE_SCH_ID']]),
                "mathEsl2018": school['PROFICIENT_DISTINGUISHED']
            })
        if school['DEMOGRAPHIC'] == "ACO":
            mathNonSe2018.append({
                "uid": getUid([school['SCH_NAME'], school['LEVEL'], school['STATE_SCH_ID']]),
                "mathNonSe2018": school['PROFICIENT_DISTINGUISHED']
            })
        if school['DEMOGRAPHIC'] == "ETW":
            mathSe2018.append({
                "uid": getUid([school['SCH_NAME'], school['LEVEL'], school['STATE_SCH_ID']]),
                "mathSe2018": school['PROFICIENT_DISTINGUISHED']
            })


# *********************************
# CONVERT THE DICTS TO A DATAFRAME
# *********************************
# Options
dictList = ["schoolListJson", "schoolMetaListJson",
            "gradRateJson", "transitionReadyRateJson",
            "readingTotal2019",
            "readingWhite2019",
            "readingBlack2019",
            "readingNonFrl2019",
            "readingFrl2019",
            "readingNonEsl2019",
            "readingEsl2019",
            "readingNonSe2019",
            "readingSe2019",
            "mathTotal2019",
            "mathWhite2019",
            "mathBlack2019",
            "mathNonFrl2019",
            "mathFrl2019",
            "mathNonEsl2019",
            "mathEsl2019",
            "mathNonSe2019",
            "mathSe2019",
            "readingTotal2018",
            "readingWhite2018",
            "readingBlack2018",
            "readingNonFrl2018",
            "readingFrl2018",
            "readingNonEsl2018",
            "readingEsl2018",
            "readingNonSe2018",
            "readingSe2018",
            "mathTotal2018",
            "mathWhite2018",
            "mathBlack2018",
            "mathNonFrl2018",
            "mathFrl2018",
            "mathNonEsl2018",
            "mathEsl2018",
            "mathNonSe2018",
            "mathSe2018"]

df = {}
for item in dictList:
    df[item] = pd.DataFrame.from_dict(eval(item), orient="columns")

# *******************************************
# MERGE THE DATAFRAMES BASED ON A COMMON KEY
# *******************************************
result = df["schoolListJson"].merge(df["schoolMetaListJson"], on="id")
result = result.merge(df["gradRateJson"], how="left", on="uid")
result = result.merge(df["transitionReadyRateJson"], how="left", on="uid")
for i in range(4, len(dictList)):
    result = result.merge(df[dictList[i]], how="left", on="uid")

# *************************************
# CALCULATE DIFF BETWEEN 2018 AND 2019
# *************************************
result = result.assign(
    readingTotalDiff=result['readingTotal2019'] - result['readingTotal2018'])
result = result.assign(
    readingWhiteDiff=result['readingWhite2019'] - result['readingWhite2018'])
result = result.assign(
    readingBlackDiff=result['readingBlack2019'] - result['readingBlack2018'])
result = result.assign(
    readingNonFrlDiff=result['readingNonFrl2019'] - result['readingNonFrl2018'])
result = result.assign(
    readingFrlDiff=result['readingFrl2019'] - result['readingFrl2018'])
result = result.assign(
    readingNonEslDiff=result['readingNonEsl2019'] - result['readingNonEsl2018'])
result = result.assign(
    readingEslDiff=result['readingEsl2019'] - result['readingEsl2018'])
result = result.assign(
    readingNonSeDiff=result['readingNonSe2019'] - result['readingNonSe2018'])
result = result.assign(
    readingSeDiff=result['readingSe2019'] - result['readingSe2018'])
result = result.assign(
    mathTotalDiff=result['mathTotal2019'] - result['mathTotal2018'])
result = result.assign(
    mathWhiteDiff=result['mathWhite2019'] - result['mathWhite2018'])
result = result.assign(
    mathBlackDiff=result['mathBlack2019'] - result['mathBlack2018'])
result = result.assign(
    mathNonFrlDiff=result['mathNonFrl2019'] - result['mathNonFrl2018'])
result = result.assign(
    mathFrlDiff=result['mathFrl2019'] - result['mathFrl2018'])
result = result.assign(
    mathNonEslDiff=result['mathNonEsl2019'] - result['mathNonEsl2018'])
result = result.assign(
    mathEslDiff=result['mathEsl2019'] - result['mathEsl2018'])
result = result.assign(
    mathNonSeDiff=result['mathNonSe2019'] - result['mathNonSe2018'])
result = result.assign(mathSeDiff=result['mathSe2019'] - result['mathSe2018'])


# ROUND FLOATS
result = result.round(decimals=1)

# WRITE CSV OUTPUT FOR DEBUGGING
outputFile = "../raw-data/processed.csv"
result.to_csv(outputFile)


# WRITE PRIMARY DATA FILE
outputFile = "../src/data/2019-kprep-scores.json"
finalOut = json.loads(
    result.where((pd.notnull(result)), None).to_json(orient='records'))
output = []
for school in finalOut:
    output.append(
        {
            "n": school["nameLabel"],
            "d": school["district"],
            "s": school["stars"],
            "ss": school["starScore"],
            "c": school["classification"],
            "r": school["classificationReason"],
            "hs": {"g": school["gradRate"],
                   "t": school["transitionReadyRate"]},
            "t": [[
                school['readingTotal2019'],
                school['readingWhite2019'],
                school['readingBlack2019'],
                school['readingNonFrl2019'],
                school['readingFrl2019'],
                school['readingNonEsl2019'],
                school['readingEsl2019'],
                school['readingNonSe2019'],
                school['readingSe2019']
            ], [
                school['mathTotal2019'],
                school['mathWhite2019'],
                school['mathBlack2019'],
                school['mathNonFrl2019'],
                school['mathFrl2019'],
                school['mathNonEsl2019'],
                school['mathEsl2019'],
                school['mathNonSe2019'],
                school['mathSe2019']
            ], [
                school['readingTotalDiff'],
                school['readingWhiteDiff'],
                school['readingBlackDiff'],
                school['readingNonFrlDiff'],
                school['readingFrlDiff'],
                school['readingNonEslDiff'],
                school['readingEslDiff'],
                school['readingNonSeDiff'],
                school['readingSeDiff']
            ], [
                school['mathTotalDiff'],
                school['mathWhiteDiff'],
                school['mathBlackDiff'],
                school['mathNonFrlDiff'],
                school['mathFrlDiff'],
                school['mathNonEslDiff'],
                school['mathEslDiff'],
                school['mathNonSeDiff'],
                school['mathSeDiff']
            ]
            ],
        }
    )


with open(outputFile, "w") as f:
    json.dump(output, f)
