import pandas as pd
import json

"""
This script processes the raw data provided by KDE and outputs a
csv and json file we can use in the app.
"""

# CREATE A LIST OF SCHOOLS
# <options>
sourceFile = "../raw-data/All_SRC_Embargo_Datasets_2019/DISTRICT_SCHOOL_LIST.xlsx"
sourceSheet = "DATA"
includeDistrictTotals = True
# </options>

excelData = pd.read_excel(sourceFile, sheet_name=sourceSheet)
schoolListRaw = excelData.transpose().to_dict()
schoolListJson = []
for index, school in schoolListRaw.items():
    if type(school['TITLE1_STATUS']) is str:
        if "Title I Eligible" in school['TITLE1_STATUS']:
            schoolListJson.append({
                "id": school['STATE_SCH_ID'],
                "name": school['SCH_NAME'],
                "county": school['CNTYNAME'],
                "district": school['DIST_NAME'],
                "lat": school['LATITUDE'],
                "lng": school['LONGITUDE']
            })


# EXTRACT STAR RATING
# <options>
sourceFile = "../raw-data/All_SRC_Embargo_Datasets_2019/ACCOUNTABILITY_PROFILE.xlsx"
sourceSheet = "DATA"
# </options>

excelData = pd.read_excel(sourceFile, sheet_name=sourceSheet)
starListRaw = excelData.transpose().to_dict()
starListJson = []
for index, school in starListRaw.items():
    starListJson.append({
        "id": school['STATE_SCH_ID'],
        "stars": school['STARS'],
        "rating": school['PROFICIENCY_RATE'],
        "classification": school['FED_CLASS'],
        "gradRate": school['GRAD_RATE']
    })


# CONVERT THE DICTS TO A DATAFRAME
# <options>
dictList = ["schoolListJson", "starListJson"]
# </options>

df = {}
for item in dictList:
    df[item] = pd.DataFrame.from_dict(eval(item), orient='columns')


# MERGE THE DATAFRAMES BASED ON A COMMON KEY
# <options>
mergeKey = "id"
# </options>

result = df['schoolListJson'].merge(df['starListJson'], on=mergeKey)


# WRITE CSV OUTPUT FOR DEBUGGING
result.to_csv(r'debug.csv')


# WRITE PRIMARY DATA FILE
output = []
for index, school in result.transpose().to_dict().items():
    output.append({
        "n": school['name'],
        "d": school['district'],
        "s": school['stars'],
        "c": school['classification'],
        "t": []
    })


with open('../src/data/2019-kprep-scores.json', 'w') as f:
    json.dump(output, allow_nan= False,f)
