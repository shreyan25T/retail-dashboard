
import json

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly
import plotly.express as px
from flask_jwt_extended import jwt_required
from flask_restful import Resource


class BarChartOne(Resource):
    df=pd.read_csv('Petrol Dataset.csv')
    @jwt_required()
    def get(self):
        res = self.df.groupby('Country')['Daily Oil Consumption (Barrels)'].mean().sort_values(ascending=False)
        res = res.head(10)
        return {"x":list(res.index),"y":list(res.values)}

class BarChartTwo(Resource):
    df=pd.read_csv('Petrol Dataset.csv')
    @jwt_required()
    def get(self):
        res = self.df.groupby('Country')['Price Per Liter (USD)'].mean().sort_values(ascending=False)
        res = res.head(10)
        return {"x":list(res.index),"y":list(res.values)}

class HistogramChart(Resource):
     df=pd.read_csv('Petrol Dataset.csv')
     @jwt_required()
     def get(self):
         cp =np.array(self.df.select_dtypes("number").drop(columns=["World Share1", "Price Per Liter (PKR)"]).corr())
         print(cp)
         m,n = cp.shape
         R,C = np.mgrid[:m,:n]
         cpr = np.round_(cp.ravel(), decimals = 1)
         out = np.column_stack((C.ravel(),R.ravel(), cpr.ravel()))
         data=out.tolist()
         return {"x":data}

class ScatterChart(Resource):
    df=pd.read_csv('Petrol Dataset.csv')
    @jwt_required()
    def get(self):
        sc =np.array(self.df[['Daily Oil Consumption (Barrels)','Price Per Liter (USD)']])
        data =sc.tolist()
        return {"x":data}


