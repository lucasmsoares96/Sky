from typing import Any

import ast

from .antlr.SkyParser import SkyParser
from .antlr.SkyVisitor import SkyVisitor


class SkyInterpreter(SkyVisitor):
    variables: dict[str, Any] = {}

    def visitProgram(self, ctx: SkyParser.ProgramContext) -> ast.Module:
        body = []
        for stmt in ctx.children:
            node = self.visit(stmt)
            if node is not None:
                body.append(node)
        fixed = ast.fix_missing_locations(ast.Module(body=body, type_ignores=[]))
        return fixed

    def visitDeclaration(self, ctx: SkyParser.DeclarationContext) -> ast.Assign:
        name = ctx.ID().getText()
        value = ctx.NUM().getText()
        ast_name = ast.Name(id=name, ctx=ast.Store())
        ast_value = ast.Num(n=value)
        variable = ast.Assign(targets=[ast_name], value=ast_value)
        self.variables[name] = value
        return variable

    def visitMultiplication(self, ctx: SkyParser.MultiplicationContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return ast.BinOp(left=left, op=ast.Mult(), right=right)

    def visitAddition(self, ctx: SkyParser.AdditionContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return ast.BinOp(left=left, op=ast.Add(), right=right)

    def visitVariable(self, ctx: SkyParser.VariableContext):
        return ast.Name(id=ctx.ID().getText(), ctx=ast.Load())

    def visitNumber(self, ctx: SkyParser.NumberContext):
        return ast.Constant(value=int(ctx.NUM().getText()))

    def visitFunction(self, ctx: SkyParser.FunctionContext) -> ast.Expr:
        name = ctx.getChild(0).getText()
        argument = ctx.getChild(2).getText()
        ast_argument = ast.Name(id=argument, ctx=ast.Load())
        ast_name = ast.Name(id=name, ctx=ast.Load())
        if argument in self.variables:
            return ast.Expr(
                value=ast.Call(func=ast_name, args=[ast_argument], keywords=[])
            )
        else:
            print("Error: Variable not found")
