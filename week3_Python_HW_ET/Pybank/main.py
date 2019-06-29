# -*- coding: utf-8 -*-
import datetime

#filename = "budget_data.csv"
count = 0
Net_total_profit_loss = 0
average_change = 0
last_profit_loss = 0
Greatest_increase = 0
Greatest_increase_date = " "
Greatest_decrease = 0
Greatest_decrease_date = " "

with open("budget_data.csv", "r") as file_object:
    for line in file_object:
        count += 1
        if ( count == 1 ):
            continue
        else:
            (Date, Profit_loss) = line.split(",") # splitting input lines
            Profit_loss = int(Profit_loss)
            Net_total_profit_loss += Profit_loss
            average_change += (Profit_loss - last_profit_loss)
            last_profit_loss = Profit_loss #remember the last profit loss for next row comparison
            if ( Profit_loss >= Greatest_increase):
                Greatest_increase = Profit_loss
                Greatest_increase_date = Date
            if ( Profit_loss <= Greatest_decrease):
                Greatest_decrease = Profit_loss
                Greatest_decrease_date = Date
            #print(Date + " - " + str(Profit_loss) + "\n")

            #print(str(count - 1) + " - " + Date + " - " + str(Profit_loss) + " - " + str(Net_total_profit_loss)) #this is total months and total profit and loss
average_change = average_change / (count - 1)    

print("Financial Analysis")
print("- - - - - - - - - - -")
print("Total months: " + str(count - 1))
print("Total: $" + str(Net_total_profit_loss))
print("Average Change: $" + str(int(average_change)))
print("Greatest Increase in Profits: " + Greatest_increase_date + "($" + str(Greatest_increase) + ")") 
print("Greatest Decrease in Profits: " + Greatest_decrease_date + "($" + str(Greatest_decrease) + ")")    

outfile = open("budget_data.txt", "w+")
outfile.write("\n\nFinancial Analysis\n")
outfile.write("\n- - - - - - - - - - -\n")
outfile.write("\nTotal months: " + str(count - 1) + "\n")
outfile.write("\nTotal: $" + str(Net_total_profit_loss) + "\n")
outfile.write("\nAverage Change: $" + str(int(average_change)) + "\n")
outfile.write("\nGreatest Increase in Profits: " + Greatest_increase_date + "($" + str(Greatest_increase) + ")" + "\n") 
outfile.write("\nGreatest Decrease in Profits: " + Greatest_decrease_date + "($" + str(Greatest_decrease) + ")" + "\n")  
outfile.close()       
# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The average of the changes in "Profit/Losses" over the entire period

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period"""
