import os
from werkzeug import secure_filename
from flask import render_template, url_for, redirect
from app import app, db
from forms import NewItemForm
from models import Item

@app.route('/')
@app.route('/index')
def index():
    items = Item.query.all()
    items = [dict(key=item.key, image=url_for('static', filename=item.image))
             for item in items]

    return render_template("index.html",
        title='Flasks',
        items=items)
    # url_for('static', filename='.')

@app.route('/add', methods = ['GET', 'POST'])
def add():
    form = NewItemForm()

    if form.validate_on_submit():
        #filename = secure_filename(form.image.data.filename)

        # save new data here
        file = form.image.data

        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            key = form.key.data

            new_item = Item(key=key, image=filename)
            db.session.add(new_item)
            db.session.commit()

            return redirect('/')
    else:
        return render_template('add.html', 
            title = 'Add new item',
            form=form)
