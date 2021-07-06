import os
import csv

filePath = os.path.join('Resources', 'election_data.csv')
outputPath = os.path.join("Analysis","electionResults.csv")

candidates = []
numVotes = []
percentage = []
greatest = 0
totalVotes = 0

with open(filePath) as file:

    fileReader = csv.reader(file, delimiter=',')

    

    for row in fileReader:
        totalVotes = totalVotes + 1
        #Resource: https://www.geeksforgeeks.org/python-get-unique-values-list/
        if row[2] not in candidates and row[2] != "Candidate":
            candidates.append(row[2])
            numVotes.append(1)
        
        if row[2] in candidates:
            numVotes[candidates.index(row[2])] = numVotes[candidates.index(row[2])] +1

    print("Election Results")
    print("---------------------------------------------------")
    print(f"Total Votes: {totalVotes}")
    print("---------------------------------------------------")
    for x in candidates:
        # Resource: https://www.geeksforgeeks.org/python-list-index/
        accessor = candidates.index(x)
        percentVotes = round((numVotes[accessor]/totalVotes)*100,2)
        percentage.append(percentVotes)
        print(f"{x}: {percentVotes}% ({numVotes[accessor]})")

    
    for y in numVotes:
        

        if y > greatest:
            greatest = y
            indexer = numVotes.index(y)
            winner = candidates[indexer]
    print("---------------------------------------------------")
    print(f"Winner: {winner}")
            

    with open (outputPath,'w',newline ='') as csvfile:
        
        toFile = csv.writer(csvfile, delimiter=',')

        toFile.writerow(['Election Results'])
        
        for c in candidates:
            accessor2 = candidates.index(c)
            toFile.writerow([c,percentage[accessor2], numVotes[accessor2]])

        toFile.writerow(['Winnner', winner])



