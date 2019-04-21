from flask import Flask
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup2 import Category, Base, Item


engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
#todo This example gives the all the items of the first category. I need to get all the Categories.
@app.route('/')
@app.route('/hello')
def HelloWorld():
    #below gets you the list of all Categories
    category = session.query(Category)
    #category = session.query(Category).first()
    #items = session.query(Item).filter_by(category_id=category.id)
    output = ''
    for c in category:
        output += c.name
        output += '</br>'
    return output

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)    