# Library Imports
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

# Local imports
from create_database import create_database, insert_data, ElecProdBySource

db = SQLAlchemy()

def create_app():

    DATABASE_URL, engine = create_database()
    insert_data(engine)

    # Flask app set up and connect to database
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # initialise the database
    db = SQLAlchemy()
    db.init_app(app)
    
    @app.route('/')
    def index():
        data = db.session.query(ElecProdBySource).all()
        return render_template('index.html', data=data)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=False)