import os
from datetime import date, timedelta

from flask import Flask, jsonify
from flask_jwt import JWT, jwt_required
from flask_restful import Api

from db import db
from models.sales import SalesModel
from resources.customer import CustomerRegister
from resources.product import ProductList
from resources.sales import (
    Average_sales_per_customer,
    PurchaseList,
    Sales,
    TotalSales,
    UniqueVisitors,
)
from security import authenticate, identity

app=Flask(__name__)
app.secret_key= '123'
api=Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=2000)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True


# api endpoint for customer signing in the site for the first time
api.add_resource(CustomerRegister,'/register')


# customer login and check for valid customer
app.config['JWT_AUTH_URL_RULE'] = '/log_in'
jwt=JWT(app, authenticate, identity)


# api for product purchase
api.add_resource(Sales,'/purchase')



# api endpoint for total sales
api.add_resource(TotalSales,'/total_sales')

# api endpoint for listing of product
api.add_resource(ProductList,'/product_list')


# api end point for unique visitors
api.add_resource(UniqueVisitors,'/uniquevisitors')



# api endpoint for avg_sales_per_customer
api.add_resource(Average_sales_per_customer,'/avg_sales_per_customer')


# api endpoint for list_of_daily_displays
api.add_resource(PurchaseList,'/daily_sales_list')


if __name__=='__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)