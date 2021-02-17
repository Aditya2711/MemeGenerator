"""Represents a simple class for encapsulating quote body and author.

For any quote - this class is encapsulating the quotes body and its author
in a proper format.
"""


class QuoteModel:
    """A quotemodel object.

    A quote model object represent the actual structure of the quote which,
    comprises of its body and author name.
    """

    def __init__(self, body=None, author=None):
        """Create a new quotemeodel object.

        :param info: body and author for the given quote.
        """
        self.body = body
        self.author = author

    def __str__(self):
        """Return `str(self)`.

        A printable representation of this object.
        """
        return f"{self.body} - {self.author}"
