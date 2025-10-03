from .base import BWidgetBase

class Separator(BWidgetBase):
    """
    The Separator widget displays a horizontal or vertical separator line.
    """
    def __init__(self, master, **kwargs):
        """
        Initializes a new Separator widget.

        Args:
            master: The parent widget.
            **kwargs: Configuration options for the Separator.
        """
        super().__init__(master, 'Separator', kwargs)