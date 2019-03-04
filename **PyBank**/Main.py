# PyBank 

""" ![Revenue](Images/revenue-per-lead.jpg)

* In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). 
The dataset is composed of two columns: `Date` and `Profit/Losses`. 
(Thankfully, your company has rather lax standards for accounting so the records are simple.)

* Your task is to create a Python script that analyzes the records to calculate each of the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * The average of the changes in "Profit/Losses" over the entire period

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

* As an example, your analysis should look similar to the one below:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```

* In addition, your final script should both print the analysis to the terminal and export a text file with the results. """
#Project starts here
# Modules


#creates file paths along operating systems
import os
#module for reading csv files
import csv


# # Set path for file
budget_data = os.path.join('//Users//danieltaylor//Desktop//python-challenge//**PyBank**//budget_data.csv')
output_path = ('//Users//danieltaylor//Desktop//python-challenge//**PyBank**//output_1.txt')

#read file
# Open the CSV
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    months=0
    revenue=0
    rows=[r for r in csvreader]
    change_revenue=int(rows[1][1])
    max = rows[1]
    min = rows[1]
    for i in range(1, len(rows)):

        months=months+1
        row=rows[i]
        revenue=int(row[1]) + revenue
        if i > 1:
            change_revenue=change_revenue + int(row[1])+-int(rows[i-1][1])
        if int(max[1]) < int(row[1]):
            max=row
        if int(min[1]) > int(row[1]):
            min=row
average = int(revenue/months)
average_revenue_change=int(change_revenue/months)

#Printing the Outputs
with open(output_path, "w", newline='') as textfile:
    print("Financial Analysis", file=textfile)
    print("------------------", file=textfile)
    print("Total Months: " + str(months), file=textfile)
    print("Total Revenue: " +"$" +str(revenue), file=textfile)       
    print("Monthly Average Change: " +"$"+ str(average_revenue_change), file=textfile)
    print("Greatest Increase in Revenue:" + str(max[0])+" ($" + str(max[1])+")", file=textfile)
    print("Greatest Decrease in Revenue:" + str(min[0])+" ($" + str(min[1])+")", file=textfile)

with open(output_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        print(row)