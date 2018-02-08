#concatenate two files into one file
import pandas as pd

a = pd.read_csv("election_data_1.csv")
b = pd.read_csv("election_data_2.csv")
b = b.dropna(axis=1)
merged = a.merge(b, on='title')
merged.to_csv("concatenated_election.csv", index=False)

import cs
import os
newfile = 'concatenated_election.csv'
#count number of votes
with open (newfile, 'r') as csvfile:
        row_count = int(sum(1 for row in newfile))
        print ("Election Results"
        "----------------------------------------------")
        print ("Total Votes: " + (row_count))
        print("----------------------------------------------") 

    
#I don't know how to count votes for each candidates. i thought of a for loop
count = 0
for CandidateVotes in newfile:
    if (row[3]) == "Rogers"                                   
        Rogers_count += count
        Rogers_percent = (int(Rogers_count)/row_count)*100
    if (row[3]) == "Gomez"
        Gomez_count += count
        Gomez_percent = (int(Gomez_count)/row_count)*100
    if (row[3]) == "Brentwood"
        Brentwood_count += count
        Brentwood_percent = (int(Brentwood_count)/row_count)*100 
    if (row[3]) == "Higgins"
        Higgins_count += count
        Higgins_percent = (int(Higgins_count)/row_count)*100
# I dont know how to get the winner, i think i should use the str(max()) function to find the most votes, but i dont know what to put in the bracket ()
# winner = str(max())
print ("Rogers: "+  Rogers_percent + "(" + (Rogers_count) + ")"
        "Gomez: "+  Gomez_percent + "(" + (Gomez_count) + ")"
        "Brentwood: "+  Brentwood_percent + "(" + (Brentwood_count) + ")"
        "Higgins: "+  Higgins_percent + "(" + (Higgins_count) + ")")
print("----------------------------------------------")
print ("Winner: " + str(winner)
print("----------------------------------------------")

