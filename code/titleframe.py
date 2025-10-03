from .base import BWidgetBase

class TitleFrame(BWidgetBase):
    """
    The TitleFrame widget is a frame with a title.
    """
    def __init__(self, master, **kwargs):
        """
        Initializes a new TitleFrame widget.

        Args:
            master: The parent widget.
            **kwargs: Configuration options for the TitleFrame.
        """
        super().__init__(master, 'TitleFrame', kwargs)