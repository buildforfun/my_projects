import sqlite3
from flask import Flask, render_template

conn = sqlite3.connect('test_db.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM FavMovieData;")
tables = cursor.fetchall()

def create_app():
    # Flask app set up and connect to database
    app = Flask(__name__)

    # TODO connect database and pass in data

    @app.route('/')
    def index():
        return render_template('index.html')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=False)