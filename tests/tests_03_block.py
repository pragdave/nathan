import unittest
from helpers import logger, logger_init, logger_next_line, logger_empty, run_and_check


class TestCount(unittest.TestCase):

    def test_simple_block(self):
        run_and_check(
            self,
            "[FL]F[LF]LF",
            [
                ['F', [1, 0], [1, 0], []],
                ['L', [1, 0], [0, 1], []],
                ['F', [1, 1], [0, 1], []],
                ['L', [1, 1], [-1, 0], []],
                ['F', [0, 1], [-1, 0], []],
                ['L', [0, 1], [0, -1], []],
                ['F', [0, 0], [0, -1], []]
            ])

    def test_block_with_count(self):
        run_and_check(
            self,
            "F3[LF]",
            [
                ['F', [1, 0], [1, 0], []],
                ['L', [1, 0], [0, 1], []],
                ['F', [1, 1], [0, 1], []],
                ['L', [1, 1], [-1, 0], []],
                ['F', [0, 1], [-1, 0], []],
                ['L', [0, 1], [0, -1], []],
                ['F', [0, 0], [0, -1], []]
            ])

    def test_nested_block(self):
        run_and_check(
            self,
            "2[3[FL]L]",
            [
              [ "F",[1, 0],[1, 0],[] ],
              [ "L",[1, 0],[0, 1],[] ],
              [ "F",[1, 1],[0, 1],[] ],
              [ "L",[1, 1],[-1, 0],[] ],
              [ "F",[0, 1],[-1, 0],[] ],
              [ "L",[0, 1],[0, -1],[] ],
              [ "L",[0, 1],[1, 0],[] ],
              [ "F",[1, 1],[1, 0],[] ],
              [ "L",[1, 1],[0, 1],[] ],
              [ "F",[1, 2],[0, 1],[] ],
              [ "L",[1, 2],[-1, 0],[] ],
              [ "F",[0, 2],[-1, 0],[] ],
              [ "L",[0, 2],[0, -1],[] ],
              [ "L",[0, 2],[1, 0],[] ],
            ])
if __name__ == '__main__':
    unittest.main()
