"""
Simple unit testing module for quick tests during coding problems.
"""

tests = []


def test(func):
    global tests
    tests.append(func)
    return func


def run_tests(trace=False):
    global tests
    for each_test in tests:
        message = 'succeeded!'
        try:
            each_test()
        except AssertionError as e:
            if trace:
                raise e from e
            message = e.args[0] if e.args else ''
        finally:
            if message != 'succeeded!':
                if message:
                    status = f'failed: "{message}"'
                else:
                    status = 'failed.'
            else:
                status = message
            print(
                f'Test: "{each_test.__name__}" {status}'
            )


if __name__ == '__main__':
    @test
    def foo():
        assert 1 == 1, 'I am seriously worried'

    @test
    def foo2():
        assert 1 == 2

    @test
    def foo3():
        assert 1 == 3, 'hehehe'

    run_tests()
