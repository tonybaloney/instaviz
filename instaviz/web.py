"""
Entry points for managing a micro-http server to serve tables.
"""
from bottle import run, jinja2_view, route, static_file

data = {}


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='instaviz/static')


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
    data['ins'] = list(instructions)
    # Read source code
    try:
        with open(obj.co_filename, "r") as source_f:
            src = source_f.readlines()
            src = src[obj.co_firstlineno-1:]
            data['src'] = src
    except FileNotFoundError:
        data['src'] = ''
    start()


def show_ast(ast):
    # Not implemented
    pass
