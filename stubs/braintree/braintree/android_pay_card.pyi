from _typeshed import Incomplete

from braintree.resource import Resource as Resource
from braintree.subscription import Subscription

class AndroidPayCard(Resource):
    is_expired: Incomplete
    subscriptions: list[Subscription]
    def __init__(self, gateway, attributes) -> None: ...
    @property
    def expiration_date(self): ...
    @property
    def last_4(self): ...
    @property
    def card_type(self): ...
    @staticmethod
    def signature(): ...
    @staticmethod
    def card_signature(): ...
    @staticmethod
    def network_token_signature(): ...
