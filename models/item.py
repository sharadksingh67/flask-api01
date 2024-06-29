from db import db


class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey(
        "stores.id"), unique=False, nullable=False)

    store = db.relationship("StoreModel", back_populates="items")

    # Establishes a relationship between the ItemModel and another model called StoreModel. The back_populates="items" part indicates that the StoreModel has an attribute named items that is populated with all the items related to that store.
