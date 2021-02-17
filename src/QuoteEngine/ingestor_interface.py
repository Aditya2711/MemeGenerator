"""Abstract base class.

A complete classmethod method to verify if the file type is compatible with
the ingestor class.
"""


from abc import ABC, abstractmethod
from typing import List
from .quote_model import QuoteModel


class IngestorInterface(ABC):
    """Abstarct class which is used for verification."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path):
        """Checks file comaptibility."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstarct method for pdarsing data."""
        pass
