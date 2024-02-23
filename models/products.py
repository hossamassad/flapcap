from vending.base import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productName = db.Column(db.String(128))
    amountAvailable = db.Column(db.Integer)
    cost = db.Column(db.Integer)
    sellerId = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Product('{self.productName}', {self.amountAvailable}, {self.cost}, {self.sellerId})"