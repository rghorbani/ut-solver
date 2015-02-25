from antlr4 import *

from mpsLexer import mpsLexer

from mpsParser import mpsParser

from mpsListener import *

import sys


def parsing_cuda():
    input = FileStream('cuda.txt')
    lexer = mpsLexer(input)
    stream = CommonTokenStream(lexer)
    parser = mpsParser(stream)
    tree = parser.modell()


def main(argv):

    input = FileStream(argv[1])

    lexer = mpsLexer(input)

    stream = CommonTokenStream(lexer)

    parser = mpsParser(stream)

    tree = parser.modell()

#    printer = modellPrinter()

#    walker = ParseTreeWalker()

#    walker.walk(printer, tree)


if __name__ == '__main__':

    main(sys.argv)
