"""To ingest the PDF data.

This is used to ingest the pdf data using the abstarct ingestor class.
"""


import subprocess
import os
from .ingestor_interface import IngestorInterface
from .text_ingestor import TextIngestor


class PDFIngestor(IngestorInterface):
    """Ingests PDF data."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path):
        """Get PDF data and parse it into body and author."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        tempfile = '.\\converted.txt'
        pdftotext = '.\\pdftotext.exe'
        cmd = [pdftotext, '-layout', '-nopgbrk', path, tempfile]
        subprocess.run(cmd, shell=True, capture_output=True)
        quotes = TextIngestor.parse(tempfile)
        os.remove(tempfile)
        return quotes
