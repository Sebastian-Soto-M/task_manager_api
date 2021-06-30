from unittest import TestSuite, TextTestRunner, makeSuite

def get_suite() -> TestSuite:
    suite = TestSuite()
    selected_suite = CLI_OPTS.suite
    if selected_suite != False:
        suite.addTest(makeSuite(TESTS[selected_suite]))
    else:
        tests = set()
        for k, v in TESTS.items():
            tests.add(f'Test{k.capitalize()}')
            suite.addTest(makeSuite(v))
    return suite


if __name__ == "__main__":
    runner = TextTestRunner()
    runner.run(get_suite())
