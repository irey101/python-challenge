#Importing the neccessary libraries before defining the paths
import os
import csv
budget_csv = os.path.join("/Users/Coding/desktop/python-challenge/pybank/Resources", "budget_data.csv")
#We then want to determine what the question is asking and how we are going to get there.
#Month count, Profit/Loss count, Profit/Loss Change and the constant are all equal to zero because
#those will be our counters.
monthcount = 0
profitlosscount = 0
profitlosschange = 0
constant = 0
#Thos that are equal to brackets, we want as lists because it will be easier to reference the list/index 
#when determining the dates and profit.
date = []
profit = []
#We will open and redefine the data file to a csvfile
with open(budget_csv, newline = "") as csvfile:
    #Next, we then want to open the csvfile in read mode having to create a new column after each comma
    #For this block of code, we are stating our rules before going to the loops. 
    csvreader = csv.reader(csvfile, delimiter = ",")
    #We will read the header.
    header = next(csvfile)
    #For the string of code below, we need to determine our first variable in order to calculate the 
    #change that is happening throughout the data set
    firstrowvariables = next(csvreader)
    #*Before Loop* We will start off by having +1 with our month count. This is to account for the first row variables
    monthcount += 1
    #*Before Loop* We also want to start off with our profit/loss count as the first variable in column 2.
    profitlosscount += int(firstrowvariables[1])
    #*Before Loop* We will consider the constant as the first variable within column 2.
    constant = int(firstrowvariables[1])
    #Now we will begin our loop through the dataset. For each row within the csv
    for row in csvreader:
        #For each row within the csv, we want to record the date per row in column 1
        date.append(row[0])
        #For each row within the csv, we will calculate the profit/loss change by subtracting the 
        #first row variable to first row variable. (This of course will be zero)
        profitlosschange = int(row[1])-constant
        #After the calculation we will want to record the change in profit/loss within the profit
        #list.
        profit.append(profitlosschange)
        #Once the loop for the row is complete we want the constant to change to the next row
        #considering the constant started the first number within the column, once a loop finishes
        #the value will move on to the next number withihn the column which is row 2 then 3 then 4
        #and so on (i.e (1-1), (2-3) (3-4) etc ..)
        constant = int(row[1])
        #One count will be added per row loop
        monthcount += 1
        #*After loop* Once fininshed with all the rows within the csv. We want the profitloss counter to be
        #the recorded amount plus the column as a whole. 
        profitlosscount = profitlosscount + int(row[1])
        #Now to determine the max increase of the whole dataset.
        #This easily doable by using the max syntax from the profit list (which has been recording the change
        # per loop)
        maxincrease = max(profit)
        #Once we have the max profit from the list, we then want to record the max profit within the profit index.
        maxincreaseindex = profit.index(maxincrease)
        #By recording the max increase to the profit index, we can then reference the increase with the date list.
        maxincreasedates = date[maxincreaseindex]
        #The same process as the max increase applies to this
        maxdecrease = min(profit)
        maxdecreaseindex = profit.index(maxdecrease)
        maxdecreasedates = date[maxdecreaseindex]
        #To calculate the the average we want the sum of all the number within the profit list and divide it by the
        #amount of times (rows) it recorded.
        averageprofitloss = sum(profit)/len(profit)
#Lastly, we want to print out the results using f-strings.
print(f'Financial Analysis')
print(f'---------------------------')
print(f'Total Months within dataset: {str(monthcount)}')
print(f'Total profit throughout the dataset: ${str(profitlosscount)}')
print(f'Average profit change throughout the dataset: ${str(profitlosschange)}')
print(f'Greatest increase in profit within the dataset: {maxdecreasedates} ${str(maxincrease)}')
print(f'Greatest decrease in profits within the dataset: {maxdecreasedates} ${str(maxdecrease)}')
#Printing analysis using f-strings.
analysis = open("/users/coding/desktop/python-challenge/pybank/analysis/Analysis.txt", "w")
line1 = "Financial Analysis"
line2 = "---------------------------------------------------------"
line3 = str(f'Total Months within dataset: {str(monthcount)}')
line4 = str(f'Total profit throughout the dataset: ${str(profitlosscount)}')
line5 = str(f'Average profit change throughout the dataset: ${str(profitlosschange)}')
line6 = str(f'Greatest increase in profit within the dataset: {maxdecreasedates} ${str(maxincrease)}')
line7 = str(f'Greatest decrease in profits within the dataset: {maxdecreasedates} ${str(maxdecrease)}')
analysis.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))