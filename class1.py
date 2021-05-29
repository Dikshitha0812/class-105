import pandas as pd
import statistics
import plotly.express as px

data = pd.read_csv("./class1.csv")
markslist = data["Marks"].tolist()
print(markslist)

mean = statistics.mean(markslist)
median = statistics.median(markslist)
mode = statistics.mode(markslist)

print("Class 1" , mean, median, mode)

fig = px.scatter(data, x="Student Number", y = "Marks")
fig.update_layout(shapes = [dict(type = 'line', x0 = 0, x1= len(markslist), y0 = mean, y1 = mean)])
fig.show()

#class 1 : 75, 80.0, 90


