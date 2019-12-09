"""
InstaViz - a tool for visualizing ASTs and CPython code objects in a web server.
"""

__version__ = "0.6.0"
from .web import show_ast, show_code_object
from dis import get_instructions


def show(obj):
    """
    Start a web server and show `obj` in the WebUI
    Assumes `obj` is compiled and has `__code__` attribute.
    :return:
    """
    if hasattr(obj, "__code__"):
        instructions = get_instructions(obj.__code__)
        show_code_object(obj, instructions)
    else:
        print("{0} is not compiled, could not locate __code__ attribute.".format(type(obj)))
        return
