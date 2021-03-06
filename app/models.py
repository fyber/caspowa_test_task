from app import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(50), index=True, unique=True)
    image = db.Column(db.String(255), unique=True)

    def __repr__(self):
        return '<Item key: %r>' % (self.key)

