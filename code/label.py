from .base import BWidgetBase

class Label(BWidgetBase):
    """
    The Label widget is an extension of the Tk label widget.
    """
    def __init__(self, master, **kwargs):
        """
        Initializes a new Label widget.

        Args:
            master: The parent widget.
            **kwargs: Configuration options for the Label.
        """
        super().__init__(master, 'Label', kwargs)