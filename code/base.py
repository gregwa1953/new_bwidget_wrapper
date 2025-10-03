import tkinter

class BWidgetBase(tkinter.Widget):
    """
    Base class for all BWidget wrappers in tkinter.

    This class provides the fundamental functionality for creating and managing
    BWidgets. It should not be instantiated directly but should be subclassed
    for each specific BWidget.
    """
    def __init__(self, master, bwidget_name, cnf={}, **kw):
        """
        Initializes a BWidget wrapper.

        Args:
            master: The parent widget.
            bwidget_name (str): The Tcl command for creating the BWidget 
                                (e.g., 'Button', 'Label').
            cnf (dict): A dictionary of configuration options.
            **kw: Additional configuration options as keyword arguments.
        """
        # Merge cnf and kw, with kw taking precedence
        if cnf and kw:
            cnf.update(kw)
        elif not cnf and kw:
            cnf = kw
        
        # Initialize the base tkinter.Widget
        tkinter.Widget.__init__(self, master, bwidget_name, cnf)

    def __setitem__(self, key, value):
        """Allows configuration of widget options using dictionary-style assignment."""
        self.configure({key: value})

    def __getitem__(self, key):
        """Allows retrieval of widget option values using dictionary-style access."""
        return self.cget(key)

    @property
    def master(self):
        """Returns the master widget for this widget."""
        return self._master

    def destroy(self):
        """Destroys this widget and all its descendants."""
        super().destroy()