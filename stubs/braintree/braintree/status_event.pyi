from decimal import Decimal

from braintree.resource import Resource as Resource

class StatusEvent(Resource):
    amount: Decimal
    def __init__(self, gateway, attributes) -> None: ...
