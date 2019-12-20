This assignment will let you demonstrate that you understand:

1. The use of a grammar to specify a language to a parsing tool.

2. The generation of an AST from a parse.

3. Visiting an AST in order to interpret it.

The language is designed to control a very silly robot. Initially it can

* more forward one foot  (F)
* turn 90º left (L) or 90º right (R)

The program "FLFRF" moves it from 0,0 to 0,1, turns left and moves to 1,1, then
turns right and moves to 2,1.

I've already written this functionality: it gives you a skeleton on which to
build your code.

During this assignment, you will extend it to support

* pick up a package at its current position (P)
* drop a package at its current position (D)
* the ability to move forward multiple feet in one command, and the ability
  to turn by multiples of 90º.
* the ability to create blocks of instructions to be repeated.

Here is what you have to do:

1. Fork this repo on github, then download the copy from your github
   account onto your local machine.

2. Validate that the basic functionality works. Run this command in the
   top-level directory

       python3  tests/tests_00_initial.py

   You should see:

       ...
       ----------------------------------------------------------------------
       Ran 3 tests in 0.002s
       OK

3. Familiarize yourself with the existing source.

4. Make the changes described below, and pass the corresponding tests.


### The Starting Point

This repository already contains the code for a robot that honors the F, L, and
R commands. The grammar for this, along with the interface to arpeggio that
parses using it, is in the file `grammar.py`.

This `parse` function in this file uses the argeggio `visit_parse_tree` function
to build an AST. This work is done by `ast_builder.py`, and the definitions of
the AST nodes are in ast_node.py.

The file `interpreter.py` is a visitor on the AST. It executes the commands in
the program fed to the parser.

The file `main.py` can be used to run the program manually. You pass it the
program source as a parameter, and it logs each step of the execution to
standard output.

For example:

~~~
python3 main.py FLFRF
F,[1, 0],[1, 0],[]
L,[1, 0],[0, 1],[]
F,[1, 1],[0, 1],[]
R,[1, 1],[1, 0],[]
F,[2, 1],[1, 0],[]
~~~

Each logging line contains 4 fields:

* the action performed
* the updated location of the robot [x,y]
* the direction the robot is moving [∂x,∂y]. These two values are added to the
  current location to get the nest location during an (F)orward action.
* the items the robot is carrying (empty until you add that code:)

This logging is used by the tests to verify the code. If you look at a test, it
is easy to see the input program and the expected logging.

### The Tests

There are 4 files containing tests in the `tests/` directory.They have 00, 01,
02, and 03 in their names. Initially only test_00_simple.py will pass. As you
implement the various tasks below, you'll be able to run additional test files.
Don't forget to run the older tests as well to make sure you haven't broken any
old functionality when adding new.

### Task 1: Add Pick and Drop

If you look at `interpreter.py`, you'll see that there's an instance variable
called `self.holding` that is initialized to an empty list. Your job is to
implement two new actions in the language that will manipulate that.

* the `P` action will pick up whatever is at the current square and push in onto
  the `holding` list. To simulate stuff on the floor, you'll push the
  coordinates of the current square as an `[x, y]` list.

* the `D` action pops off the last item added to `holding`. This simulates
  dropping something on the floor.

The logging shows the contents of `holding`. You can see P and D in action in
the following session (I added line numbers):

~~~
P,[0, 0],[1, 0],[[0, 0]]              # 1
F,[1, 0],[1, 0],[[0, 0]]              # 2
P,[1, 0],[1, 0],[[0, 0], [1, 0]]      # 3
F,[2, 0],[1, 0],[[0, 0], [1, 0]]      # 4
D,[2, 0],[1, 0],[[0, 0]]              # 5
D,[2, 0],[1, 0],[]                    # 6
~~~

On line 1 the robot executes a P action while at the starting position, As a
result, the `holding` variable (the last item on the log line) is `[[0,0]]`

The robot then moves forward to 1,0 and executes another P. The `holding` stack
is now `[[0, 0], [1, 0]]`. It then move forward again, and executes two D
actions. The first drops the `[1,0]` entry, and the second drops the `[0.0]`
entry, leaving `holding` empty.

You will need to alter the grammar, ast, and interpreter files for this.

When you are finished, run the tests:

~~~~
python tests/tests_00_initial.py
python tests/tests_01_pickdrop.py
~~~~

### Task 2: Add a Count

You will update the program to allow a count to be specified in front of F, R,
and L actions. This count will be stored in the AST alongside the actions, and
during interpretation the count will control the number of times the action is
performed. So "3F2R2F" moves forward three times, rotates right 90º twice (point
back the way it came) then moves forward 2, ending up one square from where it
started:

~~~
python3 main.py "3F2R2F"
F,[1, 0],[1, 0],[]
F,[2, 0],[1, 0],[]
F,[3, 0],[1, 0],[]
R,[3, 0],[0, -1],[]
R,[3, 0],[-1, 0],[]
F,[2, 0],[-1, 0],[]
F,[1, 0],[-1, 0],[]
~~~

The count is optional, and applies to the action that immediately follows it.

I strongly suggest you deal with the count at the `CommandNode` level, and not
in the individual actions.

When you are finished, run the tests:

~~~~
python tests/tests_00_initial.py
python tests/tests_01_pickdrop.py
python tests/tests_02_count.py
~~~~


### Task 3: Add blocks

You'll add blocks to the syntax. A block groups a set of actions so that they
can be treated as a single action by a count. You write a block as "[", the
actions, and "]". For example, the sequence `4[FL]` makes the robot visit the
corners of a square:

~~~
python3 main.py "4[FL]"
F,[1, 0],[1, 0],[]
L,[1, 0],[0, 1],[]
F,[1, 1],[0, 1],[]
L,[1, 1],[-1, 0],[]
F,[0, 1],[-1, 0],[]
L,[0, 1],[0, -1],[]
F,[0, 0],[0, -1],[]
L,[0, 0],[1, 0],[]
~~~

When you are finished, run the tests:

~~~~
python tests/tests_00_initial.py
python tests/tests_01_pickdrop.py
python tests/tests_02_count.py
python tests/tests_03_block.py
~~~~



## Grading

Each of the three tasks will be graded the same way, and each will contribute a
maximum of 50 points to the overall assignment grade.

For each task:

* if the tests pass: 40 points

* if the tests do not pass, I will judge how close to passing them the code is,
  and give you a proportion of the 40 points accordingly

For each task an additional 10 points is available depending on the quality of
the implementation. This uses the same criteria as the original assignment
(scaled down a little):

| | |
|-|-|
| The code is easy to understand.†            | 6% |
| Clear division between parsing and runtime  | 2% |
| Makes good use of features of parsing tool chosen | 2% |

(†) _Easy to understand_ means:

* well laid out (indentation, short lines, blank lines, etc)
* short methods/functions
* meaningful names
* complex code broken into smaller less complex chunks
* consistency
* and other _I'll know it when I don't understand it_ stuff

Thus you'd score 100% on the assignment if you have a grade of 150 points.