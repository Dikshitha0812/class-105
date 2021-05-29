import pandas as pd
import statistics
import plotly.express as px
import math

data = pd.read_csv("./class1.csv")
markslist = data["Marks"].tolist()
print(markslist)

#HOW TO STANDARD DEVIATION
# first step you find the mean of the desired column.i.e. markslist 
# second step you do subtraction of each marks value from mean  , i.e mean - marks 
# and you store in a list
#square each element of the subtracted list , i.e. (mean-marks)^2
# perform addition of each (mean-marks)^2
# divide the total sum by the total number of values, i.e. the length of markslist 
# perform the square root to get the standard deviation. 

mean = statistics.mean(markslist)
print(mean)
sub_list = []
for i in markslist:
    value = mean - int(i)
    sub_list.append(value)

print(sub_list)

square_list = []
for i in sub_list:
    value = i * i
    square_list.append(value)

print(square_list)

total = sum(square_list)
print(total)

final = total / len(markslist)
print(final)

std_deviation = math.sqrt(final)
print("the standard deviation for class 1 is ", std_deviation)
print("hence the data is scattered in the range ", mean-std_deviation, mean + std_deviation)