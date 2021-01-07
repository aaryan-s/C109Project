import statistics
import csv
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
math = []
with open("C109.csv", newline='') as csvfile:
    row = csv.DictReader(csvfile) #row 1
    for i in row:
        math.append(float(i["math score"]))
#print(brand)
#print(rating)

std = statistics.stdev(math)
mean = statistics.mean(math)
print("Test prep mean:",mean)
median = statistics.median(math)
print("Test prep median:",median)
print("Standard Deviation for test prep:",std)

# 68 - 95 - 99.7
math1start = mean - std
math1end = mean + std
math2start = math1start - std
math2end = math1end + std
math3start = math2start - std
math3end = math2end + std



math1stddev = [ i for i in math if i < math1end and i > math1start]
print("rating % of first standard deviation: ",len(math1stddev)*100/len(math))
math2stddev = [ i for i in math if i < math2end and i > math2start]
print("rating % of second standard deviation: ",len(math2stddev)*100/len(math))
math3stddev = [ i for i in math if i < math3end and i > math3start]
print("rating % of third standard deviation: ",len(math3stddev)*100/len(math))

fig = ff.create_distplot([math],["Result"])
fig.add_trace(go.Scatter(x=[mean,mean], y=[0,1],mode="lines",name = "Mean"))
fig.show()