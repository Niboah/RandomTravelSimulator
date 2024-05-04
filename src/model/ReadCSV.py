
import pandas as pd

cityBetween = dict()

personFlying = {"" , "", ""}
dailyFlyer = []
allFlyer = []
file_path = 'hackupc-travelperk-dataset.csv'
unique_cities = ['Amsterdam', 'Barcelona', 'Berlin', 'Brussels', 'Budapest', 'Dublin', 'Florence', 
                 'Lisbon', 'London', 'Madrid', 'Milan', 'Munich', 'Paris', 'Prague', 'Rome', 'Vienna', 'Zurich']
# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

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

# Output the unique categories
# for idx, category in enumerate(union_list):
#     print(str(idx + 1)+ " " + category)

# exit()
dias = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def dailyAction():
    exit()

def compareDate(date1, date2):
    mes1 = date1[2:3]
    mes2 = date2[2:3]
    dia1 = date1[0:1]
    dia2 = date2[0:1]
    if mes1 == mes2 and dia1 == dia2:
        return 0
    elif mes1 > mes2 or (mes1 == mes2 or dia1 > dia2):
        return 1
    elif mes1 < mes2 or (mes1 == mes2 or dia1 < dia2):
        return -1

def DailyIteration(cityMiddle):
    # Replace 'your_file.csv' with the path to your CSV file
    file_path = 'hackupc-travelperk-dataset.csv'
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    cityDict = {key: 0 for key in union_list}
    cityPersonDict = {key: set() for key in union_list}
    EveryDay = list()
    EveryDayPerson = list()
    for idx, i in enumerate(dias):
        for j in range(i):
            #print("2024" + str(idx+1) + str(j + 1))
            for index, row in df.iterrows():
                comp = compareDate(row["Departure Date"].replace(" ", ""), str(j + 1) + str(idx+1) + "2024")
                if(comp == 0):
                    print("Flying")
                    personFlying[0] = row["Traveller Name"]
                    personFlying[1] = row["Departure City"]
                    personFlying[2] = row["Arrival City"]
                    for it in cityMiddle[row["Departure City"]+row["Arrival City"]]:
                        cityDict[unique_cities[it-1]] += 1
                elif(comp == 1):
                    print("Check return date")
                    recomp = compareDate(row["Return Date"].replace(" ", ""), str(j + 1) + str(idx+1) + "2024")
                    if(recomp == 0):
                        print("Flying Back")
                        personFlying[0] = row["Traveller Name"]
                        personFlying[1] = row["Arrival City"]
                        personFlying[2] = row["Departure City"]
                        for it in cityMiddle[row["Departure City"]+row["Arrival City"]]:
                            cityDict[unique_cities[it-1]] += 1
                    elif(recomp == -1):
                        print("Staying at foraign place")
                        cityDict[row["Arrival City"]] = cityDict[row["Arrival City"]] + 1
                        cityPersonDict[row["Arrival City"]].add(row["Traveller Name"])
                    elif(recomp == 1):
                        print("Already came back to my place")
                        cityDict[row["Departure City"]] = cityDict[row["Departure City"]] + 1
                        cityPersonDict[row["Departure City"]].add(row["Traveller Name"])
                elif(comp == -1):
                    print("Stay at original place")
                    cityDict[row["Departure City"]] = cityDict[row["Departure City"]] + 1
                    cityPersonDict[row["Departure City"]].add(row["Traveller Name"])
                dailyFlyer.append(personFlying)
                personFlying = {"","",""}
            EveryDay.append(cityDict)
            EveryDayPerson.append(cityPersonDict)
            allFlyer.append(dailyFlyer)
            dailyFlyer=[]
            for key in cityDict:
                cityDict[key] = 0
            for key in cityPersonDict:
                cityPersonDict[key] = 0
    return [EveryDay,EveryDayPerson,allFlyer]
        
    