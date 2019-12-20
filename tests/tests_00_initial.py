import unittest
from helpers import logger, logger_init, logger_next_line, logger_empty, run_and_check


class TestBasicMovement(unittest.TestCase):

  def test_single_command(self):
    run_and_check(self, "F", [["F",[1, 0],[1, 0],[]]])

  def test_rotation_doesnt_move(self):
    run_and_check(self, "R", [["R",[0, 0],[0, -1],[]]])
    run_and_check(self, "L", [["L",[0, 0],[0,  1],[]]])

  def test_square(self):
    run_and_check(
      self,
      "FLFLFLF",
      [
        [ 'F',[1, 0],[1, 0],[] ],
        [ 'L',[1, 0],[0, 1],[] ],
        [ 'F',[1, 1],[0, 1],[] ],
        [ 'L',[1, 1],[-1, 0],[] ],
        [ 'F',[0, 1],[-1, 0],[] ],
        [ 'L',[0, 1],[0, -1],[] ],
        [ 'F',[0, 0],[0,-1],[] ]
      ])


if __name__ == '__main__':
    unittest.main()