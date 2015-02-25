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