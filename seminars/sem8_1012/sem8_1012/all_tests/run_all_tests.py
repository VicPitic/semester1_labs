from all_tests.tests_domain import *
from all_tests.repo_tests import *


def run_all():
    test_create_movie()
    test_domain_setters()
    test_validate_movie()
    test_create_movie()
    test_delete_movie()

    print("all tests have passed")