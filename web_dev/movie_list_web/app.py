import sqlite3
from flask import Flask, render_template



def create_app():
    # Flask app set up and connect to database
    app = Flask(__name__)

    conn = sqlite3.connect('test_db.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM FavMovieData;")

    # Column names
    column_names = [description[0] for description in cursor.description]

    # Row data
    rows_data = cursor.fetchall()

    # Combine column and row data together to make a list of dicts
    data = [dict(zip(column_names, row)) for row in rows_data]

    @app.route('/')
    def index():
        return render_template('index.html', data=data)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=False)