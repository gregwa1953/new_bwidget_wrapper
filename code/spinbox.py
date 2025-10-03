from .base import BWidgetBase

class SpinBox(BWidgetBase):
    """
    The SpinBox widget is an entry-like widget with up/down arrows.
    """
    def __init__(self, master, **kwargs):
        """
        Initializes a new SpinBox widget.

        Args:
            master: The parent widget.
            **kwargs: Configuration options for the SpinBox.
        """
        super().__init__(master, 'SpinBox', kwargs)