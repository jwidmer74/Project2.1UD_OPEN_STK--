from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup2 import Category, Base, Item
app = Flask(__name__)

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

#todo This example gives the all the items of the first category. I need to get all the Categories.
@app.route('/')
@app.route('/catalog')

def showCategories():
    categories = session.query(Category).all()
    # return "This page will show all my restaurants"
    return render_template('categories.html', categories=categories)
if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)    