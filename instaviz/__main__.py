from instaviz.web import show_code_object
import dis
import sys


def main(f):
    with open(f) as src:
        co = compile(src.read(), f, mode='exec')
        instructions = dis.get_instructions(co)
    show_code_object(co, instructions)

if __name__ == "__main__":
    main(sys.argv[1])
