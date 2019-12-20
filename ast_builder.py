from arpeggio import PTNodeVisitor
from ast_nodes import *

class ASTBuilder(PTNodeVisitor):

    def visit_robolang(self, node, children):
        #Since the only time that this is being visited by itself is at the beginning of the program
        #default count is 1, for "run the program once"
        return BlockNode(1, children)

    def visit_command(self, node, children):
        #R / L / F by themselves
        if len(children) == 1:
            return CommandNode(1, children[0])
        #count + R / count + L / count + F
        elif len(children) == 2:
            return CommandNode(children[0], children[1])
        #block [RF] (with or without count)    
        else:
            if(children[0] == "["):
                #count is default of 1, as it is not specified
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
