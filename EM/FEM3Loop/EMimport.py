from IPython.display import HTML
from IPython.display import set_matplotlib_formats
import matplotlib
set_matplotlib_formats('png')
matplotlib.rcParams['savefig.dpi'] = 100 # Change this to adjust figure size
from IPython.html.widgets import *
from FEM3loop import fem3loop, interactfem3loop
