from .base import BWidgetBase

class LabelFrame(BWidgetBase):
    """
    The LabelFrame widget is a frame with a label.
    """
    def __init__(self, master, **kwargs):
        """
        Initializes a new LabelFrame widget.

        Args:
            master: The parent widget.
            **kwargs: Configuration options for the LabelFrame.
        """
        super().__init__(master, 'LabelFrame', kwargs)