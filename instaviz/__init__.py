"""
InstaViz - a tool for visulizing ASTs and CPython code objects in a web server.
"""

__version__ = "0.2.0"
from .web import show_ast, show_code_object
import ast
from dis import get_instructions


def show(obj):
    """
    Start a web server and show `obj` in the WebUI
    :param obj: Show an AST or code object.
    :type  obj: ``ast.AST` or `codeobject`
    :return:
    """
    if isinstance(obj, ast.AST):
        show_ast(obj)
    elif hasattr(obj, "__code__"):
        instructions = get_instructions(obj.__code__)
        show_code_object(obj.__code__, instructions)
    else:
        print("Not sure what to do with {0}".format(type(obj)))
        return
