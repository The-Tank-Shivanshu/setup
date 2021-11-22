import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df,x="coffee in ml", y="sleep in hours")
        fig.show()

def getDataSource(data_path):
    coffee = []
    sleep = []
    with open(data_path) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))

    return {"x" : coffee, "y": sleep}
def findCoRelation(source):
    corelation=np.corrcoef(source["x"],source["y"])
    print (corelation)
dataSource=getDataSource("./data/cups of coffee vs hours of sleep.csv")
findCoRelation(dataSource)

