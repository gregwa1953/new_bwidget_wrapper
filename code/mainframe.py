from .base import BWidgetBase

class MainFrame(BWidgetBase):
    """
    The MainFrame widget provides a standard application window layout.
    """
    def __init__(self, master, **kwargs):
        """
        Initializes a new MainFrame widget.

        Args:
            master: The parent widget.
            **kwargs: Configuration options for the MainFrame.
        """
        super().__init__(master, 'MainFrame', kwargs)