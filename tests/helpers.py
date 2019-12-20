from collections import deque
import sys,os,copy

sys.path.append(os.path.realpath('.'))
sys.path.append(os.path.realpath('..'))
from main import parse_and_run


logged_lines = deque()

def logger_init():
  logged_lines.clear()

def logger(action, position,direction,holding):
  logged_lines.append(
    copy.deepcopy([action, position,direction,holding])
  )

def logger_next_line():
  return logged_lines.popleft()

def logger_empty():
  return len(logged_lines) == 0

def dump():
  print("logged", repr(logged_lines))

def run_and_check(test, script, expected_lines):
    logger_init()
    parse_and_run(script, logger)

    for expected in expected_lines:
      got = logger_next_line()
      test.assertEqual(got, expected)

    test.assertTrue(logger_empty())