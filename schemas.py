from marshmallow import Schema, fields


# This is a schema for the Item model without the store relationship
class PlainItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)


class PlainStoreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


# This is a schema for the Item model with the store relationship
class ItemSchema(PlainItemSchema):
    # This field is only for loading data from the client
    store_id = fields.Int(required=True, load_only=True)
    # This field is only for dumping data to the client
    store = fields.Nested(PlainStoreSchema(), dump_only=True)


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()
    store_id = fields.Int()


class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
