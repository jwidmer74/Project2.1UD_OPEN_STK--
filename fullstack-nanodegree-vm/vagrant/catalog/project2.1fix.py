from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup2 import Base, Category, Item

app = Flask(__name__)

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/catalog')

def showCategories():
    categories = session.query(Category).all()
    # return "This page will show all my restaurants"
    return render_template('categories.html', categories=categories)


@app.route('/catalog/<int:category_id>/')
def categoryMenu(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(Item).filter_by(category_id=category_id)
    output = ''
    for i in items:
        output += i.name
        output += '</br>'
        output += i.title
        output += '</br>'
        output += i.description
        output += '</br>'
        output += '</br>'

    return output


@app.route('/catalog/<int:category_id>/new', methods=['GET', 'POST'])
def newItem(category_id):

    if request.method == 'POST':
        newItem = Item(name=request.form['name'], description=request.form[
                           'description'], title=request.form['title'], course=request.form['course'], category_id=category_id)
        session.add(newItem)
        session.commit()
        return redirect(url_for('categoryMenu', category_id=category_id))
    else:
        return render_template('newitem.html', category_id=category_id)


@app.route('/catalog/<int:category_id>/<int:menu_id>/edit',
           methods=['GET', 'POST'])
def editItem(category_id, menu_id):
    editedItem = session.query(Item).filter_by(id=menu_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        session.add(editedItem)
        session.commit()
        return redirect(url_for('categoryMenu', category_id=category_id))
    else:
        # USE THE RENDER_TEMPLATE FUNCTION BELOW TO SEE THE VARIABLES YOU
        # SHOULD USE IN YOUR EDITitem TEMPLATE
        return render_template(
            'edititem.html', category_id=category_id, menu_id=menu_id, item=editedItem)


@app.route('/category/<int:category_id>/<int:menu_id>/delete/')
def deleteItem(category_id, menu_id):
    return "page to delete a new menu item."

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
