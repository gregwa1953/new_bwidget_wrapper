from .base import BWidgetBase

class Button(BWidgetBase):
    """
    The Button widget is an extension of the Tk button widget.
    """
    def __init__(self, master, **kwargs):
        """
        Initializes a new Button widget.

        Args:
            master: The parent widget.
            **kwargs: Configuration options for the Button.
        """
        super().__init__(master, 'Button', kwargs)