"""To ingest the TEXT data.

This is used to ingest the text data using the abstarct ingestor class.
"""


from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel
from typing import List


class TextIngestor(IngestorInterface):
    """Ingests TEXT data."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Get TEXT data and parse it into body and author."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        with open(path, 'r') as infile:
            lines = infile.readlines()

        for quote in lines:
            new_quote = QuoteModel(quote.rstrip("\n").split(" - ")[0],
                                   quote.rstrip("\n").split(" - ")[1])
            quotes.append(new_quote)

        return quotes
