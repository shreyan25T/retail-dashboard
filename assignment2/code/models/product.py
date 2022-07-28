from db import db
from flask_restful import Resource


class ProductModel(db.Model):
    __tablename__ ='products'
    id=db.Column(db.Integer, primary_key=True)
    product_id=db.Column(db.Integer)
    prod_description=db.Column(db.String(80))

    def __init__(self,product_id, prod_description):

        self.product_id=product_id
        self.prod_description=prod_description


    def json(self):
        return {"prod_id":self.product_id,"prod_description":self.prod_description}


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()



