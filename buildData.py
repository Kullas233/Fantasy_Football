import os
from glob import glob
import pandas as pd
import re

PATH = "data"
EXT = "*.csv"
all_csv_files = [file
                 for path, subdir, files in os.walk(PATH)
                 for file in glob(os.path.join(path, EXT))]
print(all_csv_files)


# def Merge_CSV(files, output):
#     data = []
#     for file in files:
#         data.append(pd.read_csv(file))
#     merge = pd.concat(data)
#     merge.to_csv(output, index=False)

# data = Merge_CSV(all_csv_files, 'data.csv')


def PlayerMatch(player1, player2):
    if(player1['Name'] == player2['Name'] and player1['Team'] == player2['Team'] and player1['Pos'] == player2['Pos']):
        return True
    elif(player1['Name'] == player2['Name'] and player1['Pos'] == player2['Pos'] and (player1['Team'] == "Dumb" or player2['Team'] == "Dumb")):
        return True
    elif(player1['Name'].split(" ")[0][0] + " " + player1['Name'].split(" ")[1] == player2['Name'] and player1['Team'] == player2['Team'] and player1['Pos'] == player2['Pos']):
        return True
    elif(player1['Name'] == player2['Name'].split(" ")[0][0] + " " + player2['Name'].split(" ")[1] and player1['Team'] == player2['Team'] and player1['Pos'] == player2['Pos']):
        player1['Name'] = player2['Name']
        return True
    
    if(len(player1['Name'].split(" ")) == 2 and len(player2['Name'].split(" ")) == 2):
        if(player1['Name'].split(" ")[0][0] + " " + player1['Name'].split(" ")[1] == player2['Name'] and player1['Team'] == player2['Team'] and player1['Pos'] == player2['Pos']):
            return True
        elif(player1['Name'] == player2['Name'].split(" ")[0][0] + " " + player2['Name'].split(" ")[1] and player1['Team'] == player2['Team'] and player1['Pos'] == player2['Pos']):
            player1['Name'] = player2['Name']
            return True
        
    if(len(player1['Name'].split(" ")) == 3 and len(player2['Name'].split(" ")) == 3):
        if(player1['Name'].split(" ")[0][0] + " " + player1['Name'].split(" ")[1]+ " " + player1['Name'].split(" ")[2] == player2['Name'] and player1['Team'] == player2['Team'] and player1['Pos'] == player2['Pos']):
            return True
        elif(player1['Name'] == player2['Name'].split(" ")[0][0] + " " + player2['Name'].split(" ")[1]+ " " + player2['Name'].split(" ")[2] and player1['Team'] == player2['Team'] and player1['Pos'] == player2['Pos']):
            player1['Name'] = player2['Name']
            return True
        
    return False

def AddRank(combinedData, newPlayer):
    for player in combinedData:
        match = PlayerMatch(player, newPlayer)
        if(match):
            player['Ranks'].append(newPlayer['Rank'])
            player['Costs'].append(newPlayer['Cost'])
            return #NEED THIS TO SKIP APPEND
    combinedData.append({'Ranks':[newPlayer['Rank']], 'Name':newPlayer['Name'], 'Pos':newPlayer['Pos'], 'Team':newPlayer['Team'], 'Costs':[newPlayer['Cost']]})

combinedData = []

for csv_name in all_csv_files:
    csv = pd.read_csv(csv_name)
    for index, row in csv.iterrows():
        # print(row['Rank'], row['Name'])
        AddRank(combinedData, row)



# print(combinedData) # HAS ALL PLAYERS WITH ALL RANKS AND COSTS HERE


def CalculateRank(ranks):
    count = 0
    sum = 0
    for rank in ranks:
        sum += rank
        count += 1
    return sum/count

def CalculateCost(costs):
    count = 0
    sum = 0
    for cost in costs:
        if(cost == -1):
            continue
        sum += cost
        count += 1
    if(count == 0):
        return 'N/A'    
    return sum/count


byeWeeks = { "ARI":14, "ATL":11, "BAL":13, "BUF":13, "CAR":7, "CHI":13, "CIN":7, "CLE":5, "DAL":7, "DEN":9, "DET":9, "FA":0, "GB":6, "HOU":7, "IND":11, "JAC":9, "KC":10, "LAC":5, "LAR":10, "LV":13, "MIA":10, "MIN":13, "NE":11, "NO":11, "NYG":13, "NYJ":7, "PHI":10, "PIT":6, "SEA":5, "SF":9, "TB":5, "TEN":7, "WAS":14 }

def bubble(text):
    for i in range(len(text),1,-1):
        for j in range(0,i-1):
            if float(text[j][text[j].find('<td class="has-details">')+24 : text[j][text[j].find('<td class="has-details">')+24:].find("<")+text[j].find('<td class="has-details">')+24  ]) > float(text[j+1][text[j+1].find('<td class="has-details">')+24 : text[j+1][text[j+1].find('<td class="has-details">')+24:].find("<")+text[j+1].find('<td class="has-details">')+24  ]):
                text[j],text[j+1]=text[j+1],text[j]
            else:
                pass

# Start building html
text = []
count = 1
for player in combinedData:
    # if(player['Team'] == "-1"):
    # print(player)
    text.append('<tr class="clickable-row tablerow"id="player'+ str(count) +'"data-href="http://tutorialsplane.com"><td class="has-details">' +str(CalculateRank(player['Ranks']))[:5]+ '<span class="details">'+str(player['Ranks'])+'</span></td><td>' +player['Name']+ '</td><td>' +player['Pos']+ '</td><td>' +player['Team']+'</td><td>'+str(byeWeeks[player['Team']])+'</td><td class="has-details">'+str(CalculateCost(player['Costs']))[:5]+'<span class="details">'+str(player['Costs'])+'</span></td></tr>\n')
    count += 1

bubble(text)

newText = ""
for line in text:
    # print(line)
    newText += line

# print(text)
file = open('html.txt', "w")
file.write(newText)