# Generated from ./sky/Sky.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SkyParser import SkyParser
else:
    from SkyParser import SkyParser

# This class defines a complete listener for a parse tree produced by SkyParser.
class SkyListener(ParseTreeListener):

    # Enter a parse tree produced by SkyParser#Program.
    def enterProgram(self, ctx:SkyParser.ProgramContext):
        pass

    # Exit a parse tree produced by SkyParser#Program.
    def exitProgram(self, ctx:SkyParser.ProgramContext):
        pass


    # Enter a parse tree produced by SkyParser#Declaration.
    def enterDeclaration(self, ctx:SkyParser.DeclarationContext):
        pass

    # Exit a parse tree produced by SkyParser#Declaration.
    def exitDeclaration(self, ctx:SkyParser.DeclarationContext):
        pass


    # Enter a parse tree produced by SkyParser#Multiplication.
    def enterMultiplication(self, ctx:SkyParser.MultiplicationContext):
        pass

    # Exit a parse tree produced by SkyParser#Multiplication.
    def exitMultiplication(self, ctx:SkyParser.MultiplicationContext):
        pass


    # Enter a parse tree produced by SkyParser#Addition.
    def enterAddition(self, ctx:SkyParser.AdditionContext):
        pass

    # Exit a parse tree produced by SkyParser#Addition.
    def exitAddition(self, ctx:SkyParser.AdditionContext):
        pass


    # Enter a parse tree produced by SkyParser#Variable.
    def enterVariable(self, ctx:SkyParser.VariableContext):
        pass

    # Exit a parse tree produced by SkyParser#Variable.
    def exitVariable(self, ctx:SkyParser.VariableContext):
        pass


    # Enter a parse tree produced by SkyParser#Number.
    def enterNumber(self, ctx:SkyParser.NumberContext):
        pass

    # Exit a parse tree produced by SkyParser#Number.
    def exitNumber(self, ctx:SkyParser.NumberContext):
        pass


    # Enter a parse tree produced by SkyParser#Function.
    def enterFunction(self, ctx:SkyParser.FunctionContext):
        pass

    # Exit a parse tree produced by SkyParser#Function.
    def exitFunction(self, ctx:SkyParser.FunctionContext):
        pass



del SkyParser