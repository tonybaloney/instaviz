"""
Entry points for managing a micro-http server to serve tables.
"""
from bottle import run
from bottle import jinja2_view, route

data = {}


@route('/', name='home')
@jinja2_view('home.html', template_lookup=['instaviz/templates'])
def home():
    global data
    return data


def start(host="localhost", port=8080):
    """
    Run the web server
    """
    run(host=host, port=port, reloader=True)
    print(f"Running web-server on http://{host}:{port}/")


def show_code_object(obj, instructions):
    """
    Render code object
    """
    global data
    data['co'] = obj
    data['tpl_t'] = "CO"
    data['ins'] = instructions
    start()


def show_ast(ast):
    # Not implemented
    pass