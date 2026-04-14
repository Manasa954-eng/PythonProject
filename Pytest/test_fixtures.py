#fixtures are something like Predecessors. If the method name is given in argument, the arguments content is run first, later that method
#Yield is a part of fixture, whatever is written in it is executed at last. Like a Successor

import pytest


@pytest.fixture()
def test_firstrun():
    print("When given my method name it will be run first")
    yield
    print("Whatever comes after yield is run at last")

def test_secondrun(test_firstrun):
    print("Runs Second")