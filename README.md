# instaviz
Instant visualization of Python AST and Code Objects.

## Usage

Instaviz is designed to be used like PDB, it will start a webserver when the `show()` function is called. Simply pass a class or function to be displayed

```python
def my_function():
    # your code
    ...

# your code
import instaviz; instaviz.show(my_function)

```

![](screenshot.png)

## Credits

This package bundles some 3rd party javascript libraries. All libraries are bundled in the package so that the WebUI doesn't need to make any requests to the internet to protect the privacy of your code.

[json2html](https://json2html.com/)
[json2html-visualizer](http://visualizer.json2html.com/)
[visjs](http://visjs.org/)