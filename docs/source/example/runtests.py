from proboscis import register
from proboscis import TestProgram

if __name__ == '__main__':
    # Import all modules which have been decorated with @test.
    from tests import util_test
    from tests import service_tests

    # Now create some groups of groups.
    register(groups=["fast"], depends_on_groups=["unit"])
    register(groups=["integration"],
             depends_on_groups=["service.initialize",
                                "service.tests",
                                "service.shutdown"])
    register(groups=["slow"],
             depends_on_groups=["fast", "integration"])

    # Run Proboscis and exit.
    TestProgram().run_and_exit()