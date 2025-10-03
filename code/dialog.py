from .base import BWidgetBase

class Dialog(BWidgetBase):
    """
    The Dialog widget provides a base class for creating dialog windows.
    """
    def __init__(self, master, **kwargs):
        """
        Initializes a new Dialog widget.

        Args:
            master: The parent widget.
            **kwargs: Configuration options for the Dialog.
        """
        super().__init__(master, 'Dialog', kwargs)