from numpy import mafromtxt
import pandas as pd
import statistics
import plotly.express as px
import math

data = pd.read_csv("./class2.csv")
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
mean=statistics.mean(markslist)
print(mean)

sub_list=[]
for i in markslist:
    value= mean-int(i)
    sub_list.append(value)


square_list=[]
for i in sub_list:
    value=i*i
    square_list.append(value)

total=sum(square_list)

final=total/len(markslist)
print(final)

std_deviation=math.sqrt(final)
print("the standard deviation of class 2 :",std_deviation)
print("the data is scattered in the range", mean-std_deviation,mean+std_deviation)