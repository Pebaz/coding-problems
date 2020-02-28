from tester import *

@test
def foo():
    assert 1 == 2

run_tests(trace=True)
