from flask import Flask, render_template, request, session, redirect, url_for, Response, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import hashlib


db = SQLAlchemy()




def create_app():
    app = Flask(__name__, template_folder="templates")
    app.secret_key =  hashlib.sha256("Viva Christo Rey".encode()).hexdigest()
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./maindb.db"

    db.init_app(app)


    from routes import register_routes
    register_routes(app,db)


    migrate = Migrate(app, db)

    return app