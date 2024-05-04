import pandas as pd
import os


def getCities():
    path = os.path.join(os.curdir,"resource","hackupc-travelperk-dataset.csv")
    data = pd.read_csv(path)
    return set(data["Departure City"]).union(set(data["Arrival City"]))