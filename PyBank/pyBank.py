import os
import csv

filePath = os.path.join('Resources', 'budget_data.csv')
outputPath = os.path.join('Analysis','budgetAnalysis.csv')

totalMonths = 0 
totalPL = 0 
maxProfit = 0 
profitChanges = []
profitsRecord = []
recordMonths = []


with open(filePath) as file:
    fileReader = csv.reader(file,delimiter=',')

    for row in fileReader:
        totalMonths = totalMonths + 1
        if row[1] != "Profit/Losses" and row[0] != "Date":
            totalPL = totalPL + int(row[1])
            profitsRecord.append(int(row[1]))
            recordMonths.append(row[0])

    for i in range(len(profitsRecord) -1):
        profitChanges.append(profitsRecord[i+1]-profitsRecord[i])
    
    averagePL = round(sum(profitChanges)/len(profitChanges),2)
    maxProfitChange = max(profitChanges)
    minProfitChange = min(profitChanges)

    maxValueIndex = profitChanges.index(maxProfitChange) + 1
    minValueIndex = profitChanges.index(minProfitChange) + 1

    maxMonthValue = recordMonths[maxValueIndex]
    minMonthValue = recordMonths[minValueIndex]

print("Financial Analysis")
print("---------------------------------------------------")
print(f"Total Months Recorded: {totalMonths-1}")
print("---------------------------------------------------")
print(f"Total Profits and Losses: ${totalPL}")
print(f"Average: ${averagePL}")
print(f"Greatest Increase in Profits: {maxMonthValue} (${maxProfitChange})")
print(f"Greatest Decrease in Profits: {minMonthValue} (${minProfitChange})")


with open (outputPath,'w',newline ='') as csvfile:
        
    toFile = csv.writer(csvfile, delimiter=',')

    toFile.writerow(['Financial Analysis'])
    toFile.writerow(['Total Months Recorded',totalMonths-1])
    toFile.writerow(['Total Profits and Losses',totalPL])
    toFile.writerow(['Average',averagePL])
    toFile.writerow(['Greatest Increase in Profits',maxMonthValue, '('+str(maxProfitChange)+')'])
    toFile.writerow(['Greatest Decrease in Profits',minMonthValue, '('+str(minProfitChange)+')'])
