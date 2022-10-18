import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly
import plotly.express as px
from flask_jwt_extended import jwt_required
from flask_restful import Resource

cnx = sqlite3.connect("data.db")
df = pd.read_sql_query("SELECT * FROM petrol",cnx)

class BarChartOne(Resource):
    @jwt_required()
    def get(self):
        res = df.groupby('Country')['Daily Oil Consumption (Barrels)'].mean().sort_values(ascending=False)
        res = res.head(10)
        return {"x":list(res.index),"y":list(res.values)}

class BarChartTwo(Resource):

    @jwt_required()
    def get(self):
        res = df.groupby('Country')['Price Per Liter (USD)'].mean().sort_values(ascending=False)
        res = res.head(10)
        return {"x":list(res.index),"y":list(res.values)}

class HistogramChart(Resource):

     @jwt_required()
     def get(self):
         cp =np.array(df.select_dtypes("number").drop(columns=["World Share1", "Price Per Liter (PKR)"]).corr())
         print(cp)
         m,n = cp.shape
         R,C = np.mgrid[:m,:n]
         cpr = np.round_(cp.ravel(), decimals = 1)
         out = np.column_stack((C.ravel(),R.ravel(), cpr.ravel()))
         data=out.tolist()
         return {"x":data}

class ScatterChart(Resource):

    @jwt_required()
    def get(self):
        sc =np.array(df[['Daily Oil Consumption (Barrels)','Price Per Liter (USD)']])
        data =sc.tolist()
        return {"x":data}


