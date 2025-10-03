from .base import BWidgetBase

class Tree(BWidgetBase):
    """
    The Tree widget displays a hierarchical list of items.
    """
    def __init__(self, master, **kwargs):
        """
        Initializes a new Tree widget.

        Args:
            master: The parent widget.
            **kwargs: Configuration options for the Tree.
        """
        super().__init__(master, 'Tree', kwargs)