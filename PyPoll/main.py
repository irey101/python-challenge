#Import neccessary libraries before defining the path of csv.
import os
import csv
poll_csv = os.path.join("/users/coding/desktop/python-challenge/pypoll/resources", "election_data.csv")
#Creating placehodlers and counters. Total votes is equal to zero because we want it to accumulate the
#count adding 1 count per row.
totalvotes = 0
#The 3 variables below are defined as lists because indexing will be the easiest with referencing
#throughout the code.
prospect = []
VPP = []
VP = []
#Opening then redefining "poll_csv" as a csvfile:
with open(poll_csv, newline = "") as csvfile:
    #Once opened, we will then redefine it in read mode to create a new column after every comma
    csvreader = csv.reader(csvfile, delimiter = ",")
    #Reading the header.
    header = next(csvreader)
    #Now we are going to loop through each row in the csv file.
    for row in csvreader:
        #For each row, we will tally the votes to 1 which will then give us the final total of votes
        #individuals made. Assuming one vote per individual
        totalvotes += 1
        #We will then loop through each column in the row. If the row value is not within the list of
        #prospects then we will record the value of the 3rd column.
        if row[2] not in prospect:
            prospect.append(row[2])
            #We then create an index to reference what was just recorded (Which is the name).
            index = prospect.index(row[2])
            #We add one value to the list of VPP (Votes per prospect)
            VPP.append(1)
        else:
            #If the statement is true, if the column value matches the prospect name in the list
            #then we want to record the value and instead of adding one to the VPP list, we will add the 
            #vote in the index. We are creating an index that references the name and the amount of votes
            #per prospect has.
            index=prospect.index(row[2])
            VPP[index] += 1
    #We are now determing the percentage of the votes per prospect.
    #For each vote in the VPP list
    for votes in VPP:
        #We want to get the percentage by diving the votes (# of counted votes in the VPP list) by the total 
        #votes whihc is the length of the column. (Which has been adding up per loop since "totalvotes += 1")
        calc = (votes/totalvotes) * 100
        #We then need to round the result to 2 digits.
        calc = round(calc, 2)
        #Lastly, we then add the calculated percentage in the VP (Vote Percentage) list.
        VP.append(calc)
    #Now we will determine which prospect won by the largest amount of votes. To determine who won, we
    #can use the max syntax. We want to know the largest amount of votes in the VPP list
    #Once we get to this point in the code, the loop will be done therefore we want to then analyze the data 
    #as a whole.
    winner = max(VPP)
    #Once the get the largest number of votes per prospect, we then want to record that within the index.
    index = VPP.index(winner)
    #We can then reference the winning candidate by using the index.
    winningcand = prospect[index]

#Now we print the results and outputs using f-strings for format.
print("Election Results")
print("-------------------------------")
print(f"Total Votes: {str(totalvotes)}")
print("-------------------------------")
#Using i to match prospects within the list.
for i in range(len(prospect)):
    print(f"{prospect[i]}: {str(VP[i])}% ({str(VPP[i])})")
print("--------------------------------")
print(f"Winner: {winningcand}")
print("--------------------------------")
#Printing out the output using f-strings.
analysis = open("/users/coding/desktop/python-challenge/pypoll/analysis/Analysis.txt", "w")
line1 = "Election Results:"
line2 = "---------------------------------"
line3 = str(f"Total VotesL: {str(totalvotes)}")
line4 = "---------------------------------"
analysis.write('{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4))
for i in range(len(prospect)):
    line = str(f"{prospect[i]}: {str(VP[i])} ({str(VPP[i])})")
    analysis.write('{}\n'.format(line))
line5 = "----------------------------------"
line6 = str(f"Winner: {winningcand}")
line7 = "----------------------------------"
analysis.write('{}\n{}\n{}\n'.format(line5,line6,line7))