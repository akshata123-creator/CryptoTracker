import sys
# sys.path.append(sys.path[0] + "/...")
import os

sys.path.append(os.getcwd())

from unittest import TestLoader, TestSuite, TextTestRunner
from Test.Scripts.test import test_LT_LoginPage
from Test.Scripts.register_test import test_RT_RegisterPage
from Test.Scripts.home_test import test_HT_HomePage
from Test.Scripts.search_test import test_ST_SearchPage
from Test.Scripts.developer_test import test_DT_Developer

import testtools as testtools

if __name__ == "__main__":
    test_loader = TestLoader()
    # Test Suite is used since there are multiple test cases
    test_suite = TestSuite((test_loader.loadTestsFromTestCase(test_LT_LoginPage),))
                            #test_loader.loadTestsFromTestCase(test_RT_RegisterPage),
                            #test_loader.loadTestsFromTestCase(test_HT_HomePage),
                            #test_loader.loadTestsFromTestCase(test_ST_SearchPage),
                            #test_loader.loadTestsFromTestCase(test_DT_Developer), ))
    '''
    test_suite = TestSuite((test_loader.loadTestsFromTestCase(test_ST_SearchPage),))
    # test_loader.loadTestsFromTestCase(test_RT_RegisterPage),
    # test_loader.loadTestsFromTestCase(test_HT_HomePage),
    # test_loader.loadTestsFromTestCase(test_ST_SearchPage),
    # test_loader.loadTestsFromTestCase(test_DT_Developer), ))
    '''
    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)
    # Refer https://testtools.readthedocs.io/en/latest/api.html for more information
    parallel_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in test_suite))
    parallel_suite.run(testtools.StreamResult())
