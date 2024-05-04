
import pandas as pd
import os
import copy

from src.utils.read_file import getCities
path = os.path.join(os.curdir, 'resource','hackupc-travelperk-dataset.csv')

unique_cities = getCities()
unique_cities = list(unique_cities)
# Read the CSV file into a DataFrame
df = pd.read_csv(path)

# Extract the 'Category' column
categories_column = df['Departure City']

# Get unique categories (eliminate repetitions)
unique_categories_departure = categories_column.unique()

# Extract the 'Category' column
categories_column = df['Arrival City']

# Get unique categories (eliminate repetitions)
unique_categories_arrival = categories_column.unique()

# Convert lists to sets and take their union
union_list = list(set(unique_categories_departure) | set(unique_categories_arrival))

dias = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def dailyAction():
    exit()
def compareDate(date1, date2):
    mes1 = date1[2:4]

    mes2 = date2[2:4]

    dia1 = date1[0:2]

    dia2 = date2[0:2]

    if mes1 == mes2 and dia1 == dia2:
        return 0
    elif mes1 > mes2 or (mes1 == mes2 or dia1 > dia2):
        return 1
    elif mes1 < mes2 or (mes1 == mes2 or dia1 < dia2):
        return -1
def DailyIteration(cityMiddle):
    cityBetween = dict()
    personFlying = ["","",""]
    dailyFlyer = []
    allFlyer = []
    dailyFlyer = []
    # Read the CSV file into a DataFrame
    df = pd.read_csv(path)
    cityDict = {key: 0 for key in union_list}
    setlist = set()
    cityPersonDict = {key: setlist for key in union_list}
    EveryDay = list()
    EveryDayPerson = list()
    for idx, i in enumerate(dias):
        for j in range(i):
            #print("2024" + str(idx+1) + str(j + 1))
            for index, row in df.iterrows():
                d = ""
                if j+1 < 10:
                    d+="0"
                    d+=str(j+1)
                else:
                    d+=str(j+1)
                if idx+1 <10:
                    d+="0"
                    d+=str(idx+1)
                else:
                    d+=str(idx+1)
                comp = compareDate(row["Departure Date"].replace("/", ""), d+"2024")
                #print(row["Departure Date"].replace("/", ""))
                #print(d+"2024")
                if(comp == 0):
                    #print("Flying")
                    personFlying[0] = row["Traveller Name"]
                    personFlying[1] = row["Departure City"]
                    personFlying[2] = row["Arrival City"]
                    dailyFlyer.append(copy.deepcopy(personFlying))
                    #print(cityMiddle)
                    for it in cityMiddle[row["Departure City"]+row["Arrival City"]]:
                        cityDict[unique_cities[it-1]] += 1
                elif(comp == 1):
                    #print("Check return date")
                    d = ""
                    if j+1 < 10:
                        d+="0"
                        d+=str(j+1)
                    else:
                        d+=str(j+1)
                    if idx+1 <10:
                        d+="0"
                        d+=str(idx+1)
                    else:
                        d+=str(idx+1)
                    recomp = compareDate(row["Return Date"].replace("/", ""), d+"2024")
                    if(recomp == 0):
                        #print("Flying Back")
                        personFlying[0] = row["Traveller Name"]
                        personFlying[1] = row["Arrival City"]
                        personFlying[2] = row["Departure City"]
                        dailyFlyer.append(copy.deepcopy(personFlying))
                        #print(cityMiddle)
                        for it in cityMiddle[row["Departure City"]+row["Arrival City"]]:
                            cityDict[unique_cities[it-1]] += 1
                    elif(recomp == -1):
                        #print("Staying at foraign place")
                        cityDict[row["Arrival City"]] = cityDict[row["Arrival City"]] + 1
                        cityPersonDict[row["Arrival City"]].add(row["Traveller Name"])
                    elif(recomp == 1):
                        #print("Already came back to my place")
                        cityDict[row["Departure City"]] = cityDict[row["Departure City"]] + 1
                        cityPersonDict[row["Departure City"]].add(row["Traveller Name"])
                elif(comp == -1):
                    #print("Stay at original place")
                    cityDict[row["Departure City"]] = cityDict[row["Departure City"]] + 1
                    cityPersonDict[row["Departure City"]].add(row["Traveller Name"])
                personFlying = ["","",""]
            EveryDay.append(copy.deepcopy(cityDict))
            EveryDayPerson.append(copy.deepcopy(cityPersonDict))
            allFlyer.append(copy.deepcopy(dailyFlyer))
            dailyFlyer=[]
            for key in cityDict:
                cityDict[key] = 0
            for key in cityPersonDict:
                cityPersonDict[key] = set()
    return [EveryDay,EveryDayPerson,allFlyer]
