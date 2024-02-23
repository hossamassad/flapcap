from vending.base import db

class Coinstack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    c5 = db.Column(db.Integer, default=40, nullable=False)
    c10 = db.Column(db.Integer, default=40, nullable=False)
    c20 = db.Column(db.Integer, default=40, nullable=False)
    c50 = db.Column(db.Integer, default=40, nullable=False)
    c100 = db.Column(db.Integer, default=40, nullable=False)

    def __repr__(self):
        return f"Coinstack(5c: '{self.c5}', 10c: '{self.c10}', 20c: '{self.c20}', 50c: '{self.c50}', 100c: '{self.c100}')"

