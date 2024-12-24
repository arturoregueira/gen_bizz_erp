from app import db
from flask_login import UserMixin

# This files contains the classes that our ORM will use to create and manipulate into tables

class Inventory(db.Model):
    __tablename__ = "Inventory"
    SSR_id = db.Column(db.Integer,primary_key=True,autoincrement=True, nullable = False)
    fab_Inventory_id = db.Column(db.Text,nullable = False)
    fabricant = db.Column(db.Text,nullable = False)
    fab_Inventory_name = db.Column(db.Text,nullable = False)
    qunt = db.Column(db.Integer,nullable = False)
    desc = db.Column(db.Text,nullable = False)
    #prefix = if self.qunt > 1 "s" else ""

    def __repr__(self):
        return f" We have {self.qunt} {self.fab_Inventory_name}s"
    
class Invoice(db.Model):
    __tablename__ = "Invoice"
    Invoice_id = db.Column(db.Integer,primary_key=True,autoincrement=True, nullable = False)
    #here we will add
    
class User(db.Model,UserMixin):
    __tablename__ = "User"

    userId = db.Column(db.Integer,primary_key=True,autoincrement=True, nullable = False)
    userName = db.Column(db.Text,nullable = False)
    password = db.Column(db.Text,nullable = False)
    role = db.Column(db.Text,nullable = True)
    desc = db.Column(db.Text,nullable = True)

    def __repr__(self):
        return f" User {self.userId} is named {self.userName}"
    
    def get_id(self):
        return self.userId