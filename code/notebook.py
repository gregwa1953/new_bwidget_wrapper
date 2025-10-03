from .base import BWidgetBase

class NoteBook(BWidgetBase):
    """
    The NoteBook widget manages a collection of pages (notebooks).
    """
    def __init__(self, master, **kwargs):
        """
        Initializes a new NoteBook widget.

        Args:
            master: The parent widget.
            **kwargs: Configuration options for the NoteBook.
        """
        super().__init__(master, 'NoteBook', kwargs)