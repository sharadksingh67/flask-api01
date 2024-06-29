from db import db


class StoreModel(db.Model):
    __tablename__ = "stores"

    # we will not use uuid
    id = db.Column(db.Integer, primary_key=True)  # start with 1, autoincrement

    name = db.Column(db.String(80))

    # items = db.relationship("ItemModel", back_populates="store",  lazy="dynamic")

    items = db.relationship(
        "ItemModel", back_populates="store", lazy="dynamic", cascade="all, delete")

    # back_populates="store": This argument specifies the name of a property on the ItemModel class that should be populated with the StoreModel instance that is related to the ItemModel instances.

    # Essentially, it sets up a two-way relationship, allowing both sides to access each other.

    # lazy="dynamic": This argument tells SQLAlchemy to not load the items automatically when creating a store.

    # lavy="immediate": Loads the related objects as soon as the parent is loaded

    # This is useful for performance reasons when dealing with large collections of related items, as it prevents SQLAlchemy from loading all related items into memory at once.

    # The "all, delete" setting means that when operations (like adding, updating, or deleting) are performed on a StoreModel instance, those operations will also be cascaded to the related ItemModel instances.
