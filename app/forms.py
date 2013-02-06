from flask.ext.wtf import Form, TextField, FileField
from flask.ext.wtf import Required

class NewItemForm(Form):
    key = TextField('key', validators=[Required()])
    image = FileField('image', validators=[Required()])
