from decimal import Decimal

from braintree.attribute_getter import AttributeGetter as AttributeGetter

class TransactionDetails(AttributeGetter):
    amount: Decimal | None
    def __init__(self, attributes) -> None: ...
