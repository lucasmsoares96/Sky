import ast
from sys import argv

import antlr4

from sky.antlr.SkyLexer import SkyLexer
from sky.antlr.SkyParser import SkyParser
from sky.SkyInterpreter import SkyInterpreter

if __name__ == "__main__":
    input_stream = antlr4.FileStream(argv[1])
    lexer = SkyLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = SkyParser(stream)
    tree = parser.prog()

    python_ast = SkyInterpreter().visit(tree)
    print(ast.dump(python_ast, indent=2))
    python_code = compile(python_ast, "<string>", "exec")

    exec(python_code)
