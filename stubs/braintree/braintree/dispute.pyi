from _typeshed import Incomplete
from decimal import Decimal

from braintree.attribute_getter import AttributeGetter as AttributeGetter
from braintree.configuration import Configuration as Configuration
from braintree.dispute_details import (
    DisputeEvidence as DisputeEvidence,
    DisputePayPalMessage as DisputePayPalMessage,
    DisputeStatusHistory as DisputeStatusHistory,
)
from braintree.transaction_details import TransactionDetails as TransactionDetails

class Dispute(AttributeGetter):
    class Status:
        Accepted: str
        AutoAccepted: str
        Disputed: str
        Expired: str
        Lost: str
        Open: str
        UnderReview: str
        Won: str

    class Reason:
        CancelledRecurringTransaction: str
        CreditNotProcessed: str
        Duplicate: str
        Fraud: str
        General: str
        InvalidAccount: str
        NotRecognized: str
        ProductNotReceived: str
        ProductUnsatisfactory: str
        Retrieval: str
        TransactionAmountDiffers: str

    class Kind:
        Chargeback: str
        PreArbitration: str
        Retrieval: str

    class ChargebackProtectionLevel:
        Effortless: str
        Standard: str
        NotProtected: str

    class PreDisputeProgram:
        NONE: str
        VisaRdr: str

    class ProtectionLevel:
        EffortlessCBP: str
        StandardCBP: str
        NoProtection: str

    @staticmethod
    def accept(id): ...
    @staticmethod
    def add_file_evidence(dispute_id, document_upload_id): ...
    @staticmethod
    def add_text_evidence(id, content_or_request): ...
    @staticmethod
    def finalize(id): ...
    @staticmethod
    def find(id): ...
    @staticmethod
    def remove_evidence(id, evidence_id): ...
    @staticmethod
    def search(*query): ...
    amount: Decimal | None
    amount_disputed: Decimal | None
    amount_won: Decimal | None
    protection_level: Incomplete
    transaction_details: TransactionDetails
    transaction = transaction_details
    evidence: list[DisputeEvidence] | None
    paypal_messages: list[DisputePayPalMessage] | None
    status_history: list[DisputeStatusHistory] | None
    processor_comments: Incomplete
    forwarded_comments: processor_comments
    def __init__(self, attributes) -> None: ...
