"""Ingestor class for validation.

To select the appropriate helper class for a given file based on filetype.
"""


from typing import List
from .docx_ingestor import DocxIngestor
from .csv_ingestor import CSVIngestor
from .text_ingestor import TextIngestor
from .pdf_ingestor import PDFIngestor
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class Ingestor(IngestorInterface):
    """Identifies the correct helper class."""

    ingestors = [DocxIngestor, CSVIngestor, TextIngestor, PDFIngestor]
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Select the appropriate helper for a given file based on filetype."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
