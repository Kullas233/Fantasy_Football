import os
from glob import glob
import pandas as pd
import re

byeWeeks = 'byeWeeks = { "ARI":, "ATL":, "BAL":, "BUF":7, "CAR":, "CHI":, "CIN":, "CLE":, "DAL":, "DEN":, "DET":, "Dumb":0, "FA":0, "GB":, "HOU":, "IND":, "JAX":, "KC":, "LAC":, "LAR":, "LV":, "MIA":, "MIN":, "NE":, "NO":, "NYG":, "NYJ":, "PHI":, "PIT":, "SEA":, "SF":, "TB":, "TEN":, "WAS": }'

csv = pd.read_csv('Fantasy_Football_26/data/rotow/data.csv')
for index, row in csv.iterrows():
    if(byeWeeks.__contains__(row['Team']) and not re.search(row['Team']+'":[0-9]', byeWeeks)):
        index = byeWeeks.find(row['Team'])
        byeWeeks = byeWeeks[:index + len(row['Team'])+2] + str(row['Bye']) + byeWeeks[index + len(row['Team']) + 2:]
    else:
        print("Missing team: " + row['Team'])

print(byeWeeks)