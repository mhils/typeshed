from braintree.resource import Resource as Resource
from braintree.subscription import Subscription

class VenmoAccount(Resource):
    subscriptions: list[Subscription]
    def __init__(self, gateway, attributes) -> None: ...
