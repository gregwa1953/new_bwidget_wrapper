from .base import BWidgetBase

class ListBox(BWidgetBase):
    """
    The ListBox widget is an extension of the Tk listbox widget.
    """
    def __init__(self, master, **kwargs):
        """
        Initializes a new ListBox widget.

        Args:
            master: The parent widget.
            **kwargs: Configuration options for the ListBox.
        """
        super().__init__(master, 'ListBox', kwargs)