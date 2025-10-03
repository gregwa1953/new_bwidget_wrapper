from .base import BWidgetBase

class PanedWindow(BWidgetBase):
    """
    The PanedWindow widget allows for the creation of resizable panes.
    """
    def __init__(self, master, **kwargs):
        """
        Initializes a new PanedWindow widget.

        Args:
            master: The parent widget.
            **kwargs: Configuration options for the PanedWindow.
        """
        super().__init__(master, 'PanedWindow', kwargs)