from pathlib import Path

from flask import render_template, redirect, url_for

from . import app, db
from .models import Movie, Review

BASEDIR = Path(__file__).parent
UPLOAD_FOLDER = BASEDIR / 'static' / 'images'

@app.route('/')
def index():
    movies = Movie.query.order_by(Movie.id.desc()).all()
    return render_template('index.html',
                           movies=movies)

@app.route('/movie/<int:id>', methods=['GET', 'POST'])
def movie(id):
    movie = Movie.query.get(id)
    if movie.reviews:
        avg_score = round(sum(review.score for review in movie.reviews) / len(movie.reviews), 2)
    else:
        avg_score = 0

    return render_template('movie.html',
                           movie=movie,
                           avg_score=avg_score)

@app.route('/')
def m():
    pass