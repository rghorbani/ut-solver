from antlr4 import *
from mpsLexer import mpsLexer
from mpsParser import mpsParser
from mpsListener import *
import sys
from ut_solver.settings import BASE_DIR



def parsing_cuda():
    input = FileStream(BASE_DIR + '/cuda.txt')
    lexer = mpsLexer(input)
    stream = CommonTokenStream(lexer)
    parser = mpsParser(stream)
    tree = parser.modell()