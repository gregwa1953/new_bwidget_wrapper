from .base import BWidgetBase

class ProgressBar(BWidgetBase):
    """
    The ProgressBar widget shows the progress of a long-running operation.
    """
    def __init__(self, master, **kwargs):
        """
        Initializes a new ProgressBar widget.

        Args:
            master: The parent widget.
            **kwargs: Configuration options for the ProgressBar.
        """
        super().__init__(master, 'ProgressBar', kwargs)