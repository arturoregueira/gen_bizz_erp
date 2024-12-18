from app import db

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