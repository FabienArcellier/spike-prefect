import os

import alfred
import click

ROOT_DIR = os.path.realpath(os.path.join(__file__, "..", ".."))


@alfred.command("tests", help="workflow to execute all automatic tests")
def tests():
    """
    execute tests with unittests

    >>> $ alfred tests
    """
    python = alfred.sh("python")
    os.chdir(ROOT_DIR)
    alfred.run(python, ['-m', 'unittest', 'discover', 'tests'])




