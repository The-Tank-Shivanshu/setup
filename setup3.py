import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df,x="Size of TV", y="Average time spent watching TV in a week (hours)")
        fig.show()

def getDataSource(data_path):
    TV = []
    TIME = []
    with open(data_path) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            TV.append(float(row["Size of TV"]))
            TIME.append(float(row["TV in a week (hours)"]))

    return {"x" : TV, "y": TIME}
def findCoRelation(source):
    corelation=np.corrcoef(source["x"],source["y"])
    print (corelation)
dataSource=getDataSource("./data/Size of TV.csv")
findCoRelation(dataSource)

