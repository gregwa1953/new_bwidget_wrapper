from .base import BWidgetBase

class ComboBox(BWidgetBase):
    """
    The ComboBox widget is an entry field with a dropdown list.
    """
    def __init__(self, master, **kwargs):
        """
        Initializes a new ComboBox widget.

        Args:
            master: The parent widget.
            **kwargs: Configuration options for the ComboBox.
        """
        super().__init__(master, 'ComboBox', kwargs)