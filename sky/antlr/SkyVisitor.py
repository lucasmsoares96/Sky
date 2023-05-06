# Generated from ./sky/Sky.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SkyParser import SkyParser
else:
    from SkyParser import SkyParser

# This class defines a complete generic visitor for a parse tree produced by SkyParser.

class SkyVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SkyParser#Program.
    def visitProgram(self, ctx:SkyParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkyParser#Declaration.
    def visitDeclaration(self, ctx:SkyParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkyParser#Multiplication.
    def visitMultiplication(self, ctx:SkyParser.MultiplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkyParser#Addition.
    def visitAddition(self, ctx:SkyParser.AdditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkyParser#Variable.
    def visitVariable(self, ctx:SkyParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkyParser#Number.
    def visitNumber(self, ctx:SkyParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkyParser#Function.
    def visitFunction(self, ctx:SkyParser.FunctionContext):
        return self.visitChildren(ctx)



del SkyParser