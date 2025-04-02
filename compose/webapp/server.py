from os import getenv

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text


app = Flask(__name__)

# Setup the connection to the database
db_user = getenv('DB_USER', 'root')
db_pass = getenv('DB_PASSWORD', 'root')
db_host = getenv('DB_HOST', 'localhost')
db_port = getenv('DB_PORT', '3306')
db_name = getenv('DB_NAME', 'movies')

db_uri = f'mysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'

db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


def get_movies():
    """
    Retrieves all movies from the database.
    """
    movies = []

    for row in db.session.execute(text("SELECT * FROM movies")):
        movies.append({"name": row[0], "rating": row[1]})

    return movies


def render_movie_li(movies):
    """
    Creates a HTML list (<li>) of all movies.
    """
    html = ""

    for movie in movies:
        html += f"""
            <a href="#" class="list-group-item list-group-item-action flex-column align-items-start">
                <div class="d-flex w-100 justify-content-between">
                    <h5 class="mb-1">{movie['name']}</h5>
                    <small class="rating"><i class="bi bi-star-fill"></i><span>{movie['rating']}</span></small>
                </div>
            </a>
        """
    return html


@app.route('/')
def index():
    """
    This method is called upon opening the webapp.
    """
    movies = get_movies()
    movies_li = render_movie_li(movies)

    # Read the index.html and add the movies_li to it.
    return open('index.html').read() % movies_li


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=getenv('PORT', 5000))
