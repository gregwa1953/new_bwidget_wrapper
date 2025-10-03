from .base import BWidgetBase

class ArrowButton(BWidgetBase):
    """
    The ArrowButton widget displays a button with an arrow.
    """
    def __init__(self, master, **kwargs):
        """
        Initializes a new ArrowButton widget.

        Args:
            master: The parent widget.
            **kwargs: Configuration options for the ArrowButton.
        """
        super().__init__(master, 'ArrowButton', kwargs)