"""
Entry points for managing a micro-http server to serve tables.
"""
import ast
import json
from bottle import run, jinja2_view, route, static_file, TEMPLATE_PATH
import os
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from dill import source

data = {}


@route("/static/<filename>")
def server_static(filename):
    abs_app_dir_path = os.path.dirname(os.path.realpath(__file__))
    root_path = os.path.join(abs_app_dir_path, 'static')
    return static_file(filename, root=root_path)


@route("/", name="home")
@jinja2_view("home.html")
def home():
    global data
    data["style"] = HtmlFormatter().get_style_defs(".highlight")
    data["code"] = highlight(
        "".join(data["src"]),
        PythonLexer(),
        HtmlFormatter(
            linenos=True, linenostart=data["co"]["co_firstlineno"], linespans="src"
        ),
    )
    return data


def start(host="localhost", port=8080):
    """
    Run the web server
    """
    # set TEMPLATE_PATH to use an absolute path pointing to our directory
    abs_app_dir_path = os.path.dirname(os.path.realpath(__file__))
    abs_views_path = os.path.join(abs_app_dir_path, "templates")
    TEMPLATE_PATH.insert(0, abs_views_path)
    run(host=host, port=port)
    print(f"Running web-server on http://{host}:{port}/")


def dedupe_nodes(l):
    new_list = []
    ids_collected = []
    for i in l:
        if i["id"] not in ids_collected:
            new_list.append(i)
            ids_collected.append(i["id"])
    return new_list


def node_properties(node):
    d = {}
    for field, value in ast.iter_fields(node):
        if isinstance(value, ast.AST):
            d[field] = node_properties(value)
        elif (
            isinstance(value, list) and len(value) > 0 and isinstance(value[0], ast.AST)
        ):
            d[field] = [node_properties(v) for v in value]
        else:
            d[field] = value
    return d


def node_to_dict(node, parent):
    i = []
    children = list(ast.iter_child_nodes(node))
    if len(children) > 0:
        for n in children:
            i.extend(node_to_dict(n, node))

    d = node_properties(node)
    if hasattr(node, "lineno"):
        d["lineno"] = node.lineno
    i.append(
        {
            "id": id(node),
            "name": type(node).__name__,
            "parent": id(parent),
            "data": json.dumps(d, skipkeys=True),
        }
    )
    return i


def show_code_object(obj, instructions):
    """
    Render code object
    """
    cobj = obj.__code__
    global data
    data["co"] = {
        attr: getattr(cobj, attr)
        for attr in dir(cobj)
        if attr.startswith("co_")
    }
    data["co"]["co_code"] = data["co"]["co_code"].hex()

    data["tpl_t"] = "CO"
    data["ins"] = list(instructions)

    (lines, start_line) = source.getsourcelines(obj)
    src = "".join(lines)
    tree = ast.parse(src, cobj.co_filename)
    nodes = node_to_dict(tree, None)
    data["nodes"] = dedupe_nodes(nodes)
    data["src"] = src
    data["last_line"] = start_line + len(lines)

    start()


def show_ast(ast):
    # Not implemented
    pass
