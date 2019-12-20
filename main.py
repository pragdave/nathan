from grammar     import parse
from interpreter import Interpreter
import sys

def logger(action, position,direction,holding):
    print(f"{action},{position},{direction},{holding}")

def parse_and_run(src, logger):
    ast = parse(src)
    ast.accept(Interpreter(logger))

if __name__ == '__main__':
    parse_and_run("sys.argv[1]", logger)
