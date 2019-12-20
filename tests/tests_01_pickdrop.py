import unittest
from helpers import logger, logger_init, logger_next_line, logger_empty, run_and_check


class TestPickDrop(unittest.TestCase):

    def test_single_pick(self):
        run_and_check(
            self,
            "P",
            [
                ["P", [0, 0], [1, 0], [[0, 0]]]
            ])

    def test_single_pickdrop(self):
        run_and_check(
            self,
            "PD",
            [
                ["P", [0, 0], [1, 0], [[0, 0]]],
                ["D", [0, 0], [1, 0], []],
            ])


    def test_collect_square(self):
        run_and_check(
            self,
            "P FP LFP LFP LF DDDD ",
            [
              [ "P",[0, 0],[1, 0],[[0, 0]]],
              [ "F",[1, 0],[1, 0],[[0, 0]]],
              [ "P",[1, 0],[1, 0],[[0, 0], [1, 0]]],
              [ "L",[1, 0],[0, 1],[[0, 0], [1, 0]]],
              [ "F",[1, 1],[0, 1],[[0, 0], [1, 0]]],
              [ "P",[1, 1],[0, 1],[[0, 0], [1, 0], [1, 1]]],
              [ "L",[1, 1],[-1, 0],[[0, 0], [1, 0], [1, 1]]],
              [ "F",[0, 1],[-1, 0],[[0, 0], [1, 0], [1, 1]]],
              [ "P",[0, 1],[-1, 0],[[0, 0], [1, 0], [1, 1], [0, 1]]],
              [ "L",[0, 1],[0, -1],[[0, 0], [1, 0], [1, 1], [0, 1]]],
              [ "F",[0, 0],[0, -1],[[0, 0], [1, 0], [1, 1], [0, 1]]],
              [ "D",[0, 0],[0, -1],[[0, 0], [1, 0], [1, 1]]],
              [ "D",[0, 0],[0, -1],[[0, 0], [1, 0]]],
              [ "D",[0, 0],[0, -1],[[0, 0]]],
              [ "D",[0, 0],[0, -1],[]],
            ])

if __name__ == '__main__':
    unittest.main()
