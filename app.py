from flask import Flask, render_template, request, session, redirect, url_for, Response, send_from_directory
import pandas as pd
import os
import uuid
import hashlib
listOspreads = [".xlsx ", ".xls", ".csv", ".ods", 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', "application/vnd.ms-excel", "application/vnd.oasis.opendocument.spreadsheet",]
listOspreads_notCsv = [".xlsx ", ".xls", ".ods", 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', "application/vnd.ms-excel", "application/vnd.oasis.opendocument.spreadsheet",]
app = Flask(__name__, template_folder="templates")
app.secret_key =  hashlib.sha256("Viva Christo Rey".encode()).hexdigest()

@app.route("/")
def index():

    mylist = {10,20,30,40,70,120}
    return render_template("index.jinja",mylist=mylist )
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
@app.route("/inventory")
def inventory():
    pass


if __name__ == "__main__":

    app.run(
        host='0.0.0.0',  # Allows the app to be accessible externally, not just localhost
        port=5000,       # Specifies the port number to run the server (default is 5000)
        debug=True,      # Enables debug mode for automatic reloads and better error messages
        #threaded=True,   # Enables handling multiple requests concurrently
        #use_reloader=True,  # Ensures the app reloads upon code changes
    )

#nothing should be here!!!