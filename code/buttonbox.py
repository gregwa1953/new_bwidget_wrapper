from .base import BWidgetBase

class ButtonBox(BWidgetBase):
    """
    The ButtonBox widget displays a box with buttons.
    """
    def __init__(self, master, **kwargs):
        """
        Initializes a new ButtonBox widget.

        Args:
            master: The parent widget.
            **kwargs: Configuration options for the ButtonBox.
        """
        super().__init__(master, 'ButtonBox', kwargs)