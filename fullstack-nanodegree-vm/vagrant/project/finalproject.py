from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Zoo, Animal

app = Flask(__name__)

engine = create_engine('sqlite:///zoomenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()




@app.route('/zoo/<int:zoo_id>/menu/JSON')
def zooMenuJSON(zoo_id):
    zoo = session.query(Zoo).filter_by(id=zoo_id).one()
    items = session.query(Animal).filter_by(
        zoo_id=zoo_id).all()
    return jsonify(Animals=[i.serialize for i in items])


@app.route('/zoo/<int:zoo_id>/menu/<int:animal_id>/JSON')
def animalJSON(zoo_id, animal_id):
    Menu_Item = session.query(Animal).filter_by(id=zoo_id).one()
    return jsonify(Menu_Item=Menu_Item.serialize)


@app.route('/zoo/JSON')
def zoosJSON():
    zoos = session.query(Zoo).all()
    return jsonify(zoos=[r.serialize for r in zoos])


# Show all zoos
@app.route('/')
@app.route('/zoo/')
def showzoos():
    zoos = session.query(Zoo).all()
    # return "This page will show all my zoos"
    return render_template('zoos.html', zoos=zoos)


# Create a new zoo
@app.route('/zoo/new/', methods=['GET', 'POST'])
def newZoo():
    if request.method == 'POST':
        newZoo = Zoo(name=request.form['name'])
        session.add(newZoo)
        session.commit()
        return redirect(url_for('showZoos'))
    else:
        return render_template('newZoo.html')
    # return "This page will be for making a new zoo"

# Edit a zoo


@app.route('/zoo/<int:zoo_id>/edit/', methods=['GET', 'POST'])
def editZoo(zoo_id):
    editedZoo = session.query(
        Zoo).filter_by(id=zoo_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedZoo.name = request.form['name']
            return redirect(url_for('showZoos'))
    else:
        return render_template(
            'editZoo.html', zoo=editedZoo)

    # return 'This page will be for editing zoo %s' % zoo_id

# Delete a zoo


@app.route('/zoo/<int:zoo_id>/delete/', methods=['GET', 'POST'])
def deleteZoo(zoo_id):
    zooToDelete = session.query(
        Zoo).filter_by(id=zoo_id).one()
    if request.method == 'POST':
        session.delete(zooToDelete)
        session.commit()
        return redirect(
            url_for('showZoos', zoo_id=zoo_id))
    else:
        return render_template(
            'deleteZoo.html', zoo=zooToDelete)
    # return 'This page will be for deleting zoo %s' % zoo_id


# Show a zoo menu
@app.route('/zoo/<int:zoo_id>/')
@app.route('/zoo/<int:zoo_id>/menu/')
def showAnimal(zoo_id):
    zoo = session.query(Zoo).filter_by(id=zoo_id).one()
    items = session.query(Animal).filter_by(
        zoo_id=zoo_id).all()
    return render_template('menu.html', items=items, zoo=zoo)
    # return 'This page is the menu for zoo %s' % zoo_id

# Create a new menu item


@app.route(
    '/zoo/<int:zoo_id>/menu/new/', methods=['GET', 'POST'])
def newAnimal(zoo_id):
    if request.method == 'POST':
        newItem = Animal(name=request.form['name'], species=request.form[
                           'species'], expense=request.form['expense'], diet=request.form['diet'], zoo_id=zoo_id)
        session.add(newItem)
        session.commit()

        return redirect(url_for('showAnimal', zoo_id=zoo_id))
    else:
        return render_template('newanimal.html', zoo_id=zoo_id)

    return render_template('newAnimal.html', zoo=zoo)
    # return 'This page is for making a new menu item for zoo %s'
    # %zoo_id

# Edit a menu item


@app.route('/zoo/<int:zoo_id>/menu/<int:animal_id>/edit',
           methods=['GET', 'POST'])
def editAnimal(zoo_id, animal_id):
    editedItem = session.query(Animal).filter_by(id=zoo_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['species']:
            editedItem.species = request.form['name']
        if request.form['expense']:
            editedItem.expense = request.form['expense']
        if request.form['diet']:
            editedItem.diet = request.form['diet']
        session.add(editedItem)
        session.commit()
        return redirect(url_for('showAnimal', zoo_id=zoo_id))
    else:

        return render_template(
            'editAnimal.html', zoo_id=zoo_id, animal_id=animal_id, item=editedItem)

    # return 'This page is for editing menu item %s' % zoo_id

# Delete a menu item


@app.route('/zoo/<int:zoo_id>/menu/<int:animal_id>/delete',
           methods=['GET', 'POST'])
def deleteAnimal(zoo_id, animal_id):
    itemToDelete = session.query(Animal).filter_by(id=zoo_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        return redirect(url_for('showAnimal', zoo_id=zoo_id))
    else:
        return render_template('deleteAnimal.html', item=itemToDelete)
    # return "This page is for deleting menu item %s" % zoo_id


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
