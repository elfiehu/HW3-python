# Dependencies
import csv
import moment
from datetime import datetime
import random

# Create output file name
file_output_name = "budget_data2.csv"

# Months of Financial Data (Change as needed)
num_months = 85
current_date = moment.date("01-01-2016", "M-D-YYYY")
starting_date = current_date.add(months=-num_months)

# % of months that are positive vs negative (Change as needed)
gain_loss_weights = [0.85, 0.15]

# Range of profits or losses (Chane as needed)
range_revenue = [50000, 1200000]

# Iteratively build every month between start and current date
tracked_months = []
current_month = starting_date
revenues = []

for x in range(0, num_months + 1):

    # Generate a list of formatted months
    current_month = current_month.add(month=1)
    current_month_string = current_month.date.strftime("%b-%Y")
    tracked_months.append(current_month_string)

    # Generate a random revenue for each month
    random_revenue = random.randrange(range_revenue[0], range_revenue[1])
    revenues = revenues + [random_revenue]

# Convert a set amount of revenues to be negative
neg_months = int(num_months * gain_loss_weights[1])

for x in range(neg_months):
    revenues[x] = -1 * revenues[x]

# Shuffle the revenues so the negatives appear sporadically
random.shuffle(revenues)

# Assemble the months and revenues into a single list
fin_data = zip(tracked_months, revenues)

# Print the financial data to terminal
print(fin_data)

# Export a csv of the generated financial data
with open(file_output_name, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Date", "Revenue"])
    writer.writerows(fin_data)

#concatenate two budget files into one file
import pandas as pd

a = pd.read_csv("budget_data_1.csv")
b = pd.read_csv("budget_data_2.csv")
b = b.dropna(axis=1)
merged = a.merge(b, on='title')
merged.to_csv("concatenated_budget.csv", index=False)



import csv
import os
newfile = 'concatenated_budget.csv'

#count number of months
with open(newfile, 'rb') as csvfile:
    row_count = len(newfile)
    print ("Financial Analysis"
    "----------------------------------------------")
    print ("Total Months: " + (row_count))
#sum total revenue    
with open(newfile) as fin:
    headerline = fin.next()
    total_revenue = 0
    for row in csv.reader(fin):
        total_revenue += int(row[1])
   print ("Total Revenue: "+ "$" + (total_revenue))      
#average monthly change
with open (newfile, 'rb') as csvfile:
    for average_monthly_change in row[1]:
        monthly_change = int((row[1]) - ((row[1]-1)))
        total_monthly_change += int(monthly_change)
        average_monthly_change = int ((total_monthly_change) / ((row_count)-1))
        print ("Average Revenue Change: " + "$" (average_monthly_change))"                                    
#Greatest increase in revenue           
        monthly_change = int((row[1]) - ((row[1]-1)))
        greatest_increase = max(monthly_change)
        print("Greatest Increase In Revenue: " + (row(0)) + "($" +(greatest_increase) + ")")

#Greatest decrease in revenue
        monthly_change = int((row[1]) - ((row[1]-1)))
        greatest_decrease = min(monthly_change)
        print("Greatest Decrease In Revenue: " + (row(0)) + "($" +(greatest_decrease) + ")")





