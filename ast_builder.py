from arpeggio import PTNodeVisitor
from ast_nodes import *

class ASTBuilder(PTNodeVisitor):

    def visit_robolang(self, node, children):
        return BlockNode(children)

    def visit_command(self, node, children):
        return CommandNode(children[0])

    def visit_motion(self, mode, children):
        return ForwardNode()

    def visit_turn(self, node, children):
        return TurnNode(children[0])

    def visit_objectmanip(self, node, children):
        return ObjManipNode(children[0])
