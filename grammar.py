from arpeggio.cleanpeg import ParserPEG
from arpeggio import ParserPython, visit_parse_tree

from ast_builder import ASTBuilder

grammar = """
start =
  robolang EOF

robolang =
  command+

command =
      motion
  /   turn

motion =
  "F"

turn =
  "R" / "L"
"""

parser = ParserPEG(grammar, "start", debug=False, reduce_tree=False)


def parse(source):
    parse_tree = parser.parse(source)
    return visit_parse_tree(parse_tree, ASTBuilder(debug=False))
