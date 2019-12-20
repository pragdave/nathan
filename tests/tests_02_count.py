import unittest
from helpers import logger, logger_init, logger_next_line, logger_empty, run_and_check


class TestCount(unittest.TestCase):

    def test_non_count(self):
        run_and_check(
            self,
            "FLFLFLF",
            [
                ['F', [1, 0], [1, 0], []],
                ['L', [1, 0], [0, 1], []],
                ['F', [1, 1], [0, 1], []],
                ['L', [1, 1], [-1, 0], []],
                ['F', [0, 1], [-1, 0], []],
                ['L', [0, 1], [0, -1], []],
                ['F', [0, 0], [0, -1], []]
            ])

    def test_square_with_count(self):
         run_and_check(
            self,
            "2FL2FL2FL2F",
            [
              [ "F",[1, 0],[1, 0],[] ],
              [ "F",[2, 0],[1, 0],[] ],
              [ "L",[2, 0],[0, 1],[] ],
              [ "F",[2, 1],[0, 1],[] ],
              [ "F",[2, 2],[0, 1],[] ],
              [ "L",[2, 2],[-1, 0],[] ],
              [ "F",[1, 2],[-1, 0],[] ],
              [ "F",[0, 2],[-1, 0],[] ],
              [ "L",[0, 2],[0, -1],[] ],
              [ "F",[0, 1],[0, -1],[] ],
              [ "F",[0, 0],[0, -1],[] ],
            ])

    def test_three_lefts_make_a_right(self):
         run_and_check(
            self,
            "3L",
            [
              [ "L",[0, 0],[0,  1],[] ],
              [ "L",[0, 0],[-1, 0],[] ],
              [ "L",[0, 0],[0, -1],[] ],
            ])

    def test_three_rights_dont_make_a_pun(self):
         run_and_check(
            self,
            "3R",
            [
              [ "R",[0, 0],[0, -1],[] ],
              [ "R",[0, 0],[-1, 0],[] ],
              [ "R",[0, 0],[0,  1],[] ],
            ])

if __name__ == '__main__':
    unittest.main()
