# lbu-scrabble-club-testing

This repo contains implementations of classes for a Scrabble Club member, and for the Leaderboard.

There is a basic test class for `Member`, with one test. The mission is to increase the test 
coverage for each. It should be reasonably easy to get coverage for `Member` to 100%. Some magic 
would be needed to test the display methods in `Leaderboard`, but even without that, 70% or more is possible.

The classes are believed to be correct. Probably.

## Requirements

See `requirements.txt`, which should provide `coverage` and `pytest` (and its 
coverage plug-in). The simplest approach is to build a virtual environment from this.

## Running Tests

Running the tests from PyCharm should "just work". From the command line (this should work
without a virtual environment, as `unittest` is in the standard library):

    $ python3 -m unittest discover tests

(using `pytest` instead of `unittest` would also work. Try it.)

## Seeing Coverage

These need the virtual environment.

With `pytest`:

    $ python3 -m pytest --cov=scrabble_club --cov-report=term-missing tests/

With `coverage`:

    $ coverage run -m scrabble_club.member
    $ coverage report -m 

Note that the numbers used to work out the percentages refer to lines of code. 
So the current test (if you trace
it through) does give a promising start. The commands above will point out which
lines are untested.

