from arpeggio import PTNodeVisitor
from ast_nodes import *

class ASTBuilder(PTNodeVisitor):

    def visit_robolang(self, node, children):
        return BlockNode(1, children)

    def visit_command(self, node, children):
        #R / L / F
        if len(children) == 1:
            return CommandNode(1, children[0])
        #count + R / count + L / count + F
        elif len(children) == 2:
            return CommandNode(children[0], children[1])
        #block [RF], etc    
        else:
            if(children[0] == "["):
                #count is default of 1
                return BlockNode(1, children[1])
            else:
                #count is specified as child[0]
                return BlockNode(children[0], children[2])


    def visit_motion(self, mode, children):
            return ForwardNode()

    def visit_turn(self, node, children):
            return TurnNode(children[0])

    def visit_objectmanip(self, node, children):
        return ObjManipNode(children[0])
