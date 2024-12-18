from flask import render_template, request, session, redirect, url_for, Response, send_from_directory
import pandas as pd
import os
import uuid
from models import Inventory
from sqlalchemy import func
def register_routes(app,db):
    listOspreads = [".xlsx ", ".xls", ".csv", ".ods", 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', "application/vnd.ms-excel", "application/vnd.oasis.opendocument.spreadsheet",]
    listOspreads_notCsv = [".xlsx ", ".xls", ".ods", 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', "application/vnd.ms-excel", "application/vnd.oasis.opendocument.spreadsheet",]
    
    @app.route("/")
    def index():

        #mylist = [10,20,30,40,70,120]
        return render_template("index.jinja")
    @app.route("/login", methods=["GET","POST"])
    def login():

        if request.method == "GET":
            render_template("login.jinja")
        elif request.method == "POST":
            usernameGiven = request.form.get['username']
            passwordGiven = request.form.get['password']
            if usernameGiven and passwordGiven:
                render_template("index.jinja")
            else:
                return "lopgin falied"


    @app.route("/files", methods = ["GET", "POST"])
    def files():     
        return render_template('fileSubBoiler.jinja', table=session.get('table', ""))

    @app.route("/file_upload", methods = ["POST","GET"])
    def file_upload():                 
        file = request.files['file']

        if file.content_type == "text/plain":
            return file.read().decode()
        elif file.content_type in listOspreads:
            if file.content_type == ".ods":
                df =  pd.read_excel(file, engine='odf')
                table =  df.to_html()
            elif file.content_type == ".csv":
                df =  pd.read_csv
                table =  df.to_html()
            else:
                df =   pd.read_excel(file)
                table =   df.to_html()
        table_html = df.to_html()
        session['table'] = table_html
        return redirect(url_for("files"))

    @app.route("/file_clear", methods = ["POST"])
    def file_clear():
        session['table'] = ""
        return redirect(url_for("files"))

    @app.route("/downloads",methods = ["POST","GET"])
    def downloads():
        return render_template('downloadsBoiler.jinja', fileOutput=session.get('fileOutput', ""))


    @app.route("/download_instance<fileOutput>",methods = ["GET"])
    def download_instance(fileOutput):
        return send_from_directory("downloads", fileOutput, download_name = "output.csv")


    @app.route("/to_csv", methods =["POST"])
    def to_csv():
        file = request.files['file']

        if file.content_type in listOspreads:
            if file.content_type == ".ods":
                df =  pd.read_excel(file, engine='odf')
            else:
                df =  pd.read_excel(file)
        if not os.path.exists('downloads'):
            os.makedirs('downloads')
        filename = f'{uuid.uuid4()}.csv'
        fileOutput = os.path.join('downloads', filename)
        df.to_csv(os.path.join('downloads', filename))
        session['fileOutput'] = filename
        return redirect(url_for("downloads"))



    @app.route("/invoices")
    def invoices():                 #fill in here when you construct your invoices and inventory
        pass
    @app.route("/inventory", methods=["GET", "POST"])
    def inventory():
        if request.method == "GET":
            inventory = (
            db.session.query(
            Inventory.fab_Inventory_id,
            Inventory.fabricant,
            Inventory.SSR_id,
            Inventory.fab_Inventory_name,
            func.sum(Inventory.qunt).label('qunt')
            ).group_by(Inventory.fab_Inventory_id).all())
            return render_template("inventoryHomepage.jinja", inventory = inventory)
        elif request.method == "POST":
            fab_Inventory_id = request.form.get("fab_Inventory_id")
            fabricant = request.form.get("fabricant")
            fab_Inventory_name = request.form.get("fab_Inventory_name")
            qunt = int(request.form.get("qunt"))
            desc = request.form.get("desc")

            inventory = Inventory(fab_Inventory_id = fab_Inventory_id, fabricant = fabricant,
                                  fab_Inventory_name = fab_Inventory_name, qunt = qunt, desc = desc,)
            
            db.session.add(inventory)
            db.session.commit()

            inventory = (
            db.session.query(
            Inventory.fab_Inventory_id,
            Inventory.fabricant,
            Inventory.SSR_id,
            Inventory.fab_Inventory_name,
            func.sum(Inventory.qunt).label('qunt')
            ).group_by(Inventory.fab_Inventory_id).all())
            return render_template("inventoryHomepage.jinja", inventory = inventory)
    @app.route("/delete/<SSR_id>",methods=["DELETE"] )
    def delete(SSR_id):
        Inventory.query.filter(Inventory.SSR_id == SSR_id).delete()

        db.session.commit()

        inventory = (
            db.session.query(
            Inventory.fab_Inventory_id,
            Inventory.fabricant,
            Inventory.SSR_id,
            Inventory.fab_Inventory_name,
            func.sum(Inventory.qunt).label('qunt')
            ).group_by(Inventory.fab_Inventory_id).all())
        return render_template("inventoryHomepage.jinja", inventory = inventory)



        




