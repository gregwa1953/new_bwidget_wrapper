import os
import tkinter

# The version of the BWidget library.
__version__ = "1.10.1"

# Path to the BWidget Tcl library.
BWIDGET_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'bwidget-1.10.1')

def initialize(root):
    """
    Initializes the BWidget library for use with tkinter.

    This function must be called with the root tkinter window as an argument
    before any BWidgets can be used. It sets up the Tcl interpreter to find
    and load the BWidget package.

    Args:
        root: The root tkinter window (instance of tkinter.Tk).
    """
    tcl_interp = root.tk
    tcl_interp.eval(f'global auto_path; lappend auto_path {{{BWIDGET_PATH}}}')
    tcl_interp.eval('package require BWidget')

# Import all widget classes to make them available under the package namespace.
from .arrowbutton import ArrowButton
from .button import Button
from .buttonbox import ButtonBox
from .combobox import ComboBox
from .dialog import Dialog
from .entry import Entry
from .label import Label
from .labelframe import LabelFrame
from .listbox import ListBox
from .mainframe import MainFrame
from .notebook import NoteBook
from .panedwindow import PanedWindow
from .progressbar import ProgressBar
from .separator import Separator
from .spinbox import SpinBox
from .titleframe import TitleFrame
from .tree import Tree

__all__ = [
    "initialize",
    "ArrowButton",
    "Button",
    "ButtonBox",
    "ComboBox",
    "Dialog",
    "Entry",
    "Label",
    "LabelFrame",
    "ListBox",
    "MainFrame",
    "NoteBook",
    "PanedWindow",
    "ProgressBar",
    "Separator",
    "SpinBox",
    "TitleFrame",
    "Tree",
]