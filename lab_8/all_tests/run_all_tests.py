from all_tests.tests_domain.test_domain import run_domain_tests
from all_tests.tests_repo.test_repo import run_repo_tests
from all_tests.tests_service.test_service import run_service_tests
from all_tests.tests_service.test_reports import run_reports_tests

def run_tests():
    run_domain_tests()
    run_repo_tests()
    run_service_tests()
    run_reports_tests()
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
