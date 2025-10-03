from .base import BWidgetBase

class Entry(BWidgetBase):
    """
    The Entry widget is an extension of the Tk entry widget.
    """
    def __init__(self, master, **kwargs):
        """
        Initializes a new Entry widget.

        Args:
            master: The parent widget.
            **kwargs: Configuration options for the Entry.
        """
        super().__init__(master, 'Entry', kwargs)