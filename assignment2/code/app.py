import os
from datetime import date, timedelta

from flask import Flask, jsonify
from flask_jwt import JWT, jwt_required
from flask_restful import Api

from db import db
from security import authenticate, identity
from models.sales import SalesModel
from resources.customer import CustomerSignIn
from resources.product import ProductList
from resources.sales import PurchaseList, Sales


app=Flask(__name__)
app.secret_key= 'shreyan'
api=Api(app)

app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=2000)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

@app.before_first_request
def create_tables():
    db.create_all()


# api endpoint for customer signing in the site for the first time
api.add_resource(CustomerSignIn,'/sign_in')


# customer login and check for valid customer
app.config['JWT_AUTH_URL_RULE'] = '/log_in'
jwt=JWT(app, authenticate, identity)


# api for product purchase
api.add_resource(Sales,'/purchase')


# api endpoint for total sales
@app.route('/total_sales')
@jwt_required()
def total_sales():
    return jsonify({"message": f"Total number of sales for the day is   {len(SalesModel.find_by_date(date.today()).filter(SalesModel.sale_amount != 0).all())}."})


# api end point for unique visitors
@app.route('/uniquevisitors')
@jwt_required()
def unique_visitors():
    visitors = SalesModel.find_by_date(date.today()).all()
    unique_visitor = {}
    for object in visitors:
        if object.user_id in unique_visitor.keys():
            unique_visitor[object.user_id]+=1
        else:
            unique_visitor[object.user_id] = 1
    return jsonify({"message":f"Total no of unique visitors in a day {len(unique_visitor)}"})


# api endpoint for avg_sales_per_customer
@app.route('/avg_sales_per_customer')
@jwt_required()
def avg_sales_per_customer():
    visitors = SalesModel.find_by_date(date.today()).all()
    unique_visitor = {}
    total_sales=[]
    for object in visitors:
        total_sales.append(object.sale_amount)
        if object.user_id in unique_visitor.keys():
            unique_visitor[object.user_id]+=1
        else:
            unique_visitor[object.user_id] = 1
    var=sum(total_sales)/len(unique_visitor)
    return jsonify({"message": f"Average Sales Per Customer is {var}."})


# api endpoint for list_of_daily_display
api.add_resource(PurchaseList,'/daily_sales_list')

# api endpoint for listing of product
api.add_resource(ProductList,'/product_list')

if __name__=='__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)