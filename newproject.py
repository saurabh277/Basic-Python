import pandas as pd

#1 - total sports events we have
dataframe = pd.read_excel('Olympic.xlsx')
print(dataframe)
res = set()
for index,row in dataframe.iterrows():
    res.add(row[5])
print(res)

#2 - total players we have
pla = set()
for index,row in dataframe.iterrows():
    pla.add(row[0])
print(len(pla))

#3 - how many times each games is mentioned
#dictionary out of set
games = dict.fromkeys(res,0)
for index,row in dataframe.iterrows():
    games[row[5]] += 1

print(games)

#list all the games which are played less than by 30 players
